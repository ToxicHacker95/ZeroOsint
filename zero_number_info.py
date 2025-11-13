import requests
import time
import sys
import os
from colorama import init, Fore, Style, Back
import random

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animated_text(text, delay=0.03, color=Fore.CYAN):
    """Create animated running text effect with color"""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def rainbow_text(text):
    """Create rainbow-colored text effect"""
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def loading_animation():
    """Show loading animation with emojis"""
    emojis = ["⏳", "⌛", "🔍", "📡", "📲"]
    for _ in range(3):
        for emoji in emojis:
            sys.stdout.write(f"\r{Fore.YELLOW} {emoji} Fetching information... {emoji}")
            sys.stdout.flush()
            time.sleep(0.2)
    print("\r" + " " * 50 + "\r", end="")

def display_banner():
    """Display animated banner with emojis"""
    clear_screen()
    print(Fore.MAGENTA + "="*60)
    rainbow_text("𝗭 𝗘 𝗥 𝗢 ✥ 𝗢 𝗦 𝗜 𝗡 𝗧 ✥ 𝗧𝗢𝗢𝗟")
    print(Fore.MAGENTA + "="*60)
    print(Fore.YELLOW + "🔍➤ 𝗠𝗢𝗕𝗜𝗟𝗘 𝗡𝗨𝗠 𝗜𝗡𝗙𝗢 ☉︎ 🔍")
    print(Fore.MAGENTA + "="*60 + "\n")

def get_number_info(mobile_number):
    """Fetch number information from API"""
    api_url = f"https://mynkapi.amit1100941.workers.dev/?mobile={mobile_number}&key=mynk01"
    
    try:
        loading_animation()
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        
        # Filter out developer info
        if 'data' in data:
            return data['data']
        return None
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"❌ Error fetching data: {e}")
        return None

def display_info(data):
    """Display formatted information with colors and emojis"""
    if not data:
        print(Fore.RED + "❌ No information found for this number.")
        return
    
    for idx, entry in enumerate(data, 1):
        # Entry header with random color
        header_colors = [Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
        header_color = random.choice(header_colors)
        
        print(header_color + Style.BRIGHT + f"\n📋 Entry #{idx}")
        print(Fore.BLUE + "🌟" + "─"*40 + "🌟")
        
        # Display each field with emoji and color coding
        fields = [
            ("📱 Mobile", entry.get("mobile", "N/A"), Fore.YELLOW),
            ("👤 Name", entry.get("name", "N/A"), Fore.CYAN),
            ("👨 Father's Name", entry.get("fname", "N/A"), Fore.GREEN),
            ("🏠 Address", entry.get("address", "N/A"), Fore.WHITE),
            ("📞 Alternate Number", entry.get("alt", "N/A"), Fore.MAGENTA),
            ("🌐 Circle", entry.get("circle", "N/A"), Fore.BLUE),
            ("🆔 ID", entry.get("id", "N/A"), Fore.RED),
            ("✉️ Email", entry.get("email", "N/A"), Fore.YELLOW)
        ]
        
        for field, value, color in fields:
            print(color + f"{field:20}: " + Fore.WHITE + f"{value}")
        
        print(Fore.BLUE + "🌟" + "─"*40 + "🌟")

def main():
    display_banner()
    
    while True:
        mobile_number = input(Fore.CYAN + "📲 𝐄𝐧𝐭𝐞𝐫 𝐘𝐨𝐮𝐫 𝐍𝐮𝐦𝐛𝐞𝐫: ")
        
        if mobile_number.lower() == 'exit':
            print(Fore.MAGENTA + "\n👋 Exiting ZERO NUMBER INFO...")
            time.sleep(1)
            clear_screen()
            break
        
        if not mobile_number.isdigit() or len(mobile_number) != 10:
            print(Fore.RED + "❌ Please enter a valid 10-digit mobile number.")
            continue
        
        data = get_number_info(mobile_number)
        display_info(data)
        
        input(Fore.CYAN + "\n⏎ Press Enter to continue...")
        display_banner()

if __name__ == "__main__":
    main()