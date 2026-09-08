# joke_bot.py
import requests#used for making http requests
import random#random for a random choice of the jokes
import colorama#the following three imports are for presentation)
import termcolor
import pyfiglet

colorama.init()

class JokeBot:
    def __init__(self, font="slant", color="magenta"):#initialises the font and colour for the program
        self.font = font
        self.color = color

    def display_banner(self):
        banner = pyfiglet.figlet_format('Dad Jokes Software', font=self.font)
        print(termcolor.colored(banner, color=self.color))

    def fetch_jokes(self, topic):
        url = "https://icanhazdadjoke.com/search"#uses the following url
        response = requests.get(
            url,
            headers={"Accept": "application/json"},
            params={"term": topic}
        )#makes a get request, concatinating all of this info
        data = response.json()
        return data.get("results", [])#returns whats found

    def tell_joke(self, topic=None):
        self.display_banner()#displays the dad joke banner
        if topic is None:#it a topic hasnt been chosen
            topic = input("Gimme a topic for a joke: ")

        if topic:
            jokes = self.fetch_jokes(topic)#searches for the joke using icanhazdadjokes url
            if jokes:
                print(f"I have {len(jokes)} jokes about that topic, here's one:")#tells user how many jokes it found
                print(random.choice(jokes)["joke"])#chooses a random one out of the list and tells it
                
            else:
                print("No jokes found for that topic.")
            answer=input("Would you like to hear another joke?")
            if answer == "yes":
                self.tell_joke()
            else:
                print("Redirecting back to taskhub...")
        else:
            print("You didn't type nuffin.")