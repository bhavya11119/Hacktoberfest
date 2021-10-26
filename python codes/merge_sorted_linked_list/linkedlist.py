"""
Given two sorted linked lists, merge them so that the resulting linked list is also sorted.
"""
from typing import NewType

NodeType = NewType("Node", object)


class Node:

    data: int or None
    next: NodeType or None

    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkedList(object):
    """
    singly linked list implementation
    """

    head: Node or None

    def __init__(self):
        self.head = None

    def create_from_list(self, input_list: list) -> None:
        assert self.head is None
        if len(input_list) < 1:
            return
        for item in input_list:
            self.insert_at_end(item)

    def insert_at_beginning(self, data):
        tmp = Node(data)
        if self.head is None:
            self.head = tmp
        else:
            tmp.next = self.head
            self.head = tmp

    def insert_at_end(self, data):
        tmp = Node(data)
        if self.head is None:
            self.head = tmp
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = tmp

    def pop_front(self) -> int:
        assert self.head is not None
        temp = self.head
        self.head = temp.next
        return temp.data

    def create_list(self) -> list[int]:
        output = []
        temp = self.head
        while temp is not None:
            output.append(temp.data)
            temp = temp.next
        return output

    def __repr__(self):
        start = "{head}"
        arrow = "->"
        end = "{None}"
        output_str = start + arrow
        temp = self.head
        while temp is not None:
            if temp.data is None:
                data = "??"
            else:
                data = temp.data
            output_str += "{{{}}}".format(data)
            output_str += arrow
            temp = temp.next
        output_str += end
        return output_str


def merge_sorted(list1: SingleLinkedList, list2: SingleLinkedList) -> SingleLinkedList:
    output = SingleLinkedList()

    last_added = None
    # while either list has another item iterate over them
    # then check if one has an item while the other does not, then append that item
    # and increment that list's head
    while list1.head is not None or list2.head is not None:
        if list1.head is not None and list2.head is not None:
            # identify least element, add it to the output list
            # don't assume that you can add the other element after it
            if list1.head.data < list2.head.data:
                # list2 will be consumed first if the heads are the same
                last_added = list1.head
                list1.head = last_added.next
            else:
                last_added = list2.head
                list2.head = last_added.next
            # having 'plucked' a node, remove it's reference to the next
            last_added.next = None
        elif list1.head is None:
            last_added = list2.head
            list2.head = last_added.next
            last_added.next = None
        elif list2.head is None:
            last_added = list1.head
            list1.head = last_added.next
            last_added.next = None
        # now add last_added to the end of the output SLL
        if output.head is None:
            output.head = last_added
        else:
            temp = output.head
            while temp.next is not None:
                temp = temp.next
            temp.next = last_added

    return output


def main():
    list1 = list(range(1, 10, 2))
    print(f"List 1: {list1}")
    list2 = list(range(2, 10, 2))
    print(f"List 2: {list2}")
    list3 = list1 + list2
    list3.sort()
    print(f"List 3 is List 1 added to List 2 and sorted: {list3}")
    list4 = list(range(1, 10, 1))
    assert list3 == list4

    sll1 = SingleLinkedList()
    sll1.create_from_list(list1)
    print(f"LinkedList 1: {sll1}")
    
    sll2 = SingleLinkedList()
    sll2.create_from_list(list2)
    print(f"LinkedList 2: {sll2}")
    
    merged_sll = merge_sorted(sll1, sll2)
    print(f"The merged SLL is LL1 merged with LL2: {merged_sll}")
    merged_list = merged_sll.create_list()
    assert merged_list == list4


if __name__ == "__main__":
    # at the recommendation of [https://youtu.be/g_wlZ9IhbTs](James Murphy, mcoding.io) to avoid polluting global scope
    main()
