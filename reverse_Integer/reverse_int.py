class Solution(object):
    def reverseString(self, x): 
        data = str(abs(x))
        if x < 0:
            data += "-"
        return int(data[::-1]) if -2**31 <= int(data[::-1]) <= 2**31 - 1 else 0


def main():
    stri = Solution()
    print(stri.reverseString(1534236469))
    print(stri.reverseString(123))
    print(stri.reverseString(1000))
    print(stri.reverseString(-12))


if __name__ == "__main__":
    main()