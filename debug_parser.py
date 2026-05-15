#!/usr/bin/env python3

import sys
import json
from kindle_highlights_to_markdown import parse_clippings

# Debug: Print raw file content
with open('test_clippings.txt', 'r', encoding='utf-8-sig') as f:
    print('=== RAW FILE CONTENT ===')
    print(f.read())
    print('=== END RAW FILE ===')

highlights = parse_clippings('test_clippings.txt')
print(f'Parsed {len(highlights)} highlights:')
for h in highlights:
    print(json.dumps(h.to_dict(), indent=2, ensure_ascii=False))