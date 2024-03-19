# takes a list of buzzwords and a string, and uses the list to remove the words from the string
def removeBuzzwords(buzzwords: list[str], stringToRemoveFrom: str) -> str:
    res = stringToRemoveFrom
    for buzzword in buzzwords:
        res = res.replace(buzzword + " ", "REDACTED ")

    return res


# readWordsFile takes in a path to a words file, reads it, and returns a list of words
def readWordsFile(pathToWordsFile: str) -> list[str]:
    words: list[str] = []
    # attempts to open the file, throws an error if not found
    try:
        with open(pathToWordsFile) as f:
            for line in f:
                # strip newline and excess whitespace characters from both sides of the line, then adds the line to the words array
                words.append(line.strip("\n").strip())
    except FileNotFoundError as e:
        print("ERROR: Please provide a valid path to a words file.")
        print(e)
    return words


def readListingFile(words: list[str], pathToListingFile: str) -> str:
    lines: list[str] = []
    try:
        # attempts to open the file, throws an error if not found
        with open(pathToListingFile) as f:
            for line in f:
                # stops reading at the delimiter ----\n
                if line == "----\n":
                    break
                # adds line to the lines array
                lines.append(line)
            # combines lowercased line strings into one string
            listing = "".join([line.lower() for line in lines])

            # cleans the singular string by calling the removeBuzzwords function
            cleanedStr = removeBuzzwords(words, listing)

        return cleanedStr
    except FileNotFoundError as e:
        print("ERROR: Please provide a valid path to a listing file.")
        print(e)


def writeToListingFile(cleanedStr: str, pathToListingFile: str) -> None:
    # function does nothing if given improper inputs
    if not cleanedStr or not pathToListingFile:
        return

    try:
        with open(pathToListingFile, mode="a") as f:
            f.write("----\n" + "CLEANED LISTING:\n" + cleanedStr)
    except FileNotFoundError as e:
        print("ERROR: Failure to write to file.")
        print(e)


"""
Driver method
"""


def main():
    # flag controls when the program is running
    flag = True
    # store list of words in an array
    words: list[str] = []
    # store listing string in a variable
    listing: str

    while flag:
        # ask user for a file path to words document
        pathToWordsFile = input(
            "Give me a path to the words file, or type 'quit' to exit: "
        )
        # user has option to quit
        if pathToWordsFile == "quit":
            flag = False
            continue

        # read words from the words input
        words = readWordsFile(pathToWordsFile)
        if not words:
            continue

        # once we have our words, we can move onto reading the second file
        # ask user for a file path to listing document
        pathToListingFile = input(
            "Please provide a path to the listing text file, or type 'quit to exit: "
        )
        # user has option to quit
        if pathToListingFile == "quit":
            flag = False
            continue

        # reads the listing file, which also cleans the string
        listing = readListingFile(words, pathToListingFile)
        if not listing:
            continue

        # print output to console
        print(listing)

        # write the output to the same listing file we read from
        writeToListingFile(listing, pathToListingFile)


if __name__ == "__main__":
    main()
