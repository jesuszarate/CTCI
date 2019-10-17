class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:


        pos = 0
        i = 0
        while i < len(abbr):
            if abbr[i].isdigit():
                tup = self.getDigit(i, abbr)
                pos = tup[0] + pos
                i = tup[1]
                continue

# if pos >= len(word) or i >= len(abbr) or abbr[i] != word[pos]:

            if abbr[i] != word[pos]:
                return False
            pos += 1
            i += 1
        return pos == len(word)

    def getDigit(self, i, abbr):
        dig = ''
        while i < len(abbr):
            if not abbr[i].isdigit():
                return int(dig), i
            dig += abbr[i]
            i += 1
        return int(dig), i


s = Solution()



word = "a"
abbr = "01"

print(s.validWordAbbreviation(word, abbr))