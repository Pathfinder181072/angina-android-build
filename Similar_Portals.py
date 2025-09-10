import requests
import time
import socket
import re
import os
import sys
import itertools
import threading
import json
import ssl
from datetime import datetime, timezone

# Try to import colorama with fallback for QPython
try:
    from colorama import Fore, Style, init
    COLORAMA_AVAILABLE = True
except ImportError:
    # Create basic color placeholders if colorama is not available
    class Fore:
        RED = YELLOW = GREEN = CYAN = MAGENTA = WHITE = LIGHTGREEN_EX = LIGHTYELLOW_EX = LIGHTBLUE_EX = LIGHTMAGENTA_EX = ''
    class Style:
        BRIGHT = RESET_ALL = ''
    def init(autoreset=True): 
        pass
    COLORAMA_AVAILABLE = False

# Initialize colors only if colorama is available
if COLORAMA_AVAILABLE:
    init(autoreset=True)

# Get the script's directory and name
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_NAME = os.path.splitext(os.path.basename(__file__))[0]
OUTPUT_FOLDER = os.path.join(SCRIPT_DIR, SCRIPT_NAME)

# API key
API_KEY = "01990b54-2cad-730c-8107-fa36271e7a4c"
HEADERS = {"API-Key": API_KEY, "Content-Type": "application/json"}

SCAN_ENDPOINT = "https://urlscan.io/api/v1/scan/"
RESULT_ENDPOINT = "https://urlscan.io/api/v1/result/"
SEARCH_ENDPOINT = "https://urlscan.io/api/v1/search/"

stop_spinner = False  # Flag to stop spinner thread
session_stats = {
    "scans_completed": 0,
    "portals_found": 0,
    "files_created": [],
    "start_time": datetime.now(timezone.utc)
}

def install_missing_packages():
    """Check and install missing packages"""
    missing_packages = []
    
    # Check for colorama
    try:
        import colorama
    except ImportError:
        missing_packages.append("colorama")
    
    # Install missing packages
    if missing_packages:
        print("Installing missing packages:", missing_packages)
        try:
            # For QPython (using pip from Python)
            import pip
            for package in missing_packages:
                pip.main(['install', package])
        except:
            # For systems where pip is available as a module
            try:
                import subprocess
                for package in missing_packages:
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            except:
                print("Could not automatically install missing packages.")
                print("Please install manually: " + ", ".join(missing_packages))
        
        # Reinitialize colorama if it was just installed
        if "colorama" in missing_packages:
            global Fore, Style, init, COLORAMA_AVAILABLE
            from colorama import Fore, Style, init
            init(autoreset=True)
            COLORAMA_AVAILABLE = True

def ensure_output_folder():
    """Create the output folder if it doesn't exist"""
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        if COLORAMA_AVAILABLE:
            print(f"{Fore.GREEN}📁 Created output folder: {OUTPUT_FOLDER}{Style.RESET_ALL}")
        else:
            print(f"📁 Created output folder: {OUTPUT_FOLDER}")
    return OUTPUT_FOLDER

def typewriter(text, color=Fore.MAGENTA if COLORAMA_AVAILABLE else '', delay=0.02):
    """Print text with typewriter animation"""
    for char in text:
        sys.stdout.write(color + (Style.BRIGHT if COLORAMA_AVAILABLE else '') + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animated_banner():
    """Display an animated banner"""
    os.system('cls' if os.name == 'nt' else 'clear')
    banner_frames = [
        r"""
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║    🖤 𝗔𝗡𝗚𝗜𝗡𝗔™ 🖤  SIMILAR PORTALS TOOL ⚙️            ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
        """,
        r"""
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║    💎 𝗔𝗡𝗚𝗜𝗡𝗔™ 💎  SIMILAR PORTALS TOOL ⚙️            ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
        """
    ]
    
    for frame in banner_frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.MAGENTA + frame if COLORAMA_AVAILABLE else frame)
        time.sleep(0.3)
    
    print("\n")

def clear_screen():
    """Clear screen in a cross-platform way"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_intro():
    """Show introductory message"""
    clear_screen()
    animated_banner()
    print((Fore.CYAN if COLORAMA_AVAILABLE else '') + "🌟 Welcome to the Angina Similar Portals Finder!")
    print((Fore.CYAN if COLORAMA_AVAILABLE else '') + "🔍 This tool helps you find similar portals using urlscan.io")
    print((Fore.CYAN if COLORAMA_AVAILABLE else '') + "📝 Enter an IPTV portal URL to begin...\n")
    
    # Display output folder info
    save_dir = ensure_output_folder()
    print((Fore.CYAN if COLORAMA_AVAILABLE else '') + f"📁 Output folder: {save_dir}")
    
    # Display quick stats if available
    if session_stats["scans_completed"] > 0:
        print((Fore.LIGHTMAGENTA_EX if COLORAMA_AVAILABLE else '') + 
              f"📊 Session: {session_stats['scans_completed']} scans | {session_stats['portals_found']} portals found")
    print()

def normalize_url(url):
    url = url.strip()
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    if not url.endswith("/c/"):
        if not url.endswith("/"):
            url += "/"
        url += "c/"
    return url

def extract_ip(url):
    try:
        domain = re.findall(r"https?://([^/:]+)", url)[0]
        return socket.gethostbyname(domain)
    except Exception:
        return None

def check_online_status(url, timeout=10):
    """Check if a URL is online or down with detailed information"""
    try:
        # Check the URL as-is (with /c/ path)
        start_time = time.time()
        response = requests.get(url, timeout=timeout, allow_redirects=True)
        response_time = round((time.time() - start_time) * 1000, 1)  # in ms
        
        # Check SSL certificate
        ssl_valid = "Yes"
        try:
            if url.startswith('https://'):
                hostname = url.split('//')[1].split('/')[0]
                context = ssl.create_default_context()
                with socket.create_connection((hostname, 443), timeout=timeout) as sock:
                    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                        pass
        except:
            ssl_valid = "No"
        
        # Get status category
        status_category = "Unknown"
        if response.status_code < 300:
            status_category = "Success (<300)"
        elif response.status_code < 400:
            status_category = "Redirection (<400)"
        elif response.status_code < 500:
            status_category = "Client Error (<500)"
        else:
            status_category = "Server Error (>=500)"
            
        if response.status_code < 400:
            return True, f"🟢 ONLINE", Fore.GREEN, {
                "status_code": response.status_code,
                "response_time": response_time,
                "ssl_valid": ssl_valid,
                "status_category": status_category
            }
        else:
            return False, f"🔴 DOWN", Fore.RED, {
                "status_code": response.status_code,
                "response_time": response_time,
                "ssl_valid": ssl_valid,
                "status_category": status_category
            }
    except requests.exceptions.ConnectionError:
        return False, "🔴 DOWN (Connection Error)", Fore.RED, {}
    except requests.exceptions.Timeout:
        return False, "🔴 DOWN (Timeout)", Fore.RED, {}
    except requests.exceptions.RequestException as e:
        return False, f"🔴 DOWN (Request Error)", Fore.RED, {}
    except Exception as e:
        return False, f"🔴 DOWN (Unknown Error)", Fore.RED, {}

def get_ip_info(ip):
    """Get country and flag for IP using ipwhois.app (more reliable free API)"""
    try:
        resp = requests.get(f"https://ipwhois.app/json/{ip}", timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            country = data.get("country", "Unknown")
            cc = data.get("country_code", "")
            flag = "".join([chr(127397 + ord(c)) for c in cc.upper()]) if cc else "🏳️"
            return country, flag
    except Exception:
        pass
    return "Unknown", "🏳️"

def scan_url(url):
    try:
        resp = requests.post(SCAN_ENDPOINT, json={"url": url, "visibility": "public"}, headers=HEADERS, timeout=30)
        if resp.status_code not in (200, 201):
            print((Fore.RED if COLORAMA_AVAILABLE else '') + f"❌ Scan submission failed ({resp.status_code}) → {resp.text}")
            return None
        return resp.json().get("uuid")
    except requests.exceptions.RequestException as e:
        print((Fore.RED if COLORAMA_AVAILABLE else '') + f"❌ Request error: {e}")
        return None

def fancy_spinner_animation(message="⏳ Processing your request..."):
    """A more visually appealing spinner"""
    spinner_frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    frame_index = 0
    
    while not stop_spinner:
        sys.stdout.write((Fore.YELLOW if COLORAMA_AVAILABLE else '') + 
                         f"\r{message} {spinner_frames[frame_index]} ")
        sys.stdout.flush()
        time.sleep(0.1)
        frame_index = (frame_index + 1) % len(spinner_frames)
    
    sys.stdout.write("\r" + " " * (len(message) + 4) + "\r")  # clear line

def get_scan_result(uuid):
    global stop_spinner
    url = RESULT_ENDPOINT + uuid + "/"

    # Start spinner
    stop_spinner = False
    spinner = threading.Thread(target=fancy_spinner_animation)
    spinner.start()

    try:
        for _ in range(30):  # try up to ~60 seconds
            resp = requests.get(url, headers=HEADERS, timeout=10)
            if resp.status_code == 200:
                stop_spinner = True
                spinner.join()
                return resp.json()
            time.sleep(2)
    except requests.exceptions.RequestException:
        pass

    stop_spinner = True
    spinner.join()
    return None

def search_by_ip(ip):
    try:
        params = {"q": f"page.ip:{ip}", "size": 50}
        resp = requests.get(SEARCH_ENDPOINT, headers=HEADERS, params=params, timeout=10)
        if resp.status_code != 200:
            print((Fore.RED if COLORAMA_AVAILABLE else '') + f"❌ Search failed ({resp.status_code}) → {resp.text}")
            return []
        return [item.get("page", {}).get("url") for item in resp.json().get("results", []) if item.get("page")]
    except requests.exceptions.RequestException:
        return []

def save_results(url, ip, country, flag, results, online_status, status_details):
    # Ensure output folder exists
    save_dir = ensure_output_folder()
    
    # Create a safe filename with URL and date
    safe_name = re.sub(r'[^a-zA-Z0-9]', '_', url.replace("http://", "").replace("https://", "").split('/')[0])
    date_str = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    file_name = f"{safe_name}_{date_str}.txt"
    file_path = os.path.join(save_dir, file_name)
    
    current_time = datetime.now(timezone.utc).strftime("%d-%m-%Y %H:%M:%S UTC")
    with open(file_path, "w", encoding="utf-8") as f:
        # Add a fancy header
        f.write("╔══════════════════════════════════════════════════════════╗\n")
        f.write("║                 🖤 𝗔𝗡𝗚𝗜𝗡𝗔™ 🖤                         ║\n")
        f.write("║               SIMILAR PORTALS REPORT                    ║\n")
        f.write("╚══════════════════════════════════════════════════════════╝\n\n")
        
        f.write(f"🗒 Search Results:\n   {'─'*15} \n")
        f.write(f"🌐 Original URL: {url}\n")
        f.write(f"🔢 Resolved IP: {ip}\n")
        f.write(f"🌍 Location: {country} {flag}\n")
        f.write(f"📶 Status: {online_status}\n")
        
        # Add additional status details if available
        if status_details:
            if 'status_code' in status_details:
                f.write(f"Status Code: {status_details['status_code']}\n")
            if 'status_category' in status_details:
                f.write(f"Status Category: {status_details['status_category']}\n")
            if 'response_time' in status_details:
                f.write(f"Response Time: {status_details['response_time']}ms\n")
            if 'ssl_valid' in status_details:
                f.write(f"SSL Valid: {status_details['ssl_valid']}\n")
        
        f.write(f"Time: {current_time}\n\n")
        
        if not results:
            f.write("No similar portals found.\n")
        else:
            f.write(f"Similar portals found ({len(results)}):\n")
            f.write("─" * 50 + "\n")
            for i, r in enumerate(results, 1):
                f.write(f"{i:2d}. {r}\n")
    
    print((Fore.YELLOW if COLORAMA_AVAILABLE else '') + f"\n💾 Results saved to {file_path}")
    return file_path

def display_results(url, ip, country, flag, results, online_status, status_color, status_details):
    """Display results in an attractive way"""
    print("\n" + "═"*60)
    print((Fore.GREEN if COLORAMA_AVAILABLE else '') + "✅ SCAN COMPLETED SUCCESSFULLY")
    print("═"*60)
    print((Fore.CYAN if COLORAMA_AVAILABLE else '') + f"🌐 Original URL: {url}")
    print((Fore.CYAN if COLORAMA_AVAILABLE else '') + f"🔢 Resolved IP: {ip}")
    print((Fore.CYAN if COLORAMA_AVAILABLE else '') + f"🌍 Location: {country} {flag}")
    print(status_color + f"📶 Status: {online_status}")
    
    # Show additional status details if available
    if status_details:
        if 'status_code' in status_details:
            print((Fore.CYAN if COLORAMA_AVAILABLE else '') + f"Status Code: {status_details['status_code']}")
        if 'status_category' in status_details:
            print((Fore.CYAN if COLORAMA_AVAILABLE else '') + f"Status Category: {status_details['status_category']}")
        if 'response_time' in status_details:
            print((Fore.CYAN if COLORAMA_AVAILABLE else '') + f"Response Time: {status_details['response_time']}ms")
        if 'ssl_valid' in status_details:
            print((Fore.CYAN if COLORAMA_AVAILABLE else '') + f"SSL Valid: {status_details['ssl_valid']}")
    
    print("─"*60)
    
    if results:
        print((Fore.GREEN if COLORAMA_AVAILABLE else '') + f"🔗 Found {len(results)} similar portals:")
        print((Fore.WHITE if COLORAMA_AVAILABLE else '') + "─"*60)
        for i, r in enumerate(results, 1):
            print(f"{i:2d}. {r}")
    else:
        print((Fore.RED if COLORAMA_AVAILABLE else '') + "⚠ No similar portals found.")
    print("═"*60)

def get_user_input():
    """Get user input with attractive prompt"""
    print("\n")
    print((Fore.LIGHTBLUE_EX if COLORAMA_AVAILABLE else '') + "Please enter an IPTV portal URL")
    print((Fore.LIGHTBLUE_EX if COLORAMA_AVAILABLE else '') + "Example: example.com or http://example.com/c/")
    print((Fore.YELLOW if COLORAMA_AVAILABLE else '') + ">" * 40)
    
    try:
        # Set text color for input to ensure visibility
        if COLORAMA_AVAILABLE:
            sys.stdout.write(Fore.WHITE + Style.BRIGHT)
        raw = input("👉 URL: ").strip()
        if COLORAMA_AVAILABLE:
            sys.stdout.write(Style.RESET_ALL)
        if not raw:
            return None
        return raw
    except KeyboardInterrupt:
        print((Fore.RED if COLORAMA_AVAILABLE else '') + "\n\n❌ Operation cancelled by user")
        sys.exit(0)

def show_exit_message():
    """Show attractive exit message"""
    print("\n")
    print((Fore.MAGENTA if COLORAMA_AVAILABLE else '') + "╔══════════════════════════════════════════════════════════╗")
    print((Fore.MAGENTA if COLORAMA_AVAILABLE else '') + "║                                                          ║")
    print((Fore.MAGENTA if COLORAMA_AVAILABLE else '') + "║               🖤 𝗔𝗡𝗚𝗜𝗡𝗔™ 🖤                            ║")
    print((Fore.MAGENTA if COLORAMA_AVAILABLE else '') + "║         Thank you for using our tool!                   ║")
    print((Fore.MAGENTA if COLORAMA_AVAILABLE else '') + "║                                                          ║")
    print((Fore.MAGENTA if COLORAMA_AVAILABLE else '') + "╚══════════════════════════════════════════════════════════╝")
    print("\n")

def ask_for_repeat():
    """Ask user if they want to run another search"""
    print("\n")
    print((Fore.LIGHTBLUE_EX if COLORAMA_AVAILABLE else '') + "What would you like to do next?")
    print((Fore.YELLOW if COLORAMA_AVAILABLE else '') + "1. 🔍 Search another portal")
    print((Fore.YELLOW if COLORAMA_AVAILABLE else '') + "2. 🚪 Exit")
    
    try:
        # Set text color for input to ensure visibility
        if COLORAMA_AVAILABLE:
            sys.stdout.write(Fore.WHITE + Style.BRIGHT)
        choice = input("👉 Select option (1-2): ").strip()
        if COLORAMA_AVAILABLE:
            sys.stdout.write(Style.RESET_ALL)
        return choice == "1"
    except KeyboardInterrupt:
        return False

def show_summary():
    """Show summary of files created during session"""
    if session_stats["files_created"]:
        print("\n" + "═"*60)
        print((Fore.CYAN if COLORAMA_AVAILABLE else '') + "📊 SESSION SUMMARY")
        print("═"*60)
        
        # Calculate session duration
        duration = datetime.now(timezone.utc) - session_stats["start_time"]
        hours, remainder = divmod(duration.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)
        
        print((Fore.CYAN if COLORAMA_AVAILABLE else '') + 
              f"⏱️  Session duration: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}")
        print((Fore.CYAN if COLORAMA_AVAILABLE else '') + 
              f"🔍 Scans completed: {session_stats['scans_completed']}")
        print((Fore.CYAN if COLORAMA_AVAILABLE else '') + 
              f"🌐 Portals found: {session_stats['portals_found']}")
        print((Fore.CYAN if COLORAMA_AVAILABLE else '') + 
              f"📁 Files created: {len(session_stats['files_created'])}")
        
        for file in session_stats["files_created"]:
            print((Fore.WHITE if COLORAMA_AVAILABLE else '') + f"   • {file}")
        print("═"*60)

def export_session_report():
    """Export a comprehensive session report"""
    if not session_stats["files_created"]:
        return
    
    # Ensure output folder exists
    save_dir = ensure_output_folder()
    
    report_name = f"angina_session_report_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.json"
    report_path = os.path.join(save_dir, report_name)
    
    report_data = {
        "tool": "Angina Similar Portals Finder",
        "session_start": session_stats["start_time"].isoformat(),
        "session_end": datetime.now(timezone.utc).isoformat(),
        "scans_completed": session_stats["scans_completed"],
        "portals_found": session_stats["portals_found"],
        "files_created": session_stats["files_created"],
        "generated_at": datetime.now(timezone.utc).isoformat()
    }
    
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=2, ensure_ascii=False)
    
    print((Fore.YELLOW if COLORAMA_AVAILABLE else '') + f"📋 Session report exported to {report_path}")
    return report_path

def main():
    # Install missing packages at startup
    install_missing_packages()
    
    show_intro()
    
    while True:
        raw_url = get_user_input()
        if not raw_url:
            print((Fore.RED if COLORAMA_AVAILABLE else '') + "❌ Please enter a valid URL")
            continue
            
        url = normalize_url(raw_url)
        ip = extract_ip(url)

        if not ip:
            print((Fore.RED if COLORAMA_AVAILABLE else '') + "❌ Could not resolve IP for this URL")
            time.sleep(2)
            show_intro()
            continue
        
        # Check online status
        print((Fore.YELLOW if COLORAMA_AVAILABLE else '') + "⏳ Checking if the portal is online...")
        is_online, online_status, status_color, status_details = check_online_status(url)
        
        # Show scanning message
        clear_screen()
        animated_banner()
        print((Fore.CYAN if COLORAMA_AVAILABLE else '') + f"🌐 Scanning: {url}")
        print((Fore.CYAN if COLORAMA_AVAILABLE else '') + f"🔢 Resolved IP: {ip}")
        
        country, flag = get_ip_info(ip)
        print((Fore.CYAN if COLORAMA_AVAILABLE else '') + f"🌍 Location: {country} {flag}")
        print(status_color + f"📶 Status: {online_status}")
        
        # Display status details immediately
        if status_details:
            if 'status_code' in status_details:
                print((Fore.CYAN if COLORAMA_AVAILABLE else '') + f"Status Code: {status_details['status_code']}")
            if 'status_category' in status_details:
                print((Fore.CYAN if COLORAMA_AVAILABLE else '') + f"Status Category: {status_details['status_category']}")
            if 'response_time' in status_details:
                print((Fore.CYAN if COLORAMA_AVAILABLE else '') + f"Response Time: {status_details['response_time']}ms")
            if 'ssl_valid' in status_details:
                print((Fore.CYAN if COLORAMA_AVAILABLE else '') + f"SSL Valid: {status_details['ssl_valid']}")
        
        print((Fore.YELLOW if COLORAMA_AVAILABLE else '') + "⏳ Please wait while we scan the URL...")
        
        uuid = scan_url(url)
        if not uuid:
            time.sleep(2)
            show_intro()
            continue

        result = get_scan_result(uuid)
        if not result:
            print((Fore.RED if COLORAMA_AVAILABLE else '') + "❌ Failed to retrieve scan result.")
            time.sleep(2)
            show_intro()
            continue

        results = search_by_ip(ip)
        
        # Update session stats
        session_stats["scans_completed"] += 1
        session_stats["portals_found"] += len(results)
        
        # Display results
        clear_screen()
        animated_banner()
        display_results(url, ip, country, flag, results, online_status, status_color, status_details)
        file_path = save_results(url, ip, country, flag, results, online_status, status_details)
        session_stats["files_created"].append(file_path)

        # Ask if user wants to continue
        if not ask_for_repeat():
            break
            
        show_intro()

    # Show session summary before exiting
    clear_screen()
    animated_banner()
    show_summary()
    
    # Export session report
    if session_stats["scans_completed"] > 0:
        export_session_report()
    
    show_exit_message()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print((Fore.RED if COLORAMA_AVAILABLE else '') + "\n\n❌ Operation cancelled by user")
        show_exit_message()
    except Exception as e:
        print((Fore.RED if COLORAMA_AVAILABLE else '') + f"\n\n❌ An unexpected error occurred: {e}")
        show_exit_message()