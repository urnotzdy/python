from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        result = ""
        i = 0
        temp_result = strs[0]
        size = len(temp_result)
        while i < size:
            mid = temp_result[i]
            flag = True
            for tmp in strs:
                if len(tmp) == i or tmp[i] != mid:
                    flag = False
                    break
            if flag:
                result = result + mid
                i = i + 1
            else:
                return result
        return result
solution = Solution()
strs = [""]
result = solution.longestCommonPrefix(strs)
print(result)