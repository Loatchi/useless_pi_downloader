#!/usr/bin/python3

import re
import requests


def construct_pi():

    regex_response = re.compile(r"(?P<PI>\d+)")
    found = False

    try:
        with open(".pi_progress", "r") as f:
            current = int(f.readline())
        found = True
    except FileNotFoundError:
        print("Progress not found: set to 0")
        current = 0

    try:
        with open("pi.txt", "a" if found else "w") as f:
            while current < 100_000_000_000_000:
                response = requests.get(
                    f"https://api.pi.delivery/v1/pi?start={int(current/1000)}&numberOfDigits={1000}&radix=10")
                for match in re.findall(regex_response, response.text):
                    f.write(match)
                current += 1000
                print(f"\r{current}/100,000,000,000,000 pi numbers queried [{round(current/100_000_000_000_000*100, 6)}%]",
                      end="")

    except KeyboardInterrupt:

        with open(".pi_progress", "w") as f:
            f.write(str(current))

        print(f"\nWritten {current} numbers of pi in pi.txt\nSaved progress in .progress_pi")


def main():
    construct_pi()


if __name__ == '__main__':
    main()
