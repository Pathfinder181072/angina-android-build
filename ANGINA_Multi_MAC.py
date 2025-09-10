import os
import sys
import random
import time
from tqdm import tqdm
import colorama
from colorama import Fore, Back, Style

# Check and install required packages
try:
    from tqdm import tqdm
except ImportError:
    print("Installing required package: tqdm")
    os.system(f"{sys.executable} -m pip install tqdm")
    from tqdm import tqdm

try:
    import colorama
    from colorama import Fore, Back, Style
except ImportError:
    print("Installing required package: colorama")
    os.system(f"{sys.executable} -m pip install colorama")
    import colorama
    from colorama import Fore, Back, Style

# Initialize colorama
colorama.init(autoreset=True)

# Get the script's directory and name
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_NAME = os.path.splitext(os.path.basename(__file__))[0]
OUTPUT_FOLDER = os.path.join(SCRIPT_DIR, SCRIPT_NAME)

# Prefix list
PREFIXES = [
    # Most common IPTV STBs
    "00:1A:79:",  # Infomir MAG
    "00:1B:79:",  # Infomir MAG
    "00:A1:79:",  # Infomir MAG
    "10:27:BE:",  # Infomir MAG
    "D4:CF:F9:",  # Infomir MAG
    "33:44:CF:",  # Infomir MAG
    "A0:BB:3E:",  # Infomir MAG
    "55:93:EA:",  # Infomir MAG
    "04:D6:AA:",  # Infomir MAG

    # Virtual Machines / Emulators (commonly spoofed)
    "00:0C:29:",  # VMware
    "00:50:56:",  # VMware
    "00:05:69:",  # VMware
    "00:1C:14:",  # VirtualBox
    "08:00:27:",  # VirtualBox
    "00:03:FF:",  # Microsoft Hyper-V

    # Generic manufacturers often used in IPTV
    "00:25:90:",  # Samsung
    "00:26:75:",  # Samsung
    "00:E0:4C:",  # Realtek
    "00:90:0B:",  # Realtek
    "00:05:9A:",  # Realtek
    "00:1C:42:",  # Parallels
    "00:16:3E:",  # Xen
    "00:14:22:",  # Dell
    "00:30:18:",  # Cisco
    "00:21:5C:",  # Cisco
    "00:0F:4B:",  # Huawei
    "00:24:D4:",  # Huawei
    "00:11:D8:",  # Motorola
    "00:19:66:",  # Motorola
    "00:1F:16:",  # LG
    "00:20:91:",  # LG
    "00:40:96:",  # Toshiba
    "00:60:2F:",  # Sun Microsystems
    "00:0A:27:",  # VirtualBox (alt)
    
    # OTHER MACs given from myiptvforum.com 
    "00:1C:79:",  #@Helvetier
    "00:2A:01:",  #@Helvetier
    "00:2A:79:",  #@Helvetier
    "00:1E:B8:",  #@PicKim
]

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    """Display the program banner with Egyptian flag"""
    clear_screen()
    # Egyptian flag with 8 lines total: 2 red, 4 white (with yellow eagle), 2 black
    print(Fore.RED + "    ██████████████████████████████████████████████")
    print(Fore.RED + "    ██████████████████████████████████████████████")
    print(Fore.WHITE + "    ██████████████████████████████████████████████")
    print(Fore.WHITE + "    █████████████" + Fore.YELLOW + "████" + Fore.WHITE + "██████████████████████")
    print(Fore.WHITE + "    █████████████" + Fore.YELLOW + "████" + Fore.WHITE + "██████████████████████")
    print(Fore.WHITE + "    ██████████████████████████████████████████████")
    print(Fore.BLACK + "    ██████████████████████████████████████████████")
    print(Fore.BLACK + "    ██████████████████████████████████████████████")
    print()
    print(Fore.MAGENTA + "       🖤ANGINA🖤 MULTI GENERATOR X")
    print(Fore.CYAN + "     MAC Address Combination Generator")
    print(Fore.MAGENTA + "   " + "=" * 45)
    print()

def generate_mac_suffixes(count, mode="random"):
    """Generate MAC address suffixes based on the selected mode - OPTIMIZED"""
    chars = "0123456789ABCDEF"
    
    if mode == "random":
        # Generate random suffixes without creating all combinations first
        # Using set for uniqueness with efficient generation
        suffixes = set()
        while len(suffixes) < count:
            # Generate 6 random hex characters more efficiently
            suffix = ''.join(random.choices(chars, k=6))
            suffixes.add(suffix)
            # Early exit if we've reached the maximum possible unique values
            if len(suffixes) >= 16777216:  # 16^6 maximum unique values
                break
        return list(suffixes)[:count]
    
    elif mode == "ascending":
        # Generate in ascending order - optimized with generator
        max_val = min(count, 16**6)
        for i in range(max_val):
            yield format(i, '06X')
    
    elif mode == "descending":
        # Generate in descending order - optimized with generator
        max_val = min(count, 16**6)
        for i in range(max_val):
            yield format(16**6 - 1 - i, '06X')
    
    return []

def format_mac_suffix(suffix_str):
    """Format a suffix string into MAC format (XX:XX:XX)"""
    return f"{suffix_str[0:2]}:{suffix_str[2:4]}:{suffix_str[4:6]}"

def format_number(n):
    """Format large numbers with K, M, etc."""
    if n >= 1000000:
        return f"{n/1000000:.1f}M"
    elif n >= 1000:
        return f"{n/1000:.1f}K"
    else:
        return str(n)

def get_unique_filename(directory, base_name):
    """Get a unique filename by appending numbers if needed"""
    name, ext = os.path.splitext(base_name)
    counter = 1
    new_name = base_name
    
    while os.path.exists(os.path.join(directory, new_name)):
        new_name = f"{name}-{counter}{ext}"
        counter += 1
    
    return new_name

def show_loading_bar(prefix, current, total, bar_length=40):
    """Show a custom loading bar with percentage"""
    percent = float(current) * 100 / total
    arrow = '█' * int(percent/100 * bar_length)
    spaces = ' ' * (bar_length - len(arrow))
    
    # Use different colors for the bar
    if percent < 30:
        color = Fore.RED
    elif percent < 70:
        color = Fore.YELLOW
    else:
        color = Fore.GREEN
        
    sys.stdout.write(f"\r{Fore.CYAN}{prefix}: {color}[{arrow}{spaces}] {percent:.1f}%")
    sys.stdout.flush()

def ask_angina_question():
    """Ask the user if they want to repeat or exit"""
    print(f"\n{Fore.MAGENTA}╔══════════════════════════════════════════════════════════════╗")
    print(f"{Fore.MAGENTA}║{Fore.WHITE}                      🖤ANGINA🖤                       {Fore.MAGENTA}║")
    print(f"{Fore.MAGENTA}║{Fore.CYAN}             What would you like to do?                {Fore.MAGENTA}║")
    print(f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════════════╝")
    print(f"{Fore.GREEN}1. {Fore.YELLOW}Generate more MAC addresses")
    print(f"{Fore.RED}2. {Fore.YELLOW}Exit")
    
    while True:
        try:
            choice = input(f"\n{Fore.CYAN}📋 Enter your choice (1-2): {Style.RESET_ALL}")
            if choice in ['1', '2']:
                return choice
            else:
                print(f"{Fore.RED}❌ Please enter 1 or 2.")
        except (ValueError, KeyboardInterrupt):
            print(f"{Fore.RED}❌ Invalid input. Please try again.")

def display_prefixes_in_rows():
    """Display prefixes in rows with proper formatting"""
    print(f"{Fore.CYAN}📋 Available MAC prefixes:")
    print()
    
    # Display prefixes in 3 columns
    for i in range(0, len(PREFIXES), 3):
        row = PREFIXES[i:i+3]
        for j, prefix in enumerate(row):
            idx = i + j + 1
            color = Fore.YELLOW if idx % 2 == 0 else Fore.GREEN
            print(f"{color}{idx:2d}. {prefix.ljust(12)}", end="")
        print()

def ensure_output_folder():
    """Create the output folder if it doesn't exist"""
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        print(f"{Fore.GREEN}📁 Created output folder: {OUTPUT_FOLDER}")
    return OUTPUT_FOLDER

def main():
    while True:
        show_banner()
        
        # Ensure output folder exists
        save_dir = ensure_output_folder()
        
        # Show prefix list in rows
        display_prefixes_in_rows()
        
        # Get user selection
        while True:
            try:
                selected = input(f"\n{Fore.CYAN}🔢 Select prefixes by numbers (comma-separated, or 'all' for all): {Style.RESET_ALL}").strip()
                if selected.lower() == 'all':
                    selected_indices = list(range(len(PREFIXES)))
                    break
                else:
                    selected_indices = [int(x.strip())-1 for x in selected.split(",")]
                    if all(0 <= i < len(PREFIXES) for i in selected_indices):
                        break
                    else:
                        print(f"{Fore.RED}❌ Some numbers are out of range. Please try again.")
            except ValueError:
                print(f"{Fore.RED}❌ Invalid input. Please enter numbers separated by commas.")
        
        # Clear screen after selecting prefixes
        clear_screen()
        show_banner()
        
        # Get count - unlimited now
        while True:
            try:
                count = int(input(f"\n{Fore.CYAN}🔢 How many MAC addresses to generate per prefix? {Style.RESET_ALL}"))
                if count > 0:
                    break
                else:
                    print(f"{Fore.RED}❌ Please enter a positive number.")
            except ValueError:
                print(f"{Fore.RED}❌ Please enter a valid number.")
        
        # Get generation mode
        modes = ["random", "ascending", "descending"]
        print(f"\n{Fore.CYAN}📊 Generation modes:")
        for i, mode in enumerate(modes, 1):
            color = Fore.YELLOW if i == 1 else Fore.GREEN if i == 2 else Fore.MAGENTA
            print(f"{color}{i}. {mode.capitalize()}")
        
        while True:
            try:
                mode_choice = int(input(f"\n{Fore.CYAN}📋 Select mode (1-3): {Style.RESET_ALL}"))
                if 1 <= mode_choice <= 3:
                    mode = modes[mode_choice-1]
                    break
                else:
                    print(f"{Fore.RED}❌ Please select a number between 1 and 3.")
            except ValueError:
                print(f"{Fore.RED}❌ Please enter a valid number.")
        
        # Generate MAC addresses for each selected prefix
        selected_prefixes = [PREFIXES[i] for i in selected_indices]
        
        print(f"\n{Fore.YELLOW}🚀 Generating {count} MAC addresses for {len(selected_prefixes)} prefix(es)...")
        print(f"{Fore.CYAN}📁 Saving files to: {save_dir}")
        
        # Track all generated MACs to ensure uniqueness across all prefixes
        all_generated_macs = set()
        total_duplicate_count = 0
        
        for prefix in selected_prefixes:
            # Remove colons from prefix for filename
            clean_prefix = prefix.replace(':', '')
            base_filename = f"{format_number(count)} {clean_prefix} unix.txt"  # Changed multix to unix
            filename = get_unique_filename(save_dir, base_filename)
            filepath = os.path.join(save_dir, filename)
            
            print(f"\n{Fore.GREEN}💾 Saving MAC addresses for {prefix} to: {filename}")
            
            with open(filepath, 'w', encoding='utf-8') as f:
                # Generate unique MACs for this prefix
                prefix_macs = set()
                duplicate_count = 0
                generated_count = 0
                
                if mode in ["ascending", "descending"]:
                    # Use generator for memory efficiency
                    suffix_generator = generate_mac_suffixes(count, mode)
                    for suffix in suffix_generator:
                        if generated_count >= count:
                            break
                            
                        mac = prefix + format_mac_suffix(suffix)
                        
                        # Check for duplicates across all prefixes and within this prefix
                        if mac not in all_generated_macs and mac not in prefix_macs:
                            f.write(mac + '\n')
                            all_generated_macs.add(mac)
                            prefix_macs.add(mac)
                            generated_count += 1
                        else:
                            duplicate_count += 1
                            total_duplicate_count += 1
                            
                        if generated_count % 100 == 0:
                            show_loading_bar(f"Generating {prefix}", generated_count, count)
                    
                else:
                    # For random mode, generate until we have enough unique MACs
                    while generated_count < count:
                        suffix = ''.join(random.choices("0123456789ABCDEF", k=6))
                        mac = prefix + format_mac_suffix(suffix)
                        
                        # Check for duplicates across all prefixes and within this prefix
                        if mac not in all_generated_macs and mac not in prefix_macs:
                            f.write(mac + '\n')
                            all_generated_macs.add(mac)
                            prefix_macs.add(mac)
                            generated_count += 1
                        else:
                            duplicate_count += 1
                            total_duplicate_count += 1
                            
                        if generated_count % 100 == 0:
                            show_loading_bar(f"Generating {prefix}", generated_count, count)
                
                # Show completed progress bar
                show_loading_bar(f"Generating {prefix}", generated_count, count)
                print()  # New line after progress bar
                
                if duplicate_count > 0:
                    print(f"{Fore.YELLOW}⚠️  Found and removed {duplicate_count} duplicate MAC addresses for this prefix")
        
        if total_duplicate_count > 0:
            print(f"\n{Fore.YELLOW}⚠️  Total duplicates found and removed: {total_duplicate_count}")
        
        print(f"\n{Fore.GREEN}✅ Done! Generated {len(all_generated_macs)} unique MAC addresses across {len(selected_prefixes)} files.")
        print(f"{Fore.CYAN}📁 Files saved to: {save_dir}")
        
        # Ask if user wants to repeat
        choice = ask_angina_question()
        if choice == '2':
            print(f"\n{Fore.MAGENTA}🙏 Thank you for using 🖤ANGINA🖤 MULTI GENERATOR X!")
            print(f"{Fore.CYAN}👋 Goodbye!")
            break
        else:
            clear_screen()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}❌ Operation cancelled by user.")
        print(f"{Fore.CYAN}👋 Goodbye!")
    except Exception as e:
        print(f"\n{Fore.RED}❌ An error occurred: {e}")
        print(f"{Fore.CYAN}🔄 Please try again.")