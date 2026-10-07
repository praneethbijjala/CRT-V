#876. Middle of the Linked List
# Definition for singly-linked list.

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
#solution 1:
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count=0
        temp=head
        while temp:
            count +=1
            temp = temp.next
        mid_ind = count // 2
        temp = head
        for i in range(mid_ind):
            temp = temp.next
        return temp

# solution 2 : slow and Fast pointer (Flyoid's cycle detection)

class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow




#141. Linked List Cycle
#solution 1:
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        temp= head
        while temp:
            if temp in visited:
                return True
            visited.add(temp)
            temp = temp.next
        return False

# Solution 2:
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

#21. Merge Two Sorted Lists
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        temp=ListNode()
        curr=temp
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next=list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr=curr.next
        if list1:
            curr.next=list1
        else:
            curr.next=list2
        return temp.next


#206. Reverse Linked List
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr=head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


        