class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        frequency1 = {}
        frequency2 = {}

        for character in s:
            if character in frequency1:
                frequency1[character] += 1
            else:
                frequency1[character] = 1

        for character in t:
            if character in frequency2:
                frequency2[character] += 1
            else:
                frequency2[character] = 1

        for key in frequency1:
            if key not in frequency2 or frequency1[key] != frequency2[key]:
                return False  
              
        return True