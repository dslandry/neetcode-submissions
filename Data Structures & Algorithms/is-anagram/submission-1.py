class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        occurences_s  = defaultdict(int)
        occurences_t  = defaultdict(int)

        for x in s:
            occurences_s[x]+=1
        for x in t:
            occurences_t[x]+=1
        return occurences_s==occurences_t
        