class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = set()
        left = 0
        right = 0
        max_length = 0
        while(right<len(s)):
            if s[right] not in a:
                a.add(s[right])
                max_length = max(max_length,len(a))
                right+=1
            else:
                a.remove(s[left])
                left+=1
        return max_length
       
                
        
        