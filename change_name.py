import os
from enum import Enum


class LEETCODE_TOPIC(Enum):
    ALGORITHMS = "algorithms"
    DATABASE = "database"
    SHELL = "shell"
    CONCURRENCY = "concurrency"
    JAVASCRIPT = "javascript"
    PANDAS = "pandas"


name = "271. Encode and Decode Strings"
topic = LEETCODE_TOPIC.ALGORITHMS
extension = "py"


def main():
    folder_name = topic.value
    file_name = name.lower().replace(" ", "_").replace(".", "")
    output_folder = f"{folder_name}/{file_name}"
    output_file = f"{output_folder}/{file_name}.{extension}"
    os.makedirs(output_folder, exist_ok=True)
    file = open(output_file, "a")


if __name__ == "__main__":
    main()
