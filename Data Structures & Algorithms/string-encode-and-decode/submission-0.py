
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the separator
            while s[j] != "#":
                j += 1

            # Read the length of the string
            length = int(s[i:j])

            # Extract exactly that many characters
            start = j + 1
            end = start + length
            result.append(s[start:end])

            # Move to the next encoded string
            i = end

        return result
