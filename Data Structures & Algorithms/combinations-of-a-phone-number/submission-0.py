class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        results = []

        if not digits:
            return []

        def backtrack(index, path):
            if index == len(digits):
                results.append("".join(path))
                return

            digit = digits[index]

            for letter in phone_map[digit]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return results


