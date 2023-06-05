from ast import Set
from math import floor


class Solution(object):
    def isHappy(self, n):
      seen = set()
      while n not in seen:
        seen.add(n)
        square_sum = 0
        while n > 0:
          square_sum += (n%10)*(n%10)
          n = floor(n/10)
        
        if square_sum ==1:
          return True
        
        n = square_sum
      return False