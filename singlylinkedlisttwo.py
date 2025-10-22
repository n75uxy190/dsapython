class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        nodes = []
        current = self
        while current:
            nodes.append(current.data)
            current = current.next
        return repr(nodes)
    
class singlyLinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data: int) -> None:
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

if __name__ == "__main__":
    sll = singlyLinkedList()
    sll.push(3)
    sll.push(5)
    sll.push(7)
    print(sll.head)


    

