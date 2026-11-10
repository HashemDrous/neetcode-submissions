class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = dict.fromkeys('abcdefghijklmnopqrstuvwxyz', 0)
        counter_t = dict.fromkeys('abcdefghijklmnopqrstuvwxyz', 0)

        for char in s:
            counter_s[char] += 1

        for char in t:
            counter_t[char] += 1

        if counter_s == counter_t:
            return True
            
        return False 
        
        