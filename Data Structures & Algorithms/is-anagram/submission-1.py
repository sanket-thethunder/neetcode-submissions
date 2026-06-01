class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        v= sorted(s)
        w= sorted(t)
        if v==w:
            return True
        else:
            return False

        