class Box:
    def __init__(self, data):
        self.data = data 
        self.next = None
 
def printLinkedList(curr):
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next 
def insertAtBeginning(head, ele):
    temp = Box(ele)
    if head == None:
        return temp 
    temp.next = head 
    return temp
def deleteTailNode(head,ele):
    curr=head
    if curr == None or curr.next == None:
        return None 
    while curr.next.next != None:
        curr=curr.next 
    curr.next=None
    return head    
def deleteHeadNode(head,ele):
    if head == None:
        return None 
    secondNode=head.next
    head.next=None
    return secondNode
    
def deleteNodeAtSpecific(head,position):
    if position==0:
        return deleteHeadNode(head)
    currentIndex=0
    currentNode=head
    while currentIndex != position - 1:
        currentIndex += 1
        currentNode=currentNode.next
    nodeTobeDeleted=currentNode.next
    currentNode.next=nodeTobeDeleted.next
    nodeTobeDeleted.next=None 
    return head         
head = None
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for ele in nums:
    head = insertAtBeginning(head, ele)
 
print(printLinkedList(head))
#head=deleteTailNode(head,ele)
#print(printLinkedList(head))
head=deleteTailNode(head,ele)
print(printLinkedList(head))
head=deleteHeadNode(head,ele)
print(printLinkedList(head))       
head=deleteNodeAtSpecific(head,5)
print(printLinkedList(head))