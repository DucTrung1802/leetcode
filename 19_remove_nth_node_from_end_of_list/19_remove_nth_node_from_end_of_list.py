# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None

        current_node = head
        node_list: list[ListNode] = [current_node]
        sz = 1

        while current_node.next:
            current_node = current_node.next
            node_list.append(current_node)
            sz += 1

        if sz == 1 and n == 1:
            return None

        if 0 < n <= sz:
            # Deleting node is head
            if node_list[0] == node_list[-n]:
                return node_list[-n + 1]
            # Deleting node is tail
            elif n == 1:
                node_list[-2].next = None
            # Other cases
            else:
                node_list[-n - 1].next = node_list[-n + 1]

        return head


# hello = Solution()
# hello.removeNthFromEnd(
#     ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2
# )
# hello.removeNthFromEnd(ListNode(1, ListNode(2, None)), 2)
