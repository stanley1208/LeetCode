class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                print(mp)
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans

sol=Solution().lengthOfLongestSubstring("abc")
print(sol)