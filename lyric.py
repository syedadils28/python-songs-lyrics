import time
import os

# --- Full Lyrics ---
lyrics1 = [
    "🎶 Pal Pal..... 🎶",
    "",
    "Pal pal jeena muhal",
    "Mera tere bina",
    "Ye sary nashe bekaar",
    "Teri ankhon kay siwa",
    "Ghar nahi jata mein bahar",
    "Rehta tera intazar",
    "Mere, khwabon mein aa na",
    "Kakry sola singhaar",
    
]

lyrics2 = [
    "Mein ab kyu hosh mein ata ni",
    "Sukoon ye dil kyu pata ni",
    "Kyu toru khud say jo thy wade kay ab ye ishq nibahana nahi",
    "Mein moru tumsy jo ye chehra dubara nazar milana nahi",
    "Ye duniya janay mera dard tujhe ye nazar kyu ata nahi",
    "Soneya yu tera sharmana meri jaan na lele",
    "Kaan ke peechy zulf chupana meri jan kya kehnay",
    "Zalima toba tera nakhra iske war kya kehne",
    "Tham ky bethe dil ko ghayal kaheen har na bethein"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# 🎶 Part 1 – slower speed
def display_lyrics1(lyrics):
    for line in lyrics:
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.09)  # slower typing
        print()
        time.sleep(0.5)

# 🎶 Part 2 – faster speed
def display_lyrics2(lyrics):
    for line in lyrics:
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.07)  # faster typing
        print()
        time.sleep(0.4)

if __name__ == "__main__":
    clear_screen()
    print("🎶 Now Playing 🎶\n")
    display_lyrics1(lyrics1)  

    # small delay before next part
    # time.sleep(1.5)
    display_lyrics2(lyrics2)
