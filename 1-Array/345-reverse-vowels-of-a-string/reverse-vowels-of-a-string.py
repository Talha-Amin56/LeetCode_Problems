class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"  # Include both uppercase and lowercase vowels
        s = list(s)  # Convert the string to a list for mutability
        l, r = 0, len(s) - 1

        while l < r:  # Ensure pointers do not cross
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]  # Swap the vowels
                l += 1
                r -= 1
            if s[l] not in vowels:
                l += 1  # Move left pointer to the right
            if s[r] not in vowels:
                r -= 1  # Move right pointer to the left

        return ''.join(s)  # Convert the list back to a string
