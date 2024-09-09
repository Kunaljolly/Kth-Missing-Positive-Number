class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        r, l  =  -1,  len(arr)
        while (l-r)  >  1:
            mid  =  (r+l)//2
            bf = arr[mid] - mid - 1
            if (bf < k):
                r = mid
            else:
                l = mid

        return(k+l)
