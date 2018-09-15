class Solution(object):
    def reverse(self, input):
        """
        input: string input
        return: string
        """
        # write your solution here
        left = 0
        right = len(input)-1
        dic = set(['a', 'e', 'i', 'o', 'u'])
        arr = list(input)
        while left < right:
            while arr[left] not in dic and left < right:
                left += 1
            while arr[right] not in dic and left < right:
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        return ''.join(arr)
