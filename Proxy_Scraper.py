import requests
import concurrent.futures
import time
import os
import re
from datetime import datetime

class AdvancedProxyScraper:
    def __init__(self):
        self.proxies = []
        # Only the most reliable sources
        self.sources = [
            "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
            "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt", 
            "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTP_RAW.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
        ]
        self.working_proxies = []
        
        # Get the script's directory and name
        self.SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.SCRIPT_NAME = os.path.splitext(os.path.basename(__file__))[0]
        self.OUTPUT_FOLDER = os.path.join(self.SCRIPT_DIR, self.SCRIPT_NAME)
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def typewriter_effect(self, text, delay=0.03, color_code=""):
        """Display text with a typewriter effect"""
        reset = "\033[0m"
        for char in text:
            print(f"{color_code}{char}{reset}", end='', flush=True)
            time.sleep(delay)
        print()
    
    def print_colored_banner(self):
        """Print a colorful banner with typewriter effect"""
        self.clear_screen()
        
        # Color codes
        red = "\033[91m"
        purple = "\033[95m"
        blue = "\033[94m"
        cyan = "\033[96m"
        yellow = "\033[93m"
        green = "\033[92m"
        reset = "\033[0m"
        
        # Banner art
        banner_lines = [
            f"{red}╔══════════════════════════════════════════════════════════╗{reset}",
            f"{red}║{purple}    █████╗ ███╗   ██╗ ██████╗ ██╗███╗   ██╗ █████╗     {red}║{reset}",
            f"{red}║{purple}   ██╔══██╗████╗  ██║██╔════╝ ██║████╗  ██║██╔══██╗    {red}║{reset}",
            f"{red}║{purple}   ███████║██╔██╗ ██║██║  ███╗██║██╔██╗ ██║███████║    {red}║{reset}",
            f"{red}║{purple}   ██╔══██║██║╚██╗██║██║   ██║██║██║╚██╗██║██╔══██║    {red}║{reset}",
            f"{red}║{purple}   ██║  ██║██║ ╚████║╚██████╔╝██║██║ ╚████║██║  ██║    {red}║{reset}",
            f"{red}║{purple}   ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    {red}║{reset}",
            f"{red}║{cyan}      🖤 ADVANCED PROXY SCRAPER 🌍 FREE SOURCES ONLY {red}║{reset}",
            f"{red}╚══════════════════════════════════════════════════════════╝{reset}",
            ""
        ]
        
        for line in banner_lines:
            print(line)
            time.sleep(0.1)
        
        print(f"{yellow}📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{reset}")
        print(f"{cyan}{'=' * 60}{reset}")
        print()
    
    def ask_to_start(self):
        """Ask user to start the process"""
        cyan = "\033[96m"
        yellow = "\033[93m"
        reset = "\033[0m"
        
        print(f"{cyan}🚀 Ready to scrape proxies from {len(self.sources)} sources{reset}")
        print(f"{yellow}👉 Press Enter to start fetching...{reset}", end="")
        input()
        print()
    
    def ensure_output_folder(self):
        """Create the output folder if it doesn't exist"""
        if not os.path.exists(self.OUTPUT_FOLDER):
            os.makedirs(self.OUTPUT_FOLDER)
            green = "\033[92m"
            reset = "\033[0m"
            print(f"{green}📁 Created output folder: {self.OUTPUT_FOLDER}{reset}")
        return self.OUTPUT_FOLDER
    
    def animate_progress(self, current, total, prefix="", suffix="", length=30):
        """Display animated progress bar with colors"""
        percent = current / total
        filled_length = int(length * percent)
        
        # Color codes
        yellow = "\033[93m"
        orange = "\033[33m"
        green = "\033[92m"
        reset = "\033[0m"
        
        # Choose color based on progress
        if percent < 0.5:
            color = yellow
        elif percent < 0.8:
            color = orange
        else:
            color = green
            
        bar = color + '█' * filled_length + reset + '-' * (length - filled_length)
        percent_text = f"{percent*100:.1f}%"
        
        # Clear line and print progress
        print(f"\r{prefix} |{bar}| {percent_text} {suffix}", end="", flush=True)
        
        if current == total:
            print()
    
    def fetch_proxies(self):
        cyan = "\033[96m"
        reset = "\033[0m"
        
        print(f"{cyan}📡 Fetching proxies from reliable sources...{reset}")
        print(f"{cyan}Please wait, this may take a moment...{reset}\n")
        
        total_fetched = 0
        source_count = len(self.sources)
        
        for i, url in enumerate(self.sources, 1):
            try:
                self.animate_progress(i-1, source_count, "Fetching sources", f"Source {i}/{source_count}")
                
                response = requests.get(url, timeout=15)
                if response.status_code == 200:
                    # Extract proxies from response
                    raw_proxies = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}', response.text)
                    
                    if not raw_proxies:
                        continue
                    
                    # Determine proxy type from URL
                    if 'http' in url.lower() and 'socks' not in url.lower():
                        proxy_type = 'HTTP'
                    elif 'socks4' in url.lower():
                        proxy_type = 'SOCKS4'
                    elif 'socks5' in url.lower():
                        proxy_type = 'SOCKS5'
                    else:
                        proxy_type = 'HTTP'
                    
                    # Add to proxies list
                    for proxy in raw_proxies:
                        self.proxies.append({
                            'address': proxy,
                            'type': proxy_type,
                            'status': 'Pending'
                        })
                    
                    total_fetched += len(raw_proxies)
                
            except Exception as e:
                pass
        
        # Remove duplicates
        unique_proxies = []
        seen = set()
        for proxy in self.proxies:
            if proxy['address'] not in seen:
                seen.add(proxy['address'])
                unique_proxies.append(proxy)
        
        self.proxies = unique_proxies
        self.animate_progress(source_count, source_count, "Fetching sources", "Complete!")
        
        green = "\033[92m"
        reset = "\033[0m"
        print(f"\n{green}📊 Total unique proxies: {len(self.proxies)}{reset}")
        return len(self.proxies) > 0
    
    def test_proxy_simple(self, proxy):
        """Simple proxy test without location detection"""
        try:
            start_time = time.time()
            
            # Test with a simple request (shorter timeout)
            test_url = "http://httpbin.org/ip"
            proxies = {
                'http': f"{proxy['type'].lower()}://{proxy['address']}",
                'https': f"{proxy['type'].lower()}://{proxy['address']}"
            }
            
            response = requests.get(test_url, proxies=proxies, timeout=5)
            
            if response.status_code == 200:
                response_time = round((time.time() - start_time) * 1000, 2)
                return {
                    **proxy,
                    'response_time': response_time,
                    'status': 'Working'
                }
                
        except:
            pass
        
        return None
    
    def test_proxies(self):
        """Test all proxies with simple approach"""
        if not self.proxies:
            red = "\033[91m"
            reset = "\033[0m"
            print(f"{red}❌ No proxies to test!{reset}")
            return False
            
        cyan = "\033[96m"
        reset = "\033[0m"
        
        print(f"\n{cyan}🔍 Testing {len(self.proxies)} proxies...{reset}")
        print(f"{cyan}This will take some time. Please be patient.{reset}\n")
        
        working_proxies = []
        tested = 0
        
        # Test in smaller batches with progress updates
        batch_size = 50
        total_batches = (len(self.proxies) + batch_size - 1) // batch_size
        
        for i in range(0, len(self.proxies), batch_size):
            batch = self.proxies[i:i + batch_size]
            batch_num = (i // batch_size) + 1
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
                results = list(executor.map(self.test_proxy_simple, batch))
            
            # Count working proxies in this batch
            working_in_batch = [p for p in results if p is not None]
            working_proxies.extend(working_in_batch)
            tested += len(batch)
            
            # Show animated progress
            self.animate_progress(
                batch_num, 
                total_batches, 
                "Testing proxies", 
                f"Batch {batch_num}/{total_batches} | Working: {len(working_proxies)}"
            )
            
            # Small delay to avoid overwhelming
            time.sleep(0.1)
        
        self.working_proxies = working_proxies
        self.animate_progress(total_batches, total_batches, "Testing proxies", "Complete!")
        
        green = "\033[92m"
        reset = "\033[0m"
        print(f"\n{green}🎉 Found {len(self.working_proxies)} working proxies!{reset}")
        return len(self.working_proxies) > 0
    
    def save_proxies(self):
        """Save working proxies to files"""
        if not self.working_proxies:
            red = "\033[91m"
            reset = "\033[0m"
            print(f"{red}❌ No working proxies to save!{reset}")
            return
            
        cyan = "\033[96m"
        reset = "\033[0m"
        
        print(f"\n{cyan}💾 Saving proxies to files...{reset}")
        
        # Ensure output folder exists
        save_dir = self.ensure_output_folder()
        
        # Organize by type
        by_type = {}
        for proxy in self.working_proxies:
            if proxy['type'] not in by_type:
                by_type[proxy['type']] = []
            by_type[proxy['type']].append(proxy)
        
        # Save each type
        for proxy_type, proxies in by_type.items():
            filename = f"{proxy_type.lower()}_proxies.txt"
            filepath = os.path.join(save_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                for proxy in proxies:
                    f.write(f"{proxy['address']}\n")
            
            green = "\033[92m"
            print(f"{green}✅ Saved {len(proxies)} {proxy_type} proxies to {filepath}{reset}")
        
        # Save combined list
        all_proxies_path = os.path.join(save_dir, "all_proxies.txt")
        with open(all_proxies_path, 'w', encoding='utf-8') as f:
            for proxy in self.working_proxies:
                f.write(f"{proxy['address']}\n")
        
        print(f"{green}✅ Saved {len(self.working_proxies)} total proxies to {all_proxies_path}{reset}")
        
        # Save log file
        log_path = os.path.join(save_dir, "scraper_log.txt")
        with open(log_path, 'w', encoding='utf-8') as f:
            f.write(f"Proxy Scraper Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 50 + "\n")
            f.write(f"Total proxies found: {len(self.proxies)}\n")
            f.write(f"Working proxies: {len(self.working_proxies)}\n\n")
            
            for proxy_type, proxies in by_type.items():
                f.write(f"{proxy_type}: {len(proxies)} proxies\n")
            
            f.write("\nWorking Proxies:\n")
            f.write("=" * 50 + "\n")
            for proxy in self.working_proxies:
                f.write(f"{proxy['address']} ({proxy['type']}) - {proxy['response_time']}ms\n")
        
        print(f"{green}✅ Log saved to {log_path}{reset}")
    
    def show_results(self):
        """Display results in simple format"""
        if not self.working_proxies:
            red = "\033[91m"
            reset = "\033[0m"
            print(f"{red}❌ No working proxies found!{reset}")
            return
            
        cyan = "\033[96m"
        green = "\033[92m"
        yellow = "\033[93m"
        reset = "\033[0m"
        
        print(f"\n{cyan}{'=' * 60}{reset}")
        print(f"{green}🎯 WORKING PROXIES FOUND{reset}")
        print(f"{cyan}{'=' * 60}{reset}")
        
        # Count by type
        type_count = {}
        for proxy in self.working_proxies:
            if proxy['type'] in type_count:
                type_count[proxy['type']] += 1
            else:
                type_count[proxy['type']] = 1
        
        for proxy_type, count in type_count.items():
            print(f"{yellow}{proxy_type}: {count} proxies{reset}")
        
        # Show some fastest proxies
        print(f"\n{yellow}⚡ Fastest proxies:{reset}")
        fastest = sorted(self.working_proxies, key=lambda x: x['response_time'])[:5]
        for proxy in fastest:
            print(f"  {green}{proxy['address']} ({proxy['type']}) - {proxy['response_time']}ms{reset}")
        
        print(f"{cyan}{'=' * 60}{reset}")

def main():
    """Main function"""
    red = "\033[91m"
    purple = "\033[95m"
    cyan = "\033[96m"
    green = "\033[92m"
    reset = "\033[0m"
    
    while True:
        scraper = AdvancedProxyScraper()
        scraper.print_colored_banner()
        
        # Show output folder info
        save_dir = scraper.ensure_output_folder()
        print(f"{cyan}📁 Output folder: {save_dir}{reset}\n")
        
        scraper.ask_to_start()
        
        # Fetch proxies
        if not scraper.fetch_proxies():
            print(f"\n{red}❌ Could not fetch any proxies. Please check your internet connection.{reset}")
            break
        
        # Test proxies
        if not scraper.test_proxies():
            yellow = "\033[93m"
            print(f"\n{yellow}❌ No working proxies found. This is normal - free proxies often have low reliability.{reset}")
        
        # Show results
        scraper.show_results()
        
        # Save results
        if scraper.working_proxies:
            scraper.save_proxies()
        
        print(f"\n{green}✅ Process completed successfully!{reset}")
        print(f"\n{cyan}Options:{reset}")
        print(f"{green}1. Run again{reset}")
        print(f"{red}2. Exit{reset}")
        
        while True:
            choice = input(f"\n{cyan}Enter choice (1 or 2): {reset}").strip()
            if choice == "1":
                break
            elif choice == "2":
                print(f"\n{purple}👋 Goodbye! Thank you for using ANGINA ADVANCED PROXY SCRAPER!{reset}")
                return
            else:
                print(f"{red}❌ Invalid choice. Please enter 1 or 2.{reset}")

if __name__ == "__main__":
    main()