# singly linkedlist
class Node:
    def __init__(self, data , next ):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def print(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + " -> "
            itr = itr.next
        print(llstr[:-4])

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count is index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            # newNode = Node(data, self.head)
            # self.head = newNode
            self.insert_at_begining(data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                newNode = Node(data, itr.next)
                itr.next = newNode
                break
            itr = itr.next
            count += 1
        
            
        
    
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(6)
    ll.insert_at_begining(10)
    ll.insert_at_end(4)
    ll.insert_at_begining(10)
    ll.insert_at_end(3)
    ll.print()
    print("\n")
    ll.insert_values(["banana", "apple", "grape", "orange"])
    ll.print()
    print(ll.get_length())
    ll.remove_at(2)
    ll.print()
    print("\n")
    # ll.remove_at(20)
    ll.insert_at(2, "grape")
    ll.insert_at(0, "jackfruit")
    ll.insert_at(4, "fig")
    ll.print()
