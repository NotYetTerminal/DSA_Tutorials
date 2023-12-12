class Heap:
    # values is used as an array
    values: list = [0]
    # last_index is the position where the last value is
    last_index: int = 0

    # increases the values size to the new array size
    def increase_array_size(self, new_array_size: int) -> None:
        for index in range(len(self.values), new_array_size):
            self.values.append(0)

    # up heaps value in given index
    def up_heap(self, x: int):
        parent_index: int = self.find_parent(x)
        current_index: int = x
        while parent_index != 0 and self.values[current_index] > self.values[parent_index]:
            # swapping values
            self.values[parent_index], self.values[current_index] = (
                self.values[current_index],
                self.values[parent_index],
            )
            current_index = parent_index
            parent_index = self.find_parent(current_index)

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
        for index in range(starting_index + 1, self.last_index + 1):
            if self.values[index] < smallest_value:
                smallest_value = self.values[index]
                smallest_value_index = index

        # swapping values
        self.values[smallest_value_index], self.values[self.last_index] = (
            self.values[self.last_index],
            self.values[smallest_value_index],
        )

        # delete value
        self.values[self.last_index] = 0
        self.last_index -= 1

        self.up_heap(smallest_value_index)

    # prints the heap graphically
    def pretty_print_heap(self) -> None:
        print("INFO: The graphical print may break when there are many values in the heap, or the values are too big.")
        print_lines_list: list = []
        # keeps track of multiples of 2
        current_multiple: int = 1
        longest_number_length: int = 0
        counter: int = 1

        # organises values to print out
        for index in range(1, self.last_index + 1):
            if index == current_multiple:
                print_lines_list.append([" ", str(self.values[index])])
                current_multiple *= 2
                counter = counter * 2 + 1
            else:
                # add to last line
                print_lines_list[-1].append(" ")
                print_lines_list[-1].append(self.values[index])
            if longest_number_length < len(str(self.values[index])):
                longest_number_length = len(str(self.values[index]))

        counter //= 2
        other_counter: int = len(print_lines_list)
        for line in print_lines_list:
            # prints out markers whether each node is a left or right child
            if len(line) != 2:
                left: bool = True
                for index in range(len(line)):
                    if line[index] == " ":
                        if index == 0:
                            print(
                                " "
                                * (
                                    counter * longest_number_length
                                    - (2**other_counter)
                                ),
                                end="",
                            )
                        else:
                            print(" " * (counter * longest_number_length), end="")
                    else:
                        print(" " * (longest_number_length - 1), end="")
                        if left:
                            print("/", end="")
                        else:
                            print("\\", end="")
                        left = not left
                print()

            # prints out values
            for index in range(len(line)):
                if line[index] == " ":
                    if index == 0:
                        print(
                            " "
                            * (counter * longest_number_length - (2**other_counter)),
                            end="",
                        )
                    else:
                        print(" " * (counter * longest_number_length), end="")
                else:
                    print(" " * (longest_number_length - len(str(line[index]))), end="")
                    print(line[index], end="")
            print()
            counter //= 2
            other_counter -= 1

def initialise_sample_heap() -> Heap:
    heap: Heap = Heap()
    heap.values = [0, 82, 72, 40, 56, 61, 22, 30, 20, 15, 60, 35, 5, 19, 10, 2, 3, 15, 8, 11, 4, 13]
    heap.last_index = 21
    return heap


def main():
    heap: Heap =  initialise_sample_heap()
    print("Heap printed as an array:")
    print(heap.values[:heap.last_index + 1])
    print("Heap printed graphically:")
    heap.pretty_print_heap()

    while True:
        print()
        print("1 - Insert Number")
        print("2 - Find Parent of Index")
        print("3 - Find Children of Index")
        print("4 - Delete Smallest")
        print("5 - Print Heap")
        print("6 - Exit")

        input_number: str = input("Select an number: ")

        match input_number:
            case "1":
                number_in: str = input("Input number to insert: ")
                if number_in.isdigit():
                    heap.insert(int(number_in))
                    print("Number inserted.")
                else:
                    print("Not a number put in!")
            case "2":
                number_in: str = input("Input index to get parent: ")
                if number_in.isdigit():
                    print(f"Parent index: {heap.find_parent(int(number_in))}")
                else:
                    print("Not a number put in!")
            case "3":
                number_in: str = input("Input index to get children: ")
                if number_in.isdigit():
                    print(f"Children indexes: {heap.find_child(int(number_in))}")
                else:
                    print("Not a number put in!")
            case "4":
                heap.delete_small()
                print("Smallest deleted.")
            case "5":
                print("Heap printed as an array:")
                print(heap.values[:heap.last_index + 1])
                print("Heap printed graphically:")
                heap.pretty_print_heap()
            case "6":
                break
            case _:
                print("Input numbers 1 - 5!")


if __name__ == "__main__":
    main()
