def encode(filepath):
    """
    Write code that opens up the text file specified in the argument,
    swaps out certain words in the text with replacement phrases (i.e. encodes it),
    and overwrites the original file text with the new modified text.

    Requirements:
    - The words to find and replace are given in a dictionary below, which must be used.
    - You are forbidden from hard-coding any of the string literals you see in this dictionary anywhere else in your program.
    - The program must not crash under any circumstances.

    :params filepath: The path of the text file to encode.
    :returns: True if one or more words in the original text were swapped for their replacements.  False otherwise.
    """
    swaps = {
        "dull": "a few sandwiches short of a picnic",
        "failing": "a temporarily-embarrassed honors student",
        "effort": "elbow grease",
        "excellent": "better-than-anticipated",
        "strict": "a bit more demanding than one might otherwise have anticipated",
        "fair": "exceedingly generous",
    }

    swapped = False

    try:
        with open(filepath, "r") as f:
            text = f.read()

        for word, replacement in swaps.items():
            if word in text:
                text = text.replace(word, replacement)
                swapped = True

        with open(filepath, "w") as f:
            f.write(text)
    except (OSError, IOError):
        return False

    return swapped


# -------------------------------------------------------- #
# Do not modify the code below this line #
# running this file tries out the encoding on the file at: data/secret_message.txt
if __name__ == "__main__":
    # call the function if this file is being run directly
    import os

    filepath = os.path.join(os.path.curdir, "data", "secret_message.txt")
    result = encode(filepath)
    if result:
        print("Swapped at least one word!")
    else:
        print("No words swapped!")