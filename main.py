def BuzzwordOmitter(buzzwords: list[str], stringToRemoveFrom: str) -> str:
def BuzzwordOmitter():
    print("testing")
    res = stringToRemoveFrom
    for buzzword in buzzwords:
        res = res.replace(buzzword + " ", "REDACTED ")

    return res


"""
Driver method
"""


def main():
    flag = True
    words: list[str] = []
    listing: str

    while flag:
        pathToWordsFile = input(
            "Give me a path to the words file, or type 'quit' to exit: "
        )
        if pathToWordsFile == "quit":
            flag = False
            continue
        try:
            with open(pathToWordsFile) as f:
                for line in f:
                    words.append(line.strip("\n").strip())
            # once we have our words, we can move onto reading the second file
            pathToListingFile = input(
                "Please provide a path to the listing text file, or type 'quit to exit: "
            )
            if pathToListingFile == "quit":
                flag = False
                continue
            try:
                with open(pathToListingFile) as f2:
                    lines = f2.readlines()
                    listing = "".join([line.lower() for line in lines])
                    cleanedStr = BuzzwordOmitter(words, listing)

    print("main")
                print("Cleaned String: ", cleanedStr)

            except FileNotFoundError as e:
                print("ERROR: Please provide a valid path to a listing file.")
                print(e)

        except FileNotFoundError as e:
            print("ERROR: Please provide a valid path to a words file.")
            print(e)

    BuzzwordOmitter()


if __name__ == "__main__":
    main()
