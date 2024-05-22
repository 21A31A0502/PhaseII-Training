'''
#linkedlist
class Box:
    def __init__(self,data):
        self.data=data
        self.next=None 
def printLinkedList(curr):
    while curr != None:
        print(curr.data)
        curr = curr.next 

#obj cration is happening 
obj1=Box(51)        
obj2=Box(52)   
obj3=Box(53)   
obj4=Box(54)   
obj5=Box(55)   
 
#establishing links
obj1.next=obj2  
obj2.next=obj3

obj3.next=obj4
obj4.next=obj5
obj5.next=None


#printing address
print(obj1.next)
print(obj2.next)
print(obj3.next)

print(obj4.next)
print(obj5.next)

#printing data
print(obj1.data)
print(obj2.data)
print(obj3.data)
print(obj4.data)
print(obj5.data)
printLinkedList(obj1)
'''
'''
#insertion at tail
class Box:
    def __init__(self,data):
        self.data=data
        self.next=None 
def printLinkedList(curr):
    while curr != None:
        print(curr.data)
        curr = curr.next 
def insertAtTailNode(head,ele):
    temp=Box(ele)
    if head==None:
        return temp
    tail=head
    while tail.next != None:
        tail=tail.next 
    tail.next=temp
    return head 
head = None               
n=[12,10,23,45]
for ele in n:
    
    head=insertAtTailNode(head,ele)
printLinkedList(head)
'''
#insertion  at begining 

class Box:
    def __init__(self,data):
        self.data=data
        self.next=None 
def printLinkedList(curr):
    while curr != None:
        print(curr.data,end="->")
        curr = curr.next 
def insertAtBeginning(head,ele):
    temp=Box(ele)
    if head==None:
        return temp
    temp.next=head
    return temp       


def insertAtSpecificPosition(head, position, ele):
    if position == 0:
        return insertAtBeginning(head, ele)
 
    temp = Box(ele)
    currentIndex = 0 
    currentNode = head 
    while currentIndex != position - 1:
        currentIndex += 1 
        currentNode = currentNode.next 
 
    temp.next = currentNode.next 
    currentNode.next = temp 
    return head
head = None
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for ele in nums:
    head = insertAtBeginning(head, ele)
 
printLinkedList(head)
head = insertAtSpecificPosition(head, 5, 1899)
printLinkedList(head)
