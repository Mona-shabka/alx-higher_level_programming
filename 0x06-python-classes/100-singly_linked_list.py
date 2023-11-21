#!/usr/bin/python3
"""singly linked list module"""


class Node:
    """"defines linked list"""

    def __init__(self, data, next_node=None):
        """node."""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ attribute"""

        return (self.__data)

    @data.setter
    def data(self, value):
        """data attribute"""

        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """next_node attribute
        Returns: next node
        """

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """next node value"""

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


class SinglyLinkedList:
    """singly linked list"""

    def __init__(self):
        """singly linked list"""

        self.head = None

    def __str__(self):
        """list"""

        printsll = ""
        location = self.head
        while location:
            printsll += str(location.data) + "\n"
            location = location.next_node
        return printsll[:-1]

    def sorted_insert(self, value):
        """sorted module
        Args:
            value: node value.
        """
        n_new = Node(value)
        if not self.head:
            self.head = n_new
            return
        if value < self.head.data:
            n_new.next_node = self.head
            self.head = n_new
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            n_new.next_node = location.next_node
        location.next_node = n_new
