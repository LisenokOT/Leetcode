class Solution(object):
    def firstUniqChar(self, s): 
        letters='abcdefghijklmnopqrstuvwxyz'
        new_data = [s.index(elem) for elem in letters if s.count(elem) == 1]
        return min(new_data) if len(new_data)>0 else -1
        
def main():
    stri = Solution()
    print(stri.firstUniqChar("leetcode"))
    print(stri.firstUniqChar("loveleetcode"))
    print(stri.firstUniqChar("aabb"))
    print(stri.firstUniqChar(""))


if __name__ == "__main__":
    main()