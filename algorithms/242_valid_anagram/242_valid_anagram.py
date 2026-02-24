class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char = set(s)

        if set(s) != set(t):
            return False

        for c in char:
            if s.count(c) != t.count(c):
                return False

        return True


hello = Solution()
print(hello.isAnagram("anagram", "nagaram"))
