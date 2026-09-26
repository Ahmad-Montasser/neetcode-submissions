class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = [-1]*95
        longest_sub = 0
        curr_longest = 0
        for i,c in enumerate(s):
            intc = ord(c) - ord(" ")
            curr_longest += 1
            if char_index[intc] != -1 and char_index[intc] > i - curr_longest:
                curr_longest = i - char_index[intc] + 1
            longest_sub = max(longest_sub,curr_longest)
            char_index[intc] = i + 1
        return longest_sub