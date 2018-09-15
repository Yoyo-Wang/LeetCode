class Solution(object):
    def deDup(self, input):
        """
        input: string input
        return: string
        """
        # write your solution here
        # corner case
        if not input:
            return input
        arr = list(input)
        pre = 0
        cur = 1
        res = ""
        while cur < len(arr):
            if arr[cur] == arr[pre]:
                while cur < len(arr) and arr[cur] == arr[pre]:
                    cur += 1
                pre = cur
                cur = cur + 1
            else:
                res += arr[pre]
                pre += 1
                cur += 1
        if pre < len(arr):
            res += arr[pre]

        return res