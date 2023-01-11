class Solution:
    def groupAnagrams(self, strs):
        result = []
        dic = {}
        for i in strs:
            word = ''.join(sorted(i))
            if word not in dic.keys():
                dic[word] = [i]
            else:
                dic[word].append(i)
        return dic.values()

if __name__ == "__main__":
    strs = ["tea", "ate"]
    s = Solution()
    s.groupAnagrams(strs)