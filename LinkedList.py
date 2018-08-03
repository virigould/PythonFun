class LinkedList:

    def __init__(self):
        self.front = ListNode(None, None)
        self.__size = 0

    def add(self, data):

        if self.__size is 0:
            self.front = ListNode(data, None)
            self.__size += 1
            return True
        elif data is None:
            raise ValueError
        else:
            temp = self.front
            for i in range(0, self.__size - 1):
                temp = temp.nxt
            temp.nxt = ListNode(data, None)
            self.__size += 1
            return True

    def remove(self, index):
        temp = self.front
        if index > self.__size or index < 0:
            raise ValueError
        elif index is 0:
            self.front = self.front.nxt
            self.__size -= 1
        else:
            for i in range(0, self.__size - 1):
                temp = temp.nxt
            temp.nxt = temp.nxt.next
            self.__size -= 1

    def get(self, index):
        temp = self.front
        if index > self.__size or index < 0:
            raise ValueError
        else:
            for i in range(0, index):
                temp = temp.nxt
            return temp.data

    def get_index_of(self, obj):
        temp = self.front
        count = 0
        if temp.data == obj:
            return count
        else:
            for i in range(0, self.__size):
                if temp.data == obj:
                    return count
                else:
                    temp = temp.nxt
                    count += 1

    def size(self):
        return self.__size


class ListNode:
    def __init__(self, data, nxt):
        self.data = data
        if nxt is not None:
            self.nxt = nxt
        else:
            self.nxt = None

