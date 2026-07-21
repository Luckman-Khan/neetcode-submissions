class Solution:
    def hammingWeight(self, n: int) -> int:

        d =  f"{n:b}"
        print(d)
        count = 0
        for i in d:

            print(i)
            if i== '1':
                count += 1
        return count
        