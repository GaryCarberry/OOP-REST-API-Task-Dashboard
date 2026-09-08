import keyboard
from weatherAPI import WeatherApp
from taskList import Taskr
from Dad_jokes_2 import JokeBot
from News_API import get_global_news
from colorama import init, Fore#used for a gui effect and to make the menu more enticing
import time
init(autoreset=True)

planner = Taskr()
weather1 = WeatherApp()
jokes = JokeBot()

topics = ("business", "entertainment", "general", "health", "science", "sports", "technology")#tuple for making sure the user picks a correct topic


def main(todayweather=None):#main running, defaults todayweather to none to stop the program defaulting over and over
    running = True#flag for running the menu system
    while running:
        print(Fore.CYAN + "=" * 40)
        print(Fore.YELLOW + "🗂️  Welcome to TaskHub!")
        print("Here, you can use some fun and useful tools.")
        print("\nChoose an option:")
        print("  1 To-Do List Maker")
        print("  2 Weather")
        print("  3 Tell Me a Joke")
        print("  4 More News")
        print("  5 Quit")
        print(Fore.CYAN + "=" * 40)
        print("\n" + Fore.MAGENTA + "📰  Here are your general news items for today:\n")

        get_global_news("general")

        print("\nChoose by pressing a number key (1–5)")

        #waits for a key event
        key_event = keyboard.read_event(suppress=True)#suppress ensure the key press is used only for the input
        if key_event.event_type == keyboard.KEY_DOWN:
            key = key_event.name#assigns choice here

            if key == "1":
                print("You chose To-Do List Maker")
                planner.tskFiler(todayweather)
                

            elif key == "2":
                print("You chose Weather")
                todayweather = weather1.weather()
                

            elif key == "3":
                print("You chose Joke")
                jokes.tell_joke()

            elif key == "4":
                topic = input("Please enter the topic you want to see more of: ").lower()
                while topic not in topics:#small error handling using the tuple as seen before
                    topic = input(
                        "Invalid input. Please choose from: business, entertainment, general, health, science, sports, technology: ").lower()
                get_global_news(topic)#takes arguement of the topic

            elif key == "5":
                print("Goodbye!")
                running = False
            time.sleep(2)

            


if __name__ == "__main__":
    main()