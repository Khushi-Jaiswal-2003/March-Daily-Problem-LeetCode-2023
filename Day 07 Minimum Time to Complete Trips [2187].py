import sys
class Solution:
    def minimumTime(self, time, totalTrips):
        s = 1
        e = max(time) * totalTrips
        mid = (s + e) // 2

        def good(x):
            count=0
            for t in time:
                count+= x//t
            return count>=totalTrips

        while(s<e):
            if(good(mid)):
                e = mid
            else:
                s =mid+1
            mid = (s + e) // 2

        print(s)
a = Solution()
a.minimumTime([2], 1)
