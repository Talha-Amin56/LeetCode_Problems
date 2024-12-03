class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"  # Include both uppercase and lowercase vowels
        result = list(s)  # Use a temporary list to construct the result
        l, r = 0, len(s) - 1

        while l < r:
            # Skip non-vowel characters
            while l < r and s[l] not in vowels:
                l += 1
            while l < r and s[r] not in vowels:
                r -= 1
            # Swap vowels in the result array
            if l < r:
                result[l], result[r] = s[r], s[l]
                l += 1
                r -= 1

        return ''.join(result)  # Final result
