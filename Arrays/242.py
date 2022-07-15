class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMap1, hashMap2 = [0] * 26, [0] * 26

        for char1, char2 in zip(s, t):
            hashMap1[ord(char1) - ord("a")] += 1
            hashMap2[ord(char2) - ord("a")] += 1

        print(hashMap1, hashMap2)
        return hashMap1 == hashMap2
