#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, new_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            new_node (Node): The next node of the new Node.
        """
        self.data = data
        self.new_node = new_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def new_node(self):
        """Get/set the new_node of the Node."""
        return (self.__new_node)

    @new_node.setter
    def new_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("new_node must be a Node object")
        self.__new_node = value


class SinglyLinkedList:
    """ Define a singly-linked list. """

    def __init__(self):
        """Initalize new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        Args:
            value (Node): The new Node to insert.
        """
        if self.__head is None:
            node = Node(value, self.__head)
            self.__head = node
            return

        node = Node(value)
        current = self.__head

        if (current.data > value):
            node.new_node = self.__head
            self.__head = node
            return

        while current.new_node is not None:
            if current.new_node.data < value:
                current = current.new_node
            else:
                break

        if current.new_node is None:
            current.new_node = node
        else:
            new_node = current.new_node
            current.new_node = node
            node.new_node = new_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        current = self.__head
        values = []
        while current is not None:
            values.append(str(current.data))
            current = current.new_node
        return '\n'.join(values)