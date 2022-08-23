# This is not My Code


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        result = 0
        counter = Counter()

        l = 0
        for r, c in enumerate(s):
            counter[c] += 1
            while counter[c] > 1:
                counter[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)

        return result
