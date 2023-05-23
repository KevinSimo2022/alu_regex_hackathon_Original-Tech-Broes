#!/usr/bin/env python3

import re

'''This code matches episode titles pattern into "Show Name SXXEXX: Episode Title", 
where "Show Name" is any string of characters, 
SXX is a two-digit season number and EXX is a two-digit episode number, 
and "Episode Title" is any string of characters'''

# Episodes titles of movies are listed including their season number and episode number

episode_titles = ['Money Heist S13E03', 'Money Heist S11E13', 'Money Heist S06E10', 'Money Heist S10E05']
regex_episode = r"(\w+)\sS(\d{2})E(\d{2}):\s(.*)"

for episode_title in episode_titles:
    match = re.match(regex_episode, episode_title)
    if match:
        show_name = match.group(1)
        season_number = match.group(2)
        episode_number = match.group(3)
        print(f"Show: {show_name}, Season: {season_number}, Episode: {episode_number})
