import os
import re
import sys

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

with open('../words', 'r') as f:
    old_count = int(f.read())
    print(f"..added {count - old_count} words since last build.")