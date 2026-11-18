class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sLetterCount = {}
        tLetterCount = {}

        for char in s:
            sLetterCount[char] = sLetterCount.get(char, 0) + 1


        for char in t:
            tLetterCount[char] = tLetterCount.get(char, 0) + 1
            
        if sLetterCount == tLetterCount:
            return True
        else:
            return False