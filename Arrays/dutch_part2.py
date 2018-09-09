RED, WHITE, BLUE = range(3)

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]

    smaller, equal, larger = 0, 0, len(A)-1
    while(smaller <= larger):
        if A[equal] < pivot:
            A[equal], A[smaller] =A[smaller], A[equal]
            smaller += 1
            equal += 1
        elif A[equal] > pivot:
            A[equal], A[larger] =A[larger], A[equal]
            larger -= 1
        else:
            equal += 1
'''
time: O(n)
space: O(1)