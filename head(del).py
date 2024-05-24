def deleteHeadNodeInLinkedList(head):
    if head==None:
        return None
    secondNode=head.next
    head.next=None
    return secondNode