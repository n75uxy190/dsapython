# implement a singly-linked list w/ some functionality:
#   findLowestValue, traverseAndPrint

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findLowestValue(head: Node) -> int:
    minValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data

        currentNode = currentNode.next
    return minValue


def traverseAndPrint(head: Node) -> None:
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" ->")
        currentNode = currentNode.next
    print("null")

node1 = Node(7)
node2 = Node(44)
node3 = Node(3)
node5 = Node(7)

node1.next = node2
node2.next = node3
node3.next = node5


if __name__ == "__main__":
    traverseAndPrint(node1)
    print(findLowestValue(node1))
    
    