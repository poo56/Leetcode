import heapq

class MedianFinder:

    def __init__(self):
        # Max-heap (for the lower half of the numbers)
        self.maxHeap = []  # This will store the negative values for max-heap behavior
        # Min-heap (for the upper half of the numbers)
        self.minHeap = []

    def addNum(self, x: int):  # Changed from insert to addNum
        # Insert into the max heap (invert the value to simulate max-heap)
        if not self.maxHeap or x <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -x)  # Push negative to simulate max-heap
        else:
            heapq.heappush(self.minHeap, x)

        # Balance the heaps
        self.balanceHeaps()

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            # If both heaps are of equal size, the median is the average of the tops
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        else:
            # If the heaps are unequal, the median is the top of the max heap
            return -self.maxHeap[0]

    def balanceHeaps(self):
        # If max heap has more than one extra element, move the root of max heap to min heap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        # If min heap has more elements, move the root of min heap to max heap
        elif len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

# Example usage
medianFinder = MedianFinder()
medianFinder.addNum(1)
print(medianFinder.findMedian())  # Output: 1.0
medianFinder.addNum(2)
print(medianFinder.findMedian())  # Output: 1.5
medianFinder.addNum(3)
print(medianFinder.findMedian())  # Output: 2.0