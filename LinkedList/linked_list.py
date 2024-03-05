class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    @staticmethod
    def empty():
        print("Linked List is empty")

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if not self.head:
            self.insert_at_beginning(data)
        node = self.head
        while node.next:
            node = node.next
        add_node = Node(data, None)
        node.next = add_node

    def insert_values(self, data):
        for val in data:
            self.insert_at_end(val)

    def insert_at(self, data, index):
        if index < 0 or index > self.length():
            raise Exception("InvalidIndex")
            return

        if index == 0:
            self.insert_at_beginning(data)

        count = 0
        node = self.head
        for i in range(0, index+1):
            if count == index-1:
                temp = node.next
                node_to_insert = Node(data, temp)
                node.next = node_to_insert
                return
            node = node.next
            count += 1

    def insert_after_val(self, data, val):
        if not self.head:
            self.empty()
            return

        node = self.head
        flag = False
        while node.next:
            if node.data == val:
                node_to_insert = Node(data, node.next)
                node.next = node_to_insert
                flag = True
                break
            node = node.next
        if flag == False:
            raise Exception("ValueNotFound")
            return

    def insert_before_val(self, data, val):
        if not self.head:
            self.empty()
            return

        node = self.head
        flag = False
        while node.next:
            temp = node.next
            if temp.data == val:
                node_to_insert = Node(data, temp)
                node.next = node_to_insert
                flag = True
                break
            node = node.next
        if flag == False:
            raise Exception("ValueNotFound")
            return

    def delete_at_beginning(self):
        if not self.head:
            self.empty()
            return
        node = self.head
        temp = node.next
        self.head = temp

    def delete_at_end(self):
        if not self.head:
            self.empty()
            return

        node = self.head
        while node.next:
            temp = node.next
            if not temp.next:
                node.next = None
                return
            node = node.next

    def delete_at(self, index):
        if not self.head:
            self.empty()
            return

        if index < 0 or index > self.length():
            raise Exception("InvalidIndex")
            return

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        node = self.head
        for i in range(0, index+1):
            if count == index-1:
                temp = node.next
                node.next = temp.next
                return
            node = node.next
            count += 1

    def delete_after_val(self, val):
        if not self.head:
            self.empty()
            return

        node = self.head
        flag = False
        while node.next:
            if node.data == val:
                temp = node.next
                node.next = temp.next
                flag = True
                break
            node = node.next
        if flag == False:
            raise Exception("ValueNotFound")
            return

    def delete_before_val(self, val):
        if not self.head:
            self.empty()
            return

        node = self.head
        flag = False
        while node.next:
            temp = node.next
            temp_1 = temp.next
            if temp_1.data == val:
                node.next = temp_1
                flag = True
                break
            if not temp_1.next:
                break
            node = node.next
        if flag == False:
            raise Exception("ValueNotFound")
            return

    def print(self):
        if not self.head:
            self.empty()
            return

        itr = self.head
        while itr:
            print(itr.data, end="-->")
            itr = itr.next
        print()

    def length(self):
        if not self.head:
            self.empty()
            return

        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def exist(self, val):
        if not self.head:
            self.empty()
            return

        node = self.head
        while node:
            if node.data == val:
                return True
            node = node.next
        return False


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(9)
    ll.insert_at_beginning(6)
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(0)
    ll.insert_at_end(12)
    ll.print()
    print(ll.length())
    ll.delete_at_beginning()
    ll.print()
    ll.insert_at_end(15)
    ll.insert_at_end(16)
    ll.print()
    print(ll.length())
    ll.delete_at_end()
    ll.print()
    print(ll.length())
    ll.insert_values([18,21,24,27,30])
    ll.print()
    ll.insert_at(33,0)
    ll.print()
    ll.insert_at(36,2)
    ll.print()
    ll.delete_at(0)
    ll.print()
    ll.delete_at(1)
    ll.print()
    ll.delete_at(5)
    ll.print()
    ll.delete_at(5)
    ll.print()
    ll.insert_after_val(18,15)
    ll.print()
    ll.insert_before_val(21,24)
    ll.print()
    ll.delete_before_val(30)
    ll.print()
    ll.delete_after_val(21)
    ll.print()
    ll.delete_at_end()
    ll.print()
    print(ll.exist(30))
    print(ll.exist(3))
    ll.insert_before_val(29, 30)
    ll.delete_before_val(29)
