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

def generateLinkedList(nums: list[int]) -> Node:
    head = Node(0)
    current = head

    for i, num in enumerate(nums):
        #print(num, end=" -> ")
        current.next = Node(num) if current else 0
        current = current.next if current else None
    #print()

    return head.next

def addLikeDigits(headOne: Node, headTwo: Node) -> Node:
    dummy = Node(0)
    current = dummy
    carry = 0

    while headOne or headTwo or carry:
        valueOne = headOne.data if headOne else 0
        valueTwo = headTwo.data if headTwo else 0

        total = valueOne + valueTwo + carry
        digit = total % 10
        carry = total // 10

        current.next = Node(digit)
        current = current.next

        headOne = headOne.next if headOne else None
        headTwo = headTwo.next if headTwo else None

        print(current)
    
    return dummy.next

    

if __name__ == "__main__":
    print("hi")
    print(generateLinkedList([1, 2, 3]))
    listOne = generateLinkedList([1, 2, 3])
    listTwo = generateLinkedList([3, 5, 8])

    print(addLikeDigits(listOne, listTwo))
