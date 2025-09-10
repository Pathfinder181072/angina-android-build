#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

# Function to check and install required packages
def install_packages():
    required_packages = ['colorama', 'pyfiglet', 'glob']
    
    for package in required_packages:
        try:
            # Check if package is available (glob is in standard library)
            if package != 'glob':
                __import__(package)
            print(f"✅ {package} is available")
        except ImportError:
            if package == 'glob':
                # glob is in standard library, should not need installation
                continue
                
            print(f"🔍 Installing {package}...")
            try:
                # Try pip install
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"✅ {package} installed successfully")
            except Exception as e:
                print(f"⚠️  Failed to install {package} with pip: {e}")
                try:
                    # Try easy_install as fallback (for QPython)
                    subprocess.check_call([sys.executable, "-m", "easy_install", package])
                    print(f"✅ {package} installed successfully with easy_install")
                except Exception as e2:
                    print(f"❌ Failed to install {package}: {e2}")
                    return False
    return True

# Install packages if needed
if install_packages():
    import colorama
    from colorama import Fore, Back, Style
    import pyfiglet
    
    colorama.init(autoreset=True)

# Import glob (standard library, should always be available)
import glob

# Display banner function
def display_banner():
    # Clear screen based on platform
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac/QPython
        os.system('clear')
    
    # Create ANGINA banner
    try:
        f = pyfiglet.Figlet(font='slant')
        banner_text = f.renderText('ANGINA')
        print(Fore.RED + Style.BRIGHT + banner_text)
    except:
        print(Fore.RED + Style.BRIGHT + "=" * 40)
        print(Fore.RED + Style.BRIGHT + "          A N G I N A")
        print(Fore.RED + Style.BRIGHT + "=" * 40)
    
    print(Fore.CYAN + Style.BRIGHT + "🔧 Combine Scripts - All in One Tools 🛠️")
    print(Fore.YELLOW + "=" * 60)
    print()

# Original functionality - combine scripts
def combine_scripts():
    # Get all Python files in the current directory (excluding this file)
    python_files = [f for f in glob.glob("*.py") if f != os.path.basename(__file__)]
    
    if not python_files:
        print(Fore.RED + "❌ No Python scripts found in the current directory!")
        input(Fore.MAGENTA + "Press Enter to continue..." + Style.RESET_ALL)
        return
    
    print(Fore.GREEN + "📋 Available scripts:")
    print(Fore.YELLOW + "➖" * 30)
    
    for i, script in enumerate(python_files, 1):
        print(Fore.CYAN + f"{i}. {script}")
    
    print(Fore.CYAN + f"{len(python_files) + 1}. 🚪 Exit ")
    print()
    
    try:
        choice = int(input(Fore.MAGENTA + "👉 Select an option (number): " + Style.RESET_ALL))
        
        if 1 <= choice <= len(python_files):
            selected_script = python_files[choice-1]
            print(Fore.GREEN + f"🚀 Running {selected_script}...")
            print(Fore.YELLOW + "➖" * 40)
            
            # Execute the selected script
            if os.name == 'nt':  # Windows
                os.system(f"python {selected_script}")
            else:  # Unix/Linux/Mac/QPython
                os.system(f"python3 {selected_script}")
                
            # Return to menu after script execution
            print()
            input(Fore.MAGENTA + "Press Enter to return to menu..." + Style.RESET_ALL)
            
            
        elif choice == len(python_files) + 1:
            # Exit
            print(Fore.GREEN + "👋 Thank you for using Combine Scripts!")
            sys.exit()
            
        else:
            print(Fore.RED + "❌ Invalid selection!")
            input(Fore.MAGENTA + "Press Enter to continue..." + Style.RESET_ALL)
            
    except ValueError:
        print(Fore.RED + "❌ Please enter a valid number!")
        input(Fore.MAGENTA + "Press Enter to continue..." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"❌ Error: {e}")
        input(Fore.MAGENTA + "Press Enter to continue..." + Style.RESET_ALL)

# Main function
def main():
    while True:
        display_banner()
        combine_scripts()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n\nProgram interrupted. Exiting...")
        sys.exit(0)