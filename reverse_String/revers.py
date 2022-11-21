class Solution(object):
    def reverseString(self, s):
        for i in range(len(s)):
            s.insert(0,s.pop(i))
            i += 1
        return (s)


def main():
    str = Solution()
    print(str.reverseString(["h","e","l","l","o"])) #["o","l","l","e","h"]


if __name__ == "__main__":
    main()