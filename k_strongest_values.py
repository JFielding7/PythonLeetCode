class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        center = arr[len(arr) - 1 >> 1]
        i = 0
        j = len(arr) - 1
        res = []

        for _ in range(k):
            i_val = abs(arr[i] - center)
            j_val = abs(arr[j] - center)

            if i_val > j_val:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j -= 1

        return res
