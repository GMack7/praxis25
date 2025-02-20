import re

infile = 'week09/pg1519.txt'
outfile = 'week09/pg1519a.txt'

characters = ["BENEDICK", "BEATRICE"]

dialog_count = {character: 0 for character in characters}
character_lengths = {character: 0 for character in characters}

with open(infile, 'r', encoding='utf-8') as f:
    script = f.read()

dialogue_blocks = re.split(r"\n\n", script)

current_speaker = None

for block in dialogue_blocks:
    block = block.strip()

    speaker_match = re.match(r"^([A-Z]+)\.", block)

    if speaker_match:
        speaker = speaker_match.group(1)

        if speaker in characters:
            current_speaker = speaker
        else:
            current_speaker = None

    if current_speaker and block:
        dialog_count[current_speaker] += 1
        character_lengths[current_speaker] += len(block)

with open(outfile, 'w', encoding='utf-8') as f:
    for character in characters:
        f.write(f"{character} - Total Lines: {dialog_count[character]}, Character Count: {character_lengths[character]}\n")

outfile
