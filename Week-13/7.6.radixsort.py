from typing import List, Optional

class Node:
    def __init__(self, key):
        self.key = key
        self.link = None

        
def get_digit(key: int, digit_pos: int) -> int:
    # Complete the code here
    for i in range(digit_pos-1):
        key//=10
    return key%10


def distribute(masterlist: Optional[Node], digit_pos: int) -> List[Optional[Node]]:
    # Complete the code here
    p = masterlist
    digits = [None for _ in range(10)]
    while p:
        digit = get_digit(p.key,digit_pos)
        if digits[digit] is None:
            digits[digit] = p
        else:
            pp = digits[digit]
            while pp.link is not None:
                pp = pp.link
            pp.link = p
        l = p
        p=p.link
        l.link = None
    return digits

def coalesce(list_array: List[Optional[Node]]) -> Optional[Node]:
    # Complete the code 
    head = None
    tail = None
    for i in range(10):
        if list_array[i]:
            if head is None:
                head = tail = list_array[i]
            else:
                tail.link = list_array[i]
            while tail.link is not None:
                tail = tail.link
    return head

def radixsort(masterlist: Optional[Node], numdigits: int) -> Optional[Node]:
    for i in range(1, numdigits + 1):
        list_array = distribute(masterlist, i)
        masterlist = coalesce(list_array)
    return masterlist


def to_list(masterlist: Optional[Node]) -> List[int]:
    # Convert linked list to Python list
    result = []
    p = masterlist
    while p:
        result.append(p.key)
        p = p.link
    return result


def from_list(lst: List[int]) -> Optional[Node]:
    # Convert Python list to linked list
    head = None
    tail = None
    for key in lst:
        node = Node(key)
        if head is None:
            head = tail = node
        else:
            tail.link = node
            tail = node
    return head
