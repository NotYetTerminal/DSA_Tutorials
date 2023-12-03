
class Heap:

    values: list = [0]
    last_index: int = 0

    # increases the values size to the new array size
    def increase_array_size(self, new_array_size: int) -> None:
        for index in range(len(self.values), new_array_size):
            self.values.append(0)
    
    # up heaps value in given index
    def up_heap(self, x: int):
        parent_index = self.find_parent(x)
        while (parent_index != 0 and self.values[x] > self.values[parent_index]):
            # swapping values
            self.values[parent_index], self.values[x] = self.values[x], self.values[parent_index]
    
    # increases array size then inserts the new value, and up heaps
    def insert(self, x: int) -> None:
        self.last_index += 1
        if self.last_index >= len(self.values):
            self.increase_array_size((len(self.values) * 2))
        self.values[self.last_index] = x
        self.up_heap(self.last_index)
    
    # parent at floor division 2 of index given
    def find_parent(self, x: int) -> int:
        return x // 2

    # returns the left and right child indexes
    def find_child(self, x: int) -> tuple:
        return (x * 2, (x * 2) + 1)
    
    # finds smallest value, swaps with last value and up heaps
    def delete_small(self) -> None:
        starting_index: int = self.find_parent(self.last_index) + 1
        smallest_value: int = self.values[starting_index]
        smallest_value_index: int = starting_index

        # loops through all leaf nodes
        for index in range(starting_index + 1, self.last_index):
            if (self.values[index] < smallest_value):
                smallest_value = self.values[index]
                smallest_value_index = index

        # swapping values
        self.values[smallest_value_index], self.values[self.last_index] = self.values[self.last_index], self.values[smallest_value_index]

        # delete value
        self.values[self.last_index] = 0
        self.last_index -= 1

        self.up_heap(smallest_value_index)


def main():
    heap: Heap = Heap()
    heap.insert(30)
    heap.insert(20)
    heap.insert(5)
    heap.insert(15)
    heap.insert(16)
    heap.insert(4)
    heap.insert(2)
    heap.insert(10)
    heap.insert(11)
    print(heap.values)
    heap.delete_small()
    print(heap.values)
    pass


if __name__ == "__main__":
    main()