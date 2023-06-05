class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)  # converte o número em uma string
        rx = x[::-1]  # inverte a string
        if x == rx:
            return True
        else:
            return False