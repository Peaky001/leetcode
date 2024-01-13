class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)

        result = sum((count_s - count_t).values())

        return result