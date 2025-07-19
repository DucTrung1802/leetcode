import os

INPUT_NAME = "1757. Recyclable and Low Fat Products"
TYPE = "sql"


def main():
    output = INPUT_NAME.lower().replace(" ", "_").replace(".", "")
    os.makedirs(output)
    os.chdir(output)
    file = open(output + f".{TYPE.lower()}", "a")


if __name__ == "__main__":
    main()
