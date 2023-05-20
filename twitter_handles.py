import re


"""
The twitter handles should match the pattern "@username", 
where "username" can be any string of letters and digits.
"""


# '@' should come first
# username has nums and digits

handle_pattern = re.compile("^[@][\w\d]+$")


twitter_handles = [
    "@WhimsicalWanderer",
    "@BlazingComet19",
    "@SerenitySeeker",
    "@ElectricDreamer",
    "@CosmicExplorer",
    "@PixelNinja",
    "@InfiniteJourney",
    "@QuirkyAdventurer",
    "@RainbowChaser299",
    "@SoulfulScribe",
    "@LuckyStarGazer",
    "@Echoes O fEternity",
    "@WhisperingWillow",
    "@Neon Dancer",
    "@ CuriousCrafter"
]

for handle in twitter_handles:
    if handle_pattern.search(handle):
        print(handle, "matches pattern")
    else:
        print(handle, "does not match pattern")

