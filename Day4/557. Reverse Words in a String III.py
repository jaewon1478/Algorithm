class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split(" ")
        result = ""
        for word in temp:
            word = word[::-1] #It means that I would like to get each string "reverse"
            result += word + " "
        return result[:-1]