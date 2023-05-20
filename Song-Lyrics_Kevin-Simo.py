#!/usr/bin/env python3

import re
'''A code to match the pattern "[Verse X] some lyrics", where X is a number, 
and "some lyrics" can be any string of characters.'''

regex_lyrics = r'\[Verse (\d+)\] (.*)'
song_lyrics = "[Verse 1] I don't need any money\n[Verse 2] I need more self time\n[verse a] Tell me what's wrong with you"

matches = re.findall(regex_lyrics, song_lyrics)

for match in matches:
    verse_number = match[0]
    text_lyrics = match[1]
    print(f"Verse {verse_number}: {text_lyrics}")