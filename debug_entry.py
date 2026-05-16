import re
from pathlib import Path

with open('test_clippings.txt', 'r', encoding='utf-8-sig') as f:
    content = f.read()

entries = re.split(r'\r?\n==========\r?\n', content)
print('First entry:')
print(repr(entries[0]))