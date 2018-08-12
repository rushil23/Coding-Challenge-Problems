class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        N=n=len(s)
        if (n==0 or n==1): return s
        if (s==s[::-1]): return s
        
        for i in range(n-1,0,-1):
            start = 0
            end = i-1
            while (end < N):
                x=s[start:(end+1)] #Substring
                if x==x[::-1]:
                    return x
                start+=1
                end+=1
        
        
        
