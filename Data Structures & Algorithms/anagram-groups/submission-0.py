class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        HashMap = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in HashMap:
                HashMap[key] = []
            HashMap[key].append(s)
        return list(HashMap.values())

        