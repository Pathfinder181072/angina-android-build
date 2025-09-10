import os
import re
from datetime import datetime

# ANSI color codes for cross-platform compatibility
class Colors:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_banner():
    """Print the ASCII banner with colors"""
    banner = f"""
{Colors.RED}{Colors.BOLD}
    █████╗ ███╗   ██╗ ██████╗ ██╗███╗   ██╗ █████╗ 
   ██╔══██╗████╗  ██║██╔════╝ ██║████╗  ██║██╔══██╗
   ███████║██╔██╗ ██║██║  ███╗██║██╔██╗ ██║███████║
   ██╔══██║██║╚██╗██║██║   ██║██║██║╚██╗██║██╔══██║
   ██║  ██║██║ ╚████║╚██████╔╝██║██║ ╚████║██║  ██║
   ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
{Colors.RESET}
            {Colors.YELLOW}✂️ Advanced Text Extractor ✂️{Colors.RESET}
"""
    print(banner)

def extract_single_headers(text, headers):
    """Extract ALL individual key-value pairs for each header"""
    results = {}
    
    lines = text.split('\n')
    
    for header in headers:
        # Create a pattern to match the header followed by a value
        pattern = re.compile(re.escape(header) + r'\s*:?\s*(.+)$', re.IGNORECASE)
        
        header_results = []
        for line in lines:
            match = pattern.search(line)
            if match:
                value = match.group(1).strip()
                full_line = f"{header}: {value}"
                header_results.append(full_line)
                print(f"{Colors.GREEN}✅ Found: {full_line}{Colors.RESET}")
        
        if header_results:
            results[header] = header_results
        else:
            print(f"{Colors.RED}❌ Not found: {header}{Colors.RESET}")
            results[header] = []
    
    return results

def extract_header_groups(text, target_headers):
    """Extract complete groups of headers that appear together in sequence"""
    results = []
    
    lines = text.split('\n')
    target_patterns = {header: re.compile(re.escape(header) + r'\s*:?\s*(.+)$', re.IGNORECASE) 
                      for header in target_headers}
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check if this line matches any of our target headers
        matched_header = None
        for header, pattern in target_patterns.items():
            match = pattern.search(line)
            if match:
                matched_header = header
                break
        
        if matched_header:
            # We found a target header, now check if we have a complete group
            group = {}
            j = i
            
            # Look for consecutive target headers
            while j < len(lines):
                current_line = lines[j].strip()
                found_in_line = False
                
                for header, pattern in target_patterns.items():
                    match = pattern.search(current_line)
                    if match and header not in group:  # Only add if not already in this group
                        value = match.group(1).strip()
                        group[header] = f"{header}: {value}"
                        found_in_line = True
                        print(f"{Colors.GREEN}✅ Found in group: {header}: {value}{Colors.RESET}")
                        break
                
                # If we didn't find any new target header in this line, stop the group
                if not found_in_line:
                    break
                    
                j += 1
            
            # If we found a complete group (all target headers), add it to results
            if group and len(group) >= len(target_headers):
                results.append(group)
                print(f"{Colors.GREEN}✅ Found complete group with {len(group)} headers{Colors.RESET}")
                i = j  # Skip ahead to after this group
            else:
                i += 1
        else:
            i += 1
    
    return results

def extract_text_from_file(file_path):
    """Extract text from file with proper encoding handling"""
    try:
        # Try multiple encodings
        encodings = ['utf-8', 'utf-16', 'latin-1', 'cp1252', 'iso-8859-1']
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding, errors='replace') as f:
                    text = f.read()
                print(f"{Colors.GREEN}✅ File loaded with {encoding} encoding{Colors.RESET}")
                return text, "Success"
            except (UnicodeDecodeError, UnicodeError):
                continue
        return None, "Failed to read file with any encoding"
    except Exception as e:
        return None, f"Error reading file: {str(e)}"

def select_file(input_folder):
    """Select a file from the input folder"""
    try:
        files = [f for f in os.listdir(input_folder) if f.lower().endswith('.txt')]
    except FileNotFoundError:
        return None, "Input folder not found"
    
    if not files:
        return None, "No TXT files found in input folder"
    
    print(f"{Colors.CYAN}📁 Available files:{Colors.RESET}")
    for i, f in enumerate(files):
        print(f"{Colors.CYAN}{i+1}. {f}{Colors.RESET}")
    
    try:
        choice = input(f"{Colors.WHITE}Enter file number: {Colors.RESET}")
        choice_num = int(choice)
        if 1 <= choice_num <= len(files):
            return os.path.join(input_folder, files[choice_num-1]), "Success"
        else:
            return None, "Invalid selection"
    except ValueError:
        return None, "Please enter a valid number"

def get_headers_from_user():
    """Get headers from user input"""
    headers = []
    print(f"{Colors.MAGENTA}📝 Enter the headers to extract (one per line, press Enter twice when done):{Colors.RESET}")
    
    while True:
        header = input(f"{Colors.WHITE}>{Colors.RESET} ").strip()
        if not header:
            if not headers:
                print(f"{Colors.RED}❌ Please enter at least one header{Colors.RESET}")
                continue
            break
        headers.append(header)
        print(f"{Colors.GREEN}✅ Added: {header}{Colors.RESET}")
    
    return headers

def save_single_results(output_path, file_path, results):
    """Save individual header results to file"""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"Extraction performed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Source file: {os.path.basename(file_path)}\n")
            f.write("=" * 50 + "\n\n")
            
            total_found = 0
            for header, values in results.items():
                if values:
                    f.write(f"--- {header} ---\n")
                    for value in values:
                        f.write(f"{value}\n")
                    f.write("\n")
                    total_found += len(values)
            
            f.write(f"Total found: {total_found} entries across {len([v for v in results.values() if v])} headers")
        
        return True, "Success"
    except Exception as e:
        return False, f"Error saving file: {str(e)}"

def save_group_results(output_path, file_path, groups):
    """Save extracted header groups to file"""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"Extraction performed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Source file: {os.path.basename(file_path)}\n")
            f.write("=" * 50 + "\n\n")
            
            for i, group in enumerate(groups, 1):
                f.write(f"--- Group {i} ---\n")
                for header in group.values():
                    f.write(f"{header}\n")
                f.write("================\n\n")
            
            f.write(f"Total found: {len(groups)} complete groups\n")
        
        return True, "Success"
    except Exception as e:
        return False, f"Error saving file: {str(e)}"

def get_extraction_mode():
    """Let user choose extraction mode"""
    print(f"\n{Colors.BLUE}🔧 Choose extraction mode:{Colors.RESET}")
    print(f"{Colors.CYAN}1. Extract individual headers (all occurrences){Colors.RESET}")
    print(f"{Colors.CYAN}2. Extract header groups (complete sets){Colors.RESET}")
    
    while True:
        choice = input(f"{Colors.WHITE}Enter choice (1 or 2): {Colors.RESET}").strip()
        if choice == '1':
            return 'single'
        elif choice == '2':
            return 'group'
        else:
            print(f"{Colors.RED}❌ Please enter 1 or 2{Colors.RESET}")

def main():
    """Main function"""
    print_banner()
    print(f"{Colors.RED}{'=' * 50}{Colors.RESET}")
    print(f"{Colors.CYAN}      EASY - FAST - RELIABLE{Colors.RESET}")
    print(f"{Colors.RED}{'=' * 50}{Colors.RESET}")
    print()
    
    # Create folders
    input_folder = "Xtrct Input"
    output_folder = "Xtrct Output"
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)
    
    print(f"{Colors.YELLOW}📁 Place your text files in the 'Xtrct Input' folder{Colors.RESET}")
    input(f"{Colors.WHITE}Press Enter to continue...{Colors.RESET}")
    
    while True:
        print(f"\n{Colors.BLUE}{'=' * 50}{Colors.RESET}")
        
        # Select extraction mode
        mode = get_extraction_mode()
        
        # Select file
        print(f"{Colors.CYAN}🔍 Selecting file...{Colors.RESET}")
        file_path, status = select_file(input_folder)
        if file_path is None:
            print(f"{Colors.RED}❌ {status}{Colors.RESET}")
            input(f"{Colors.WHITE}Press Enter to try again...{Colors.RESET}")
            continue
        
        print(f"{Colors.GREEN}✅ Selected: {os.path.basename(file_path)}{Colors.RESET}")
        
        # Read file
        print(f"{Colors.CYAN}📄 Reading file...{Colors.RESET}")
        text, status = extract_text_from_file(file_path)
        if text is None:
            print(f"{Colors.RED}❌ {status}{Colors.RESET}")
            input(f"{Colors.WHITE}Press Enter to try again...{Colors.RESET}")
            continue
        
        # Get headers
        print()
        headers = get_headers_from_user()
        
        # Extract based on mode
        if mode == 'single':
            print(f"\n{Colors.CYAN}🔍 Extracting individual headers...{Colors.RESET}")
            results = extract_single_headers(text, headers)
            
            # Count total found
            total_found = sum(len(values) for values in results.values())
            if total_found == 0:
                print(f"{Colors.RED}❌ No matching headers found{Colors.RESET}")
                input(f"{Colors.WHITE}Press Enter to try again...{Colors.RESET}")
                continue
            
            print(f"{Colors.GREEN}✅ Found {total_found} total entries{Colors.RESET}")
            
            # Save results
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            output_filename = f"individual_{base_name}_{timestamp}.txt"
            output_path = os.path.join(output_folder, output_filename)
            
            success, message = save_single_results(output_path, file_path, results)
            
            if success:
                print(f"{Colors.GREEN}✅ Individual extraction complete!{Colors.RESET}")
                print(f"{Colors.CYAN}📁 Saved to: {output_path}{Colors.RESET}")
        
        else:  # group mode
            print(f"\n{Colors.CYAN}🔍 Extracting header groups...{Colors.RESET}")
            groups = extract_header_groups(text, headers)
            
            if not groups:
                print(f"{Colors.RED}❌ No complete header groups found{Colors.RESET}")
                input(f"{Colors.WHITE}Press Enter to try again...{Colors.RESET}")
                continue
            
            print(f"{Colors.GREEN}✅ Found {len(groups)} complete groups{Colors.RESET}")
            
            # Save results
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            output_filename = f"groups_{base_name}_{timestamp}.txt"
            output_path = os.path.join(output_folder, output_filename)
            
            success, message = save_group_results(output_path, file_path, groups)
            
            if success:
                print(f"{Colors.GREEN}✅ Group extraction complete!{Colors.RESET}")
                print(f"{Colors.CYAN}📁 Saved to: {output_path}{Colors.RESET}")
        
        # Continue or exit
        print(f"\n{Colors.CYAN}1. Process another file{Colors.RESET}")
        print(f"{Colors.CYAN}2. Exit{Colors.RESET}")
        choice = input(f"{Colors.WHITE}Enter choice (1 or 2): {Colors.RESET}").strip()
        if choice != '1':
            print(f"{Colors.GREEN}👋 Goodbye!{Colors.RESET}")
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{Colors.RED}❌ Error: {e}{Colors.RESET}")
        input(f"{Colors.WHITE}Press Enter to exit...{Colors.RESET}")