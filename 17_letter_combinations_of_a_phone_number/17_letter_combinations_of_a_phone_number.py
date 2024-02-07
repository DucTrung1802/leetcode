class Solution:
    my_dictionary = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def letterCombinations(self, digits: str) -> list[str]:
        return self.recursion(digits, [])

    def recursion(self, digits: str, current_list: list[str]):
        if len(digits) > 0:

            new_list = []

            if len(current_list) == 0:
                for item in self.my_dictionary[digits[0]]:
                    new_list.append(item)

            else:
                for item in self.my_dictionary[digits[0]]:
                    temp_list = current_list.copy()
                    for i in range(len(temp_list)):
                        temp_list[i] += item
                    new_list.extend(temp_list)

            if len(digits[1:]) > 0:
                return self.recursion(digits[1:], new_list)

            return new_list

        return []


# hello = Solution()
# print(hello.letterCombinations("344"))
