class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result=''
        for i in range(0,len(s),2*k):
            tmp=s[i:i+k]
            tmp=tmp[::-1]+s[i+k:i+2*k]
            result=result+tmp
        return result
