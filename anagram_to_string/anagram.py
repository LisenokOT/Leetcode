class Solution(object):
    def isAnagram(self, s, t):
        leter='abcdefghijklmnopqrstuvwxyz'
        data_s = {elem: s.count(elem) for elem in leter if s.count(elem) > 0}
        data_t = {elem: t.count(elem) for elem in leter if t.count(elem) > 0}
        if data_s == data_t:
            return True
        return False
        
def main():
    stri = Solution()
    print(stri.isAnagram("anagram", "nagaram"))
    print(stri.isAnagram("racc", "car"))
    print(stri.isAnagram("rat", "car"))
    print(stri.isAnagram("e", "e"))


if __name__ == "__main__":
    main()