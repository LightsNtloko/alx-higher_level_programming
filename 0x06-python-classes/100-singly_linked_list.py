#!/usr/bin/python3
"""Defines a Node class and a SinglyLinkedList class."""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node instance.

        Args:
            data (int): The data for the node.
            next_node (Node, optional): The next node in the list. Defaults to
            None.

        Raises:
            TypeError: If data is not an integer or next_node is not a Node or
            None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node with validation.

        Args:
            value (int): The new data for the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node of the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node of the list with validation.

        Args:
            value (Node, None): The new next node in the list.

        Raises:
            TypeError: If value is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the list while maintaining sorted order.

        Args:
            value (int): The data for the new node.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return a string representation of the list."""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
