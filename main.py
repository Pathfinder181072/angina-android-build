import os
import sys
from os.path import exists, join
import subprocess

# Add current directory to path for imports
sys.path.append(os.getcwd())

def run_script(script_name):
    """Execute a Python script from the same directory"""
    try:
        script_path = join(os.getcwd(), script_name)
        if exists(script_path):
            print(f"--- Running {script_name} ---")
            with open(script_path, 'r', encoding='utf-8') as f:
                code = compile(f.read(), script_name, 'exec')
                exec(code, globals())
        else:
            print(f"Error: {script_name} not found!")
    except Exception as e:
        print(f"Error running {script_name}: {str(e)}")

def main_menu():
    """Android-compatible menu system"""
    while True:
        print("\n" + "="*50)
        print("       ANGINA TOOLS - ANDROID EDITION")
        print("="*50)
        print("1. ANGINA 3 Scanner")
        print("2. Multi MAC Tool")
        print("3. Portal Detective MAC Plus")
        print("4. Proxy Scraper")
        print("5. Similar Portals")
        print("6. File Splitter")
        print("7. Docs Section Extractor")
        print("8. Exit")
        print("="*50)
        
        choice = input("\nSelect an option (1-8): ").strip()
        
        if choice == "1":
            run_script("ANGINA_3_Scanner.py")
        elif choice == "2":
            run_script("ANGINA_Multi_MAC.py")
        elif choice == "3":
            run_script("Portal_Detective_MAC_Plus.py")
        elif choice == "4":
            run_script("Proxy_Scraper.py")
        elif choice == "5":
            run_script("Similar_Portals.py")
        elif choice == "6":
            run_script("File_Splitter.py")
        elif choice == "7":
            run_script("Docs_Section_Extractor.py")
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-8.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    # Android-specific setup
    if hasattr(sys, 'getandroidapilevel'):
        print("Running on Android device!")
        # Request necessary permissions
        try:
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.INTERNET, Permission.ACCESS_NETWORK_STATE])
        except:
            pass
    
    main_menu()