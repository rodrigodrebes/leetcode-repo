class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        s_map={}
        t_map={}

        for i in range(0, len(s)):
            s_ch = s[i]
            t_ch = t[i]

            if s_ch not in s_map:
                s_map[s_ch] = t_ch
            
            if t_ch not in t_map:
                t_map[t_ch] = s_ch

            if t_map[t_ch] != s_ch or s_map[s_ch] != t_ch:
                return False
            
        return True
          