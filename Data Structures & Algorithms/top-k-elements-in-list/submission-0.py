class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        HashMap = {}
        for num in nums:
            if num not in HashMap:
                HashMap[num] = 1
            else:
                HashMap[num] += 1
        return sorted(HashMap, key = lambda x: HashMap[x], reverse=True)[:k]
