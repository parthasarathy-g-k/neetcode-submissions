class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = defaultdict(int)
        for i in nums:
            dictionary[i] += 1

        dict1 = dict(
            sorted(dictionary.items(), key=lambda items : items[1], reverse = True))
        lis = []
        count = 0
        for i in dict1.keys():
            if count<k:
                lis.append(i)
                count+=1
        return lis
        