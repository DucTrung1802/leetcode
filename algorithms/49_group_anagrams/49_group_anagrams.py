from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}
        for i in strs:
            key = tuple(sorted(i))
            if key in buckets:
                buckets[key].append(i)
            else:
                buckets[key] = [i]
        return list(buckets.values())


hello = Solution()
print(hello.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
