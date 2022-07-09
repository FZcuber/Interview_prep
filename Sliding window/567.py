class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count1, count2 = {}, {}

        for i in range(len(s1)):
            count1[s1[i]] = count1.get(s1[i], 0) + 1
            count2[s2[i]] = count2.get(s2[i], 0) + 1

        def checkEqual(table1, table2):
            for char in table1:
                if char not in table2:
                    return False
                elif table1[char] != table2[char]:
                    return False

            return True

        if checkEqual(count1, count2):
            return True
        l = 0

        for r in range(len(s1), len(s2)):

            count2[s2[l]] -= 1
            l += 1

            count2[s2[r]] = count2.get(s2[r], 0) + 1

            if checkEqual(count1, count2):
                return True
        return False
