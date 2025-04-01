class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

class HeapBasedPriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, value, priority):
        self.heap.append(Node(value, priority))
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop().value

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root.value

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0].value

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest_index = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest_index]:
                smallest_index = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest_index]:
                smallest_index = right_child_index

            if smallest_index != index:
                self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
                index = smallest_index
            else:
                break

pq = HeapBasedPriorityQueue()
pq.push('n', 1)
pq.push('b', 4)
pq.push('c', 3)
pq.push('d', 2)
pq.push('e', 5)
pq.push('f', 6)
pq.push('hi', 0)

print("Peek:", pq.peek())



