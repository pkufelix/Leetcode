"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
    """
    This method check each sub-arrary with the length of len(p), O(m*n)
    """
        res = []
        d = self.createDict(p)
        change = False
        i = 0
        pivot = 0
        while i < len(s):
            c = s[i]
            if c in d:
                change = True        
                d[c] -= 1
                i += 1
                if d[c] == 0:
                    d.pop(c)
                    if not bool(d):
                        res.append(pivot)
                        change = False
            else:
                change = False
            if change == False:
                pivot += 1
                i = pivot
                d = self.createDict(p)
        return res

    def findAnagrams(self, s: str, p: str) -> List[int]:
    """
    This method uses a sliding window method, O(m)
    """
        res = []
        d = self.createDict(p)
        i = 0
        left = 0
        right = 0
        counter = len(d)
        while right < len(s):
            c = s[right]
            if c in d:
                d[c] -= 1
                if d[c] == 0:
                    counter -= 1
            right += 1
            while counter == 0:
                c = s[left]
                if c in d:
                    d[c] += 1
                    if d[c] > 0:
                        counter += 1
                if right - left == len(p):
                    res.append(left)
                left += 1
        return res
                
        
    def createDict(self, p: str):
        d = {}
        for i in p:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return d
    
        