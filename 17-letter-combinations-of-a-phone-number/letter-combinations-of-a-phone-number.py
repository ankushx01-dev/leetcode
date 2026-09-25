class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        def solve(index,subset,result):
            if index>=len(digits):
                result.append("".join(subset))
                return
            for ch in digits_to_letters[digits[index]]:
                subset.append(ch)
                solve(index+1,subset,result)
                subset.pop()
        digits_to_letters = {
            "2": "abc",
            "3": "def", 
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result=[]
        solve(0,[],result)
        return result
