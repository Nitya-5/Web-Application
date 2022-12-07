class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None


def insert(lis, data):
    m = Node(data)
    if lis.head == None:
        lis.head = m
    else:
        header = lis.head
        while header.next!=None:
            header=header.next
        header.next = m


def display(head):
    head1 = head
    print("Elements in list are", end=' ')
    while head1!=None:
        print(head1.data+'->',end='')
        head1 = head1.next
    print("NULL")


list1 = Linkedlist()
list2 = Linkedlist()
i = 0
n1 = 26
while i < n1:
    insert(list1, chr(97+i))
    i += 1
i = 0
print("Enter name : ")
s = input()
n2 = len(s)
while i < n2:
    insert(list2, s[i])
    i += 1
display(list2.head)
