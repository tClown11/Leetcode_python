# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        cur = 1
        sum_r1, sum_r2 = 0, 0

        while l1:
            sum_r1 += l1.val*cur
            l1 = l1.next
            cur = cur*10

        cur = 1

        while l2:
            sum_r2 += l2.val*cur
            l2 = l2.next
            cur = cur*10

        sum = str(int(str(sum_r1)) + int(str(sum_r2)))[::-1]
        s = int(sum[0])
        res = ListNode(s)
        temp = res
        for i in sum[1::]:
            int(i)
            te=ListNode(i)
            temp.next=te
            temp=te
        return res
