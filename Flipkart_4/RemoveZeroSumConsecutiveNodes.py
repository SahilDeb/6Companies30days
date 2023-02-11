class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeZeroSumSublists(head):
    dummy = ListNode(0)
    valueDict = {0: dummy}
    dummy.next = head

    curr = head
    currSum = 0
    while curr:
        currSum += curr.val
        valueDict[currSum] = curr
        curr = curr.next

    curr = dummy
    currSum = 0
    # Go from the dummy node again to set the next node to be the last node for a prefix sum
    while curr:
        currSum += curr.val
        curr.next = valueDict[currSum].next
        curr = curr.next

    return dummy.next
