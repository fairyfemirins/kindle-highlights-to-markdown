import re

entry = '''The Lean Startup: How Today's Entrepreneurs Use Continuous Innovation to Create Radically Successful Businesses (Eric Ries)
- Your Highlight on Location 123-124 | Added on Saturday, May 10, 2025 2:30:22 PM

The fundamental activity of a startup is to turn ideas into products, measure how customers respond, and then learn whether to pivot or persevere.'''

# Simplified regex
pattern = r'^(.*?) \((.*?)\)\n- (.+?)\n\n(.+)$'
match = re.match(pattern, entry, re.DOTALL)
print('Match:', match.groups() if match else 'None')