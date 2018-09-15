class Solution(object):
    def longest(self, input):
        """
        input: string input
        return: int
        """
        left = 0
        right = 0

        window = set()
        res = 0
        cur = 0

        arr = list(input)
        while right < len(input):
            if arr[right] not in window:
                window.add(arr[right])
                cur += 1
                if cur > res:
                    res = cur
            else:
                while arr[right] in window:
                    window.remove(arr[left])
                    left += 1
                    cur -= 1
                window.add(arr[right])
                cur += 1
            right += 1
        return res

if __name__ == '__main__':
    cur = Solution()
    res = cur.longest("abcabcbbcda")
    print res