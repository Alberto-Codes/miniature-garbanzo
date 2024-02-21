# src/main.py

from datetime import datetime
import os

name = input("What's your name? ")
team = input("What's your favorite football team? ")
print(f"Hello, {name}! Good luck to {team} in their next game!")
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
with open('log.txt', 'a') as f:
    f.write(f"At {timestamp}, {name} ran the code. They're cheering for {team} this season!\n")