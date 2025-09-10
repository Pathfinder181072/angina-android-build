import os
import sys
import time
import socket
import random
import json
import csv
import logging
import argparse
import threading
from datetime import datetime
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from colorama import Fore, init, Style
import pycountry
import ssl
import urllib3

# Initialize colorama and disable warnings
init(autoreset=True)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Get script name for folder creation
SCRIPT_NAME = os.path.splitext(os.path.basename(__file__))[0]
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), SCRIPT_NAME)

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Set up logging to file in the output directory
log_file = os.path.join(OUTPUT_DIR, f"{SCRIPT_NAME}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)

# Common ports for IPTV and web services
COMMON_PORTS = [80, 443, 8080, 8880, 25461, 2052, 2082, 2086, 2095, 8443, 8888, 9000]

# Common MAC prefixes for IPTV devices
MAC_PREFIXES = [
    "00:1A:79", "00:1B:79", "00:A1:79", "10:27:BE", "D4:CF:F9", "33:44:CF", "A0:BB:3E", "55:93:EA", "04:D6:AA",
    "00:0C:29", "00:50:56", "00:05:69", "00:1C:14", "08:00:27", "00:03:FF", "00:25:90", "00:26:75", "00:E0:4C",
    "00:90:0B", "00:05:9A", "00:1C:42", "00:16:3E", "00:14:22", "00:30:18", "00:21:5C", "00:0F:4B", "00:24:D4",
    "00:11:D8", "00:19:66", "00:1F:16", "00:20:91", "00:40:96", "00:60:2F", "00:0A:27"
]

# User agents for rotation
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3"
]

# Common subdomains for enumeration
COMMON_SUBDOMAINS = [
    "www", "api", "portal", "stream", "tv", "iptv", "live", "m", "mobile", 
    "secure", "admin", "login", "panel", "cdn", "video", "play"
]

# ====================== Banner Function ======================
def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""
{Fore.MAGENTA}╔══════════════════════════════════════════════════════════════════════════════╗
{Fore.MAGENTA}║{Fore.CYAN}                      🕵️‍♂️ PORTAL DETECTIVE PRO {Fore.YELLOW}v4.0{Fore.CYAN}                      {Fore.MAGENTA}║
{Fore.MAGENTA}║{Fore.LIGHTWHITE_EX}                 Advanced Portal Analysis Toolkit                 {Fore.MAGENTA}║
{Fore.MAGENTA}║{Fore.LIGHTRED_EX}                         🖤 𝗔𝗡𝗚𝗜𝗡𝗔™ 🖤                          {Fore.MAGENTA}║
{Fore.MAGENTA}╚══════════════════════════════════════════════════════════════════════════════╝
{Fore.CYAN}📁 Output Directory: {OUTPUT_DIR}
{Fore.YELLOW}⚠️  Warning: This tool is for educational purposes only. Use responsibly!
"""
    print(banner)
    for line in banner.split('\n'):
        time.sleep(0.01)

# ====================== Clear Screen ======================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ====================== Country to Flag ======================
def country_to_flag(country_name):
    special_cases = {'The Netherlands': 'Netherlands', 'USA': 'United States'}
    country_name = special_cases.get(country_name, country_name)
    try:
        country = pycountry.countries.get(name=country_name)
        if not country:
            return ""
        code = country.alpha_2.upper()
        return chr(127397 + ord(code[0])) + chr(127397 + ord(code[1]))
    except:
        return ""

# ====================== SSL Certificate Check ======================
def check_ssl(url):
    try:
        parsed = urlparse(url)
        hostname = parsed.hostname
        port = parsed.port or 443
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.settimeout(5)
            s.connect((hostname, port))
        return True
    except Exception as e:
        logging.error(f"SSL check failed for {url}: {e}")
        return False

# ====================== Portal Status Check ======================
def portal_status(url, proxy=None):
    try:
        start_time = time.time()
        headers = {'User-Agent': random.choice(USER_AGENTS)}
        proxies = {"http": proxy, "https": proxy} if proxy else None
        resp = requests.head(url, headers=headers, timeout=10, allow_redirects=True, 
                            verify=False, proxies=proxies)
        end_time = time.time()
        response_time = round((end_time - start_time) * 1000, 2)
        
        if resp.status_code < 200:
            status_category = "Informational (<200)"
            status_icon = "ℹ️"
        elif resp.status_code < 300:
            status_category = "Success (<300)"
            status_icon = "✅"
        elif resp.status_code < 400:
            status_category = "Redirection (<400)"
            status_icon = "↪️"
        elif resp.status_code < 500:
            status_category = "Client Error (<500)"
            status_icon = "❌"
        else:
            status_category = "Server Error (>=500)"
            status_icon = "🔥"
            
        if resp.status_code < 400:
            return "🟢 Up", resp.status_code, status_category, response_time, status_icon
        else:
            return "🔴 Down", resp.status_code, status_category, response_time, status_icon
    except Exception as e:
        logging.error(f"Portal status check failed for {url}: {e}")
        return "🔴 Down", "N/A", "No response", "N/A", "💀"

# ====================== Get IP Information (ipinfo.io) ======================
def get_ip_info(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=10)
        if response.status_code == 200:
            data = response.json()
            return {
                "IP": data.get("ip", "Unknown"),
                "Hostname": data.get("hostname", "Unknown"),
                "City": data.get("city", "Unknown"),
                "Region": data.get("region", "Unknown"),
                "Country": f"{country_to_flag(data.get('country', ''))} {data.get('country', 'Unknown')}",
                "Org": data.get("org", "Unknown"),
                "Postal": data.get("postal", "Unknown"),
                "Timezone": data.get("timezone", "Unknown"),
                "ASN": data.get("org", "Unknown").split()[0] if data.get("org") else "Unknown"
            }
        else:
            return {"Error": "Failed to fetch IP information"}
    except Exception as e:
        logging.error(f"IP info lookup failed for {ip}: {e}")
        return {"Error": str(e)}

# ====================== Reverse DNS Lookup ======================
def reverse_dns_lookup(ip):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        return hostname
    except:
        return "Not available"

# ====================== Subdomain Enumeration ======================
def enumerate_subdomains(domain, subdomains_list=COMMON_SUBDOMAINS, max_workers=20):
    found_subdomains = []
    def check_subdomain(subdomain):
        try:
            full_domain = f"{subdomain}.{domain}"
            ip = socket.gethostbyname(full_domain)
            return full_domain, ip
        except:
            return None

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(check_subdomain, subdomain): subdomain for subdomain in subdomains_list}
        for future in as_completed(futures):
            result = future.result()
            if result:
                found_subdomains.append(result)
    
    return found_subdomains

# ====================== HTTP Header Analysis ======================
def analyze_headers(url, proxy=None):
    try:
        headers = {'User-Agent': random.choice(USER_AGENTS)}
        proxies = {"http": proxy, "https": proxy} if proxy else None
        resp = requests.get(url, headers=headers, timeout=10, verify=False, proxies=proxies)
        
        security_headers = {
            'Strict-Transport-Security': 'HSTS',
            'Content-Security-Policy': 'CSP',
            'X-Frame-Options': 'X-Frame-Options',
            'X-Content-Type-Options': 'X-Content-Type-Options',
            'X-XSS-Protection': 'X-XSS-Protection',
            'Referrer-Policy': 'Referrer-Policy'
        }
        
        detected_headers = {}
        for header, value in resp.headers.items():
            if header in security_headers:
                detected_headers[security_headers[header]] = value
        
        return {
            "Server": resp.headers.get('Server', 'Unknown'),
            "X-Powered-By": resp.headers.get('X-Powered-By', 'Unknown'),
            "Security Headers": detected_headers,
            "All Headers": dict(resp.headers)
        }
    except Exception as e:
        logging.error(f"Header analysis failed for {url}: {e}")
        return {"Error": str(e)}

# ====================== Protection Detection ======================
def detect_protection(url, proxy=None):
    protections = {
        'Cloudflare': ['cf-ray', 'cloudflare', '__cfduid', '__cf_bm'],
        'DDoS-Guard': ['ddos-guard'],
        'Sucuri': ['sucuri'],
        'Akamai': ['akamai', 'akamaiedge'],
        'Incapsula': ['incapsula', 'visid_incap'],
        'Nginx': ['nginx'],
        'Apache': ['apache'],
        'LiteSpeed': ['litespeed'],
        'IIS': ['microsoft-iis', 'iis'],
        'OpenResty': ['openresty']
    }
    detected = []
    try:
        headers = {'User-Agent': random.choice(USER_AGENTS)}
        proxies = {"http": proxy, "https": proxy} if proxy else None
        resp = requests.get(url, headers=headers, timeout=10, verify=False, proxies=proxies)
        headers_lower = {k.lower(): v.lower() for k, v in resp.headers.items()}
        cookies_lower = [c.lower() for c in resp.cookies.keys()] if resp.cookies else []
        for prot, signs in protections.items():
            for sign in signs:
                if (any(sign in h for h in headers_lower.values()) or 
                    sign in str(cookies_lower) or 
                    sign in resp.text.lower()):
                    detected.append(prot)
                    break
        return list(set(detected))
    except Exception as e:
        logging.error(f"Protection detection failed for {url}: {e}")
        return []

# ====================== Generate Random MAC ======================
def generate_mac(prefix):
    return prefix + ":" + ":".join(["%02X" % random.randint(0, 255) for _ in range(3)])

# ====================== Test MAC Login ======================
def test_mac_login(url, mac, proxy=None):
    headers = {
        "User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3",
        "X-User-Agent": "Model: MAG254; Link: WiFi",
        "Authorization": f"MAC {mac}"
    }
    try:
        proxies = {"http": proxy, "https": proxy} if proxy else None
        if not url.endswith("/c/") and not url.endswith("/stalker_portal/server/load.php"):
            url = url.rstrip("/") + "/c/"
        resp = requests.get(url, headers=headers, timeout=8, verify=False, proxies=proxies)
        if "not authorized" in resp.text.lower():
            return "❌ Denied"
        elif "ok" in resp.text.lower():
            return "✅ OK"
        elif "blocked" in resp.text.lower():
            return "🚫 Blocked"
        else:
            return "❓ Unknown"
    except Exception as e:
        logging.error(f"MAC login test failed for {url} with MAC {mac}: {e}")
        return "💥 Error"

# ====================== Port Scanning (Multithreaded) ======================
def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                try:
                    s.send(b"HEAD / HTTP/1.0\r\n\r\n")
                    banner = s.recv(1024).decode('utf-8', errors='ignore').split('\n')[0]
                    return port, banner.strip()
                except:
                    return port, "Banner not available"
            return None
    except Exception as e:
        logging.error(f"Port scan failed for {host}:{port}: {e}")
        return None

def scan_ports(host, ports=COMMON_PORTS, max_workers=50):
    open_ports = {}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_port = {executor.submit(scan_port, host, port): port for port in ports}
        for future in as_completed(future_to_port):
            try:
                result = future.result()
                if result:
                    port, banner = result
                    open_ports[port] = banner
            except Exception as e:
                logging.error(f"Port scan thread error: {e}")
    return open_ports

# ====================== Save Results in Multiple Formats ======================
def save_summary(data, portal_name, format="txt"):
    safe_name = "".join(c for c in portal_name if c.isalnum() or c in ('-', '_')).rstrip()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(OUTPUT_DIR, f"Portal_Detective_{safe_name}_{timestamp}.{format}")
    
    try:
        if format == "json":
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        elif format == "csv":
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                for key, value in data.items():
                    if isinstance(value, dict):
                        for k, v in value.items():
                            writer.writerow([f"{key}_{k}", v])
                    else:
                        writer.writerow([key, value])
        else:  # txt
            with open(filename, 'w', encoding='utf-8') as f:
                for key, value in data.items():
                    if isinstance(value, dict):
                        f.write(f"\n{key}:\n")
                        for k, v in value.items():
                            f.write(f"  {k}: {v}\n")
                    else:
                        f.write(f"{key}: {value}\n")
        return filename
    except Exception as e:
        logging.error(f"Failed to save summary: {e}")
        return None

# ====================== Process URLs ======================
def process_urls(url_list, output_format="txt", proxy=None, max_workers=20):
    for url in url_list:
        url = url.strip()
        if not url:
            continue
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url

        parsed = urlparse(url)
        hostname = parsed.hostname
        domain = ".".join(hostname.split('.')[-2:]) if hostname.count('.') >= 2 else hostname

        print(f"\n{Fore.YELLOW}🔍 {Style.BRIGHT}Analyzing: {Fore.CYAN}{url}")
        print(f"{Fore.YELLOW}⏳ {Style.BRIGHT}This may take a few moments...")

        try:
            ip = socket.gethostbyname(hostname)
            ip_info = get_ip_info(ip)
            reverse_dns = reverse_dns_lookup(ip)
        except Exception as e:
            print(Fore.RED + f"❌ Unable to resolve IP for {url}: {e}")
            continue

        # Perform scans in parallel
        with ThreadPoolExecutor(max_workers=3) as executor:
            status_future = executor.submit(portal_status, url, proxy)
            ssl_future = executor.submit(check_ssl, url)
            ports_future = executor.submit(scan_ports, hostname)
            headers_future = executor.submit(analyze_headers, url, proxy)
            protections_future = executor.submit(detect_protection, url, proxy)
            subdomains_future = executor.submit(enumerate_subdomains, domain)

            status, status_code, status_category, response_time, status_icon = status_future.result()
            ssl_valid = ssl_future.result()
            open_ports = ports_future.result()
            headers_info = headers_future.result()
            protections_detected = protections_future.result()
            found_subdomains = subdomains_future.result()

        # Display results
        print(f"\n{Fore.GREEN}✅ {Style.BRIGHT}Analysis Complete!")
        print(f"{Fore.YELLOW}📊 {Style.BRIGHT}Portal Status: {status}")
        print(f"{Fore.MAGENTA}🌐 {Style.BRIGHT}IP Address: {ip}")
        print(f"{Fore.CYAN}🔁 {Style.BRIGHT}Reverse DNS: {reverse_dns}")
        
        if open_ports:
            print(f"{Fore.CYAN}🚪 {Style.BRIGHT}Open Ports:")
            for port, banner in open_ports.items():
                print(f"  {Fore.WHITE}Port {port}: {banner}")
        else:
            print(f"{Fore.CYAN}🚪 {Style.BRIGHT}Open Ports: None")
        
        print(f"{Fore.YELLOW}🔒 {Style.BRIGHT}SSL Valid: {'✅ Yes' if ssl_valid else '❌ No'}")
        print(f"{Fore.CYAN}📟 {Style.BRIGHT}Status Code: {status_icon} {status_code}")
        print(f"{Fore.CYAN}📋 {Style.BRIGHT}Status Category: {status_category}")
        print(f"{Fore.CYAN}⏱️  {Style.BRIGHT}Response Time: {response_time}ms")
        
        for key, val in ip_info.items():
            icon = "🏴" if key == "Country" else "📍" if key == "Region" else "🏙️" if key == "City" else "📮" if key == "Postal" else "🕐" if key == "Timezone" else "🏢" if key == "Org" else "🔢"
            print(f"{icon} {Style.BRIGHT}{key}: {Fore.WHITE}{val}")
        
        if found_subdomains:
            print(f"{Fore.CYAN}🌐 {Style.BRIGHT}Found Subdomains:")
            for subdomain, sub_ip in found_subdomains:
                print(f"  {Fore.WHITE}{subdomain} → {sub_ip}")
        
        if protections_detected:
            print(f"{Fore.LIGHTGREEN_EX}🛡️  {Style.BRIGHT}Protections Detected:")
            for p in protections_detected:
                shield_icon = "☁️" if "Cloud" in p else "🛡️" if "Guard" in p else "🔒" if "Sucuri" in p else "🔄" if "Akamai" in p else "⚔️" if "Incapsula" in p else "🐘" if "Nginx" in p else "🌵" if "Apache" in p else "⚡" if "LiteSpeed" in p else "🪟" if "IIS" in p else "🔧"
                print(f"  {shield_icon} {p}")
        else:
            print(f"{Fore.RED}🛡️  {Style.BRIGHT}No protection detected.")

        if 'Error' not in headers_info:
            print(f"{Fore.CYAN}📋 {Style.BRIGHT}Server: {headers_info.get('Server', 'Unknown')}")
            print(f"{Fore.CYAN}⚡ {Style.BRIGHT}X-Powered-By: {headers_info.get('X-Powered-By', 'Unknown')}")
            if headers_info.get('Security Headers'):
                print(f"{Fore.CYAN}🛡️  {Style.BRIGHT}Security Headers:")
                for header, value in headers_info['Security Headers'].items():
                    print(f"  {Fore.WHITE}{header}: {value}")

        # Prepare data for saving
        log_data = {
            "Portal": url,
            "Status": status,
            "IP Address": ip,
            "Reverse DNS": reverse_dns,
            "Open Ports": open_ports,
            "SSL Valid": "Yes" if ssl_valid else "No",
            "Status Code": status_code,
            "Status Category": status_category,
            "Response Time (ms)": response_time,
            **ip_info,
            "Subdomains Found": found_subdomains,
            "Protections Detected": protections_detected,
            "HTTP Headers": headers_info,
            "MAC Login Tests": {}
        }

        print(f"\n{Fore.CYAN}🔌 {Style.BRIGHT}Testing MAC login with common prefixes...")
        mac_results = {}
        for prefix in MAC_PREFIXES:
            mac = generate_mac(prefix)
            result = test_mac_login(url, mac, proxy)
            print(f"  📍 MAC {mac} -> {result}")
            mac_results[mac] = result
            time.sleep(0.1)  # Avoid rate limiting
        
        log_data["MAC Login Tests"] = mac_results

        # Save in all formats
        for fmt in ["txt", "json", "csv"]:
            filename = save_summary(log_data, hostname, fmt)
            if filename:
                print(f"{Fore.GREEN}💾 {Style.BRIGHT}{fmt.upper()} report saved: {os.path.basename(filename)}")

# ====================== Input Parser ======================
def parse_input(raw_input):
    for sep in [',', ';', '|', '\n']:
        raw_input = raw_input.replace(sep, ',')
    return [u.strip() for u in raw_input.split(',') if u.strip()]

# ====================== Main Function ======================
def main():
    while True:
        parser = argparse.ArgumentParser(description="Portal Detective Pro - Advanced Portal Analysis Tool")
        parser.add_argument("-u", "--url", help="Single URL to scan")
        parser.add_argument("-f", "--file", help="File containing URLs (one per line)")
        parser.add_argument("-p", "--proxy", help="Proxy server (e.g., http://proxy:port)")
        parser.add_argument("-o", "--output", choices=["txt", "json", "csv", "all"], default="all", 
                           help="Output format (default: all)")
        parser.add_argument("-w", "--workers", type=int, default=20, help="Number of workers (default: 20)")
        
        args = parser.parse_args()
        
        clear_screen()
        print_banner()
        
        url_list = []
        if args.url:
            url_list.append(args.url)
        elif args.file:
            try:
                with open(args.file, 'r') as f:
                    url_list = [line.strip() for line in f if line.strip()]
            except FileNotFoundError:
                print(Fore.RED + f"❌ File not found: {args.file}")
                sys.exit(1)
        else:
            print(f"{Fore.LIGHTYELLOW_EX}⚠️  {Style.BRIGHT}Enter portal URL(s), then hit DOUBLE ENTER to start: ")
            raw_input_lines = []
            while True:
                line = input()
                if not line.strip():
                    break
                raw_input_lines.append(line)
            urls_input = "\n".join(raw_input_lines)
            url_list = parse_input(urls_input)
        
        if not url_list:
            print(Fore.RED + "❌ No valid URLs provided. Exiting.")
            sys.exit(1)
        
        output_format = "all" if args.output == "all" else args.output
        process_urls(url_list, output_format, args.proxy, args.workers)
        
        print(f"\n{Fore.GREEN}🎉 {Style.BRIGHT}All scans completed! Results saved in: {OUTPUT_DIR}")
        print(f"{Fore.CYAN}📋 {Style.BRIGHT}Log file: {os.path.basename(log_file)}")
        
        # Ask user if they want to repeat or exit
        print(f"\n{Fore.YELLOW}🔄 {Style.BRIGHT}What would you like to do next?")
        print(f"{Fore.CYAN}1. {Style.BRIGHT}Run another scan")
        print(f"{Fore.CYAN}2. {Style.BRIGHT}Exit")
        
        while True:
            choice = input(f"{Fore.YELLOW}➡️  {Style.BRIGHT}Enter your choice (1 or 2): ").strip()
            if choice == "1":
                break  # Break out of the inner loop to restart the main loop
            elif choice == "2":
                print(f"{Fore.GREEN}👋 {Style.BRIGHT}Thank you for using Portal Detective Pro! Goodbye!")
                return  # Exit the main function
            else:
                print(f"{Fore.RED}❌ {Style.BRIGHT}Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}❌ {Style.BRIGHT}Scan interrupted by user. Exiting.")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}❌ {Style.BRIGHT}Unexpected error: {e}")
        logging.exception("Unexpected error occurred")
        sys.exit(1)