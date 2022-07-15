class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for val in strs:
            lis = [0] * 26
            for char in val:
                lis[ord(char) - ord("a")] += 1

            dic[tuple(lis)].append(val)

        return dic.values()
