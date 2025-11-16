import time
import os

# --- Full Lyrics ---

lyrics1 = [
    "🎶 Playing: Sahiba..... 🎶",
    "",
    "Sahiba, aaye ghar kaahe na?",
    "Aise to sataaye na",
    "Dekhu tujhko, chain aata hai😊",
    "",
    
]

lyrics2 = [
   "Sahiba, neende-veende aaye na", 
   "raate kaati jaaye na",
    "Tera hi khayal din-rain aata hai",
]

lyrics3 = [
    "",
    "Sahiba, samundar, meri aankho me rah gaye",
    "Ham aate-aate jaana, teri yaado me reh gaye",
    "Ye palke gawahi hai, ham raato me reh gaye",
    "Jo vaade kiye saare, bas baato me reh gaye😍",

]

lyrics4 = [
    "",
    "Baato-baato me hi, khwabo-khwabo me hi ",
    "mere qareeb hai tu", 
    "Teri talab mujhko, teri talab, jaana",
    "ho to kabhi ru-ba-ru",
    "Shor-sharaba jo seene me hai mere",
    "kaise bayaan mai karu?❤️🫣",
    
]

lyrics5=[
    "",
    "Haal jo mеra hai, mai kis ko batau?",
    "Mere sahiba, dil na kiraaye ka",
    "thoda to sambhalo na",
    "Nazuk hai yеh, toot jaata hai",
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
        time.sleep(0.6)

# 🎶 Part 2 – faster speed
def display_lyrics2(lyrics):
    for line in lyrics:
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.09)  # faster typing
        print()
        time.sleep(1.0)

# 🎶 Part 3 – slower speed
def display_lyrics3(lyrics):
    for line in lyrics:
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.08)  # faster typing
        print()
        time.sleep(1.0)

# 🎶 Part 4 – final slow ending style
def display_lyrics4(lyrics):
    for line in lyrics:
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.06)   # slightly slow for emotional effect
        print()
        time.sleep(0.6)

# 🎶 Part 5 – final slow ending style
def display_lyrics5(lyrics):
    for line in lyrics:
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.08)   # slightly slow for emotional effect
        print()
        time.sleep(0.7)

if __name__ == "__main__":
    clear_screen()
    # print("🎶 Now Playing 🎶\n")
    display_lyrics1(lyrics1)  

    # small delay before next part
    # time.sleep(1.5)
    display_lyrics2(lyrics2)

    #2 time
    display_lyrics3(lyrics3)
    display_lyrics4(lyrics4)
    display_lyrics5(lyrics5)
