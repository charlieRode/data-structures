#!/usr/bin/env python

class Node:
    def __init__(self, datum, pointer):
        self.datum= datum
        self.pointer= pointer

class Linked_List:
    def __init__(self):
        self.head= None

    def insert(self, value):
        self.head= Node(value, self.head)

    def pop(self):
        popped= self.head.datum
        self.head= self.head.pointer
        return popped

    def size(self):
        """Will count the number of non-None elements in the linked list"""
        head= self.head
        count= 0
        while self.head is not None:
            self.head= self.head.pointer
            count += 1
        self.head= head
        return count

    def search(self, value):
        head= self.head
        while self.head is not None:
            self.head= self.head.pointer
            try:    
                if self.head.datum== value:
                    result, self.head= self.head, head
                    break
            except AttributeError:
                self.head= head
                return None
        return result

    def remove(self, item):
        try:
            head= self.head
            if self.head.datum == item:
                self.head= self.head.pointer
            else:
                while self.head.pointer.datum != item:
                    self.head= self.head.pointer
                self.head.pointer= self.head.pointer.pointer
                self.head= head
        except AttributeError:
            raise ValueError("%s not in list" % str(item))

    def __str__(self):
        result= ()
        head= self.head
        while self.head is not None:
            result += (self.head.datum,)
            self.head= self.head.pointer
        self.head= head

        return str(result)


