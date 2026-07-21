class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        used = [False] * n  # Track which words are already grouped
        result = []

        for i in range(n):
            if used[i]:
                continue
            group = [strs[i]]
            used[i] = True
            sorted_i = ''.join(sorted(strs[i]))

            for j in range(i + 1, n):
                if not used[j] and ''.join(sorted(strs[j])) == sorted_i:
                    group.append(strs[j])
                    used[j] = True

            result.append(group)

        return result
