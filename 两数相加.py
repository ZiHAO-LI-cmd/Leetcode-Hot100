# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        num1 = 0
        num2 = 0
        while l1:
            num1 += l1.val * 10**n 
            n += 1
            l1 = l1.next
        n = 0
        while l2:
            num2 += l2.val * 10**n 
            n += 1
            l2 = l2.next
        s = num1 + num2
        L = []
        if s != 0:
            while s:
                L.append(ListNode(s%10))
                s = s // 10
            for i in range(len(L) - 1):
                L[i].next = L[i + 1]
            return L[0]
        else:
            return ListNode(0)



# https://leetcode-cn.com/problems/add-two-numbers/