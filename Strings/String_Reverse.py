class Solution(object):
  def reverse(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    arr = list(input)
    arr.reverse()
#    return ''.join(arr)
    return ''.join(reversed(input)