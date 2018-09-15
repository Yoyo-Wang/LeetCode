class Solution(object):
    def subSets(self, set):
        """
        input : String set
        return : String[]
        """
        # write your solution here
        res = []
        cur_list = []
        arr = list(set)
        self.helper(res, cur_list, 0, arr)
        return res

    def helper(self, res, cur_list, index, arr):
        if index == len(arr):
            res.append("".join(cur_list))
            return

        self.helper(res, cur_list, index + 1, arr)
        cur_list.append(arr[index])
        self.helper(res, cur_list, index + 1, arr)
        cur_list.pop()


a = Solution()
res = a.subSets("abc")
print res