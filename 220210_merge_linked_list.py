class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution:
    def merge_two_sorted_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None) # 做一個歸零點，才有辦法去算記憶體位置
        previous = dummy # 一開始指標先指向零點
        while l1 and l2: # 當兩個list都還有值的時候，就是互相比較
            if l1.value < l2.value:
                previous.next = l1
                l1 = l1.next
            else:
                previous.next = l2
                l2 = l2.next
            previous.next = l1 or l2 # 其中一方沒值了，那就把有值的那一方直接接上去。
        return dummy.next # 如果連任其中一方都沒值了，那就做完了，可以回傳




"""
https://leetcode-cn.com/problems/merge-two-sorted-lists/

21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：
输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0] 

提示：
两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列
"""