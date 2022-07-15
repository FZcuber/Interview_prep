# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freq = {}
#         result = []

#         for num in nums:
#             freq[num] = freq.get(num, 0) + 1

#         for i in range(k):
#             most_freq_num = max(freq, key=freq.get)
#             result.append(most_freq_num)
#             freq.pop(most_freq_num)

#         return result


def topKFrequent(nums, k):

    frequency = {}

    for num in nums:

        if num not in frequency:

            frequency[num] = 1

        else:

            frequency[num] = frequency[num] + 1

    print(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
    frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

    result = list(frequency.keys())[:k]

    return result


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
