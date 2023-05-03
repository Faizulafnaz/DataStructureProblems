class MinHeap:
    def __init__(self, capacity = 10):
        self.arr= []
        self.size = 0
        self.capacity = capacity

    def get_parent_index(self, index):
        return (index-1)//2

    def get_left_child_index(self, index):
        return 2 * index + 1

    def get_right_child_index(self, index):
        return 2 * index +2

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    def get_parent_value(self, index):
        return self.arr[self.get_parent_index(index)]

    def get_left_child_value(self, index):
        return self.arr[self.get_left_child_index(index)]

    def get_right_child_value(self, index):
        return self.arr[self.get_right_child_index(index)]

    def swap(self, index1, index2):
        self.arr[index1], self.arr[index2] = self.arr[index2], self.arr[index1]

    def is_full(self):
        return self.size == self.capacity

    def insertion(self, data):
        if self.is_full():
            print("heap is full")
            return
        self.arr.append(data)
        self.size += 1
        self.heapify_up(self.size-1)

    def heapify_up(self,index):

        if self.has_parent(index) and self.arr[index] > self.get_parent_value(index):
            self.swap(index, self.get_parent_index(index))
            self.heapify_up(self.get_parent_index(index))

    def deletion(self):

        if len(self.arr) < 0:
            print("it's an empty list")
            return
        temp = self.arr[0]
        self.arr[0] = self.arr.pop()
        self.size -= 1
        self.heapify_down(0)
        return temp


    def heapify_down(self, index):
        smallest = index
        if self.has_right_child(index) and self.arr[smallest] < self.get_right_child_value(index):
            smallest = self.get_right_child_index(index)
        if self.has_left_child(index) and self.arr[smallest] < self.get_left_child_value(index):
            smallest = self.get_left_child_index(index)

        if smallest != index:
            self.swap(smallest, index)
            self.heapify_down(smallest)


obj = MinHeap()
lst = [34, 23, 4, 35, 23, 2, 3]
for i in lst:
    obj.insertion(i)

obj.deletion()
print(obj.arr)
