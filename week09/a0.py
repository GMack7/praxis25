# Regular Expressions (regex) allows you to search, match 
# and manipulate strings based on pattern of characters within text  
import re

# List the infile and outfile here to simply code in the script
infile = 'week09/pg1519.txt'
outfile = 'week09/pg1519a.txt'

# List of specific characters
characters = ["BENEDICK", "BEATRICE"]

# Counters as a dictionary 
# below is shorthand for the following 
# dialog_count = {}
# for character in characters:
#     dialog_count[character] = 0
# same for character_lengths 
dialog_count = {character: 0 for character in characters}
character_lengths = {character: 0 for character in characters}

# Read the script
# r for read-only file, open function returns a file object 
# defacto standard UTF-8 encoding 
# which manages resources like file, ensures resources are properly 
# opened and closed 
# f is a variable name to represent the file object 
# f.read()
with open(infile, 'r', encoding='utf-8') as f:
    script = f.read()

# split using regular expression 
# r"\n\n" represents two newlines
dialogue_blocks = re.split(r"\n\n", script)

# Track the current speaker
current_speaker = None

# Process each dialogue block
# each block within dialogue_blocks 
# removes leading and trailing whitespace
for block in dialogue_blocks:
    block = block.strip()

    # Identify the speaker (uppercase followed by a period)
    # searches for a pattern at beginning of string
    # r indicates a raw string literal. It prevents Python from interpreting 
    # backslashes as escape sequences
    # ^ means starts with; [] list of characters, special characters become literal
    # inside the set, so + means one or more occurences of the preceding character
    # \. denotes literal period at end of name
    # block is the text being matched
    speaker_match = re.match(r"^([A-Z]+)\.", block)

    # check to see if the match above is found 
    # if it is, then the speaker is grouped into group 1
    if speaker_match:
        speaker = speaker_match.group(1)

        # If the speaker matches is one of the characters above, the two are the same 
        # Otherwise, the current speaker is none 
        if speaker in characters:
            current_speaker = speaker
        else:
            current_speaker = None

    # Counter for valid speakers and block ensures the current block is not empty 
    # dialogue count of current speaker increases in increments of 1
    # increases increments based on the length of the block
    # to count the number of characters (which includes spaces and punctuation)
    if current_speaker and block:
        dialog_count[current_speaker] += 1
        character_lengths[current_speaker] += len(block)

# Write output file
# open file in write mode which overwrites the content if the file already exists 
# do for loop over the list of characters
# Outputs the number of dialogue blocks (lines) and total character count
# for each character
with open(outfile, 'w', encoding='utf-8') as f:
    for character in characters:
        f.write(f"{character} - Total Lines: {dialog_count[character]}, Character Count: {character_lengths[character]}\n")

outfile
