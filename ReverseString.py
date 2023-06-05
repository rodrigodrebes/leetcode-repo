#1
class Solution(object):
    def reverseString(self, s):
        return s.reverse()

#2
class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s) -1
        while left < right:
            temp = s[left]
            s[left] =  s[right]
            s[right] = temp
            left+=1
            right-=1