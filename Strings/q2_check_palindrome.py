# Given a string s, return true if the string is a palindrome. Otherwise, return false.

# A string is considered a palindrome if it reads the same forwards and backwards.

class Solution:
    def isPalindrome(self, s):
        # code here
        # n = len(s)
        # for i in range(n//2):
        #     if s[i] != s[n-i-1]:
        #         return False
        # return True
        
        return s == s[::-1]
