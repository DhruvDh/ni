import os
import re
import sys

base_url = '/ni'
os.chdir('src')

count = 0

for thing in os.listdir('.'):
    path = os.path.join(os.getcwd(), thing)

    if thing.endswith('.md') or thing.endswith(".MD"):
        with open(path, 'r+') as file:
            text = file.read()
            
            # print(f"{path}: {len(text.split())} words.")
            count += len(text.split())

print(f"{count} words.")