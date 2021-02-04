from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):  # Complexidade -> O[N]
        if self.head:
            # inserção quando a lista já possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            # primeira inserção
            self.head = Node(elem)
        self._size += 1

    def __len__(self):  # Complexidade -> O[1]
        """Restorna o tamanho da lista"""
        return self._size

    def __getitem__(self, index):  # Complexidade -> O[N]
        # a = lista[6]
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range")

    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    def __setitem__(self, index, elem):  # Complexidade -> O[N]
        #  lista[5] = 6
        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")

    def index(self, elem):  # Complexidade -> O[N]
        """Retorna o índice do elemento da lista"""
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError("{} is not in  list".format(elem))

    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1


if __name__ == '__main__':

    list = LinkedList()

    list.append(7)
    list.append(80)
    list.append(56)
    list.append(32)
    list.append(17)