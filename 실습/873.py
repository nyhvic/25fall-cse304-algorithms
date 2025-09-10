class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        iarr = []
        s,m,e = 0,1,2
        while e<len(arr):
            if iarr:
                length = len(iarr)
                if iarr[length-1]+iarr[length-2] == arr[e]:
                    iarr.append(arr[e])
                e+=1
            else:
                if arr[s]+arr[m]==arr[e]:
                    iarr.append(s)
                    iarr.append(m)
                    iarr.append(e)
                    s+=1
                    m+=1
                    e+=1
                elif arr[s]+arr[m] > arr[e]:
                    e+=1
                else:
                    if m<e-1:
                        s+=1
                        m+=1
                    else:
                        s+=1
                        m+=1
                        e+=1
        return len(iarr)
4 14 18 32 50 
S= Solution()  
print(S.lenLongestFibSubseq([2,4,7,8,9,10,14,15,18,23,32,50]))