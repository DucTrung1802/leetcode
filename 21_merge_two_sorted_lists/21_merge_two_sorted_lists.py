class Solution:
    def mergeTwoLists(self, list1: list, list2: list) -> list:
        
        output = []

        left = 0
        right = 0

        for i in range(len(list1) + len(list2)):
            if left < len(list1) and list1[left] <= list2[right]:
                output.append(list1[left])
                left += 1
            else:
                output.append(list2[right])
                right += 1
            
        return output

mysolution = Solution()
print(mysolution.mergeTwoLists([1,2,4], [1,3,4]))

