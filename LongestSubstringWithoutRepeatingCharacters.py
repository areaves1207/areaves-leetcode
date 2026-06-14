class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s) == 1):
            return 1

        hash = defaultdict(int)
        for i in range(len(s)):
            idx = i
            temp_hash = defaultdict(int)
            while(idx < len(s)):
                temp_hash[s[idx]] += 1
                if temp_hash[s[idx]] > 1:
                    break

                if len(temp_hash) > len(hash):
                    hash = temp_hash
                    
                idx += 1
        return len(hash)
            

            
        
