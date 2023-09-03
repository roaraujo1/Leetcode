# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []
        
        while l1:
            list1.append(l1.val)
            l1 = l1.next
      
        
        while l2:
            list2.append(l2.val)
            l2 = l2.next
        
        str1 = ""
        for _ in range(len(list1)):
            str1+=str(list1.pop())
       
        
        str2 = ""
        for _ in range(len(list2)):
            str2+=str(list2.pop())
        
        res = int(str1) + int(str2)
        res = str(res)
       
        dummy = ListNode(-1)
        ptr = dummy
        for i in range(len(res)-1,-1,-1):
            newNode = ListNode(res[i])
            ptr.next = newNode
            ptr = ptr.next
        return dummy.next
            
            
            
        
            
            
            