from json import JSONDecodeError

import requests
from datetime import datetime
import csv


def get_joke() -> dict:
    try:
        joke = requests.get("https://official-joke-api.appspot.com/random_joe")
        return joke.json()
    except JSONDecodeError:
        if joke.status_code != 200:
            raise ValueError(f"Something wrong with web site (Status Code:{joke.status_code})")


def save_joke(setup: str, punchline: str) -> None:
    with open("jokes_history.csv", "a", newline="") as joke_file:
        joke_writer = csv.writer(joke_file)
        joke_writer.writerow(
            [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), setup, punchline]
        )


def tell_jokes() -> None:
    want_to_continue = "yes"
    while want_to_continue.lower() == "yes":
        joke = get_joke()

        print(joke["setup"])
        enter_pressed = None
        while enter_pressed != "":
            enter_pressed = input("Press Enter to see the punchline...")
        print(joke["punchline"])
        save_joke(joke["setup"], joke["punchline"])

        want_to_continue = input("Would you like another joke? (yes/no): ")


def main() -> None:
    # this is an entrypoint, DO NOT WRITE ALL CODE HERE !!!
    # ToDo remove these comments
    with open("jokes_history.csv", "a", newline="") as joke_file:
        joke_writer = csv.writer(joke_file)
        joke_writer.writerow(
            ["timestamp", "setup", "punchline"]
        )
    tell_jokes()


if __name__ == "__main__":
    main()
