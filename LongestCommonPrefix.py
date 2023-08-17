# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution:
    @staticmethod
    def longestCommonPrefix(strs) -> str:
        prefix=""

        v=sorted(strs)
        first=v[0]
        last=v[-1]

        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return prefix
            prefix+=first[i]
        return prefix 
    

arr = ["apple", "application", "apprentice"]   
    
print(Solution.longestCommonPrefix(arr))
