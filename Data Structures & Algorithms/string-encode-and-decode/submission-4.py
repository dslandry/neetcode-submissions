class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#"  + s
        return encoded


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i< len(s):
            j=i
            while s[j]!="#":
                j+=1
            next_str_length = int(s[i:j])
            i=j
            next_str = s[j+1: j+1+next_str_length]
            res.append(next_str)
            i+=1+next_str_length
        return res
