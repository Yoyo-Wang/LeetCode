from __future__ import print_function
import heapq


def merge(arrays):
    """
    input: int[][] arrayOfArrays
    return: int[]
    """
    # write your solution here
    # corner case
    if not arrays:
        return None
    heap = []
    for i in xrange(len(arrays)):
        if len(arrays[i]):
            heap.append((arrays[i][0], i, 0))
    heapq.heapify(heap)
    res = []

    while heap:
        val, index_array, index_element = heapq.heappop(heap)
        res.append(val)
        if index_element + 1 < len(arrays[index_array]):
            heapq.heappush(heap, (arrays[index_array][index_element + 1], index_array, index_element + 1))

    return res

input = [[],[1,5,7],[4], [2, 3, 5, 11], [2, 4, 4, 6, 8]]

res = merge(input)
print('res equal to %s'%res)