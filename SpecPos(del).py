def deleteNodeAtSpecificPosition(head,position):
    if position==0:
        return deleteHeadNodeInLinkedList(head)
    currentIndex=0
    currentNode=head
    while currentIndex != position-1 :
        currentIndex +=1
        currentNode = currentNode.next
    nodeToBeDeleted = currentNode.next
    currentNode.next=nodeToBeDeleted.next
    nodeToBeDeleted.next = None
    return head

#https://pastebin.com/ykC4AyQA