import os

INPUT_NAME = "19. Remove Nth Node From End of List"


def main():
    output = INPUT_NAME.lower().replace(" ", "_").replace(".", "")
    os.makedirs(output)
    os.chdir(output)
    file = open(output + ".py", "a")


if __name__ == "__main__":
    main()
