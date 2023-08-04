class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None

        # Swap root with the last element
        self._swap(0, len(self.heap) - 1)

        # Pop the last element (min value)
        min_value = self.heap.pop()

        # Bubble down the root
        self._bubble_down(0)

        return min_value

    def _bubble_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2

            # Compare with parent and swap if needed
            if self.heap[parent_index] > self.heap[index]:
                self._swap(parent_index, index)
                index = parent_index
            else:
                break

    def _bubble_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            # Find the smallest child
            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index

            # Swap with the smallest child if needed
            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


if __name__ == "__main__":
    heap = MinHeap()

    # Insert elements
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    heap.insert(2)
    heap.insert(4)

    # Extract min (smallest element)
    print(heap.extract_min())  

    # Extract min again
    print(heap.extract_min())  
