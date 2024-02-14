class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        res = 0
        while len(timeSeries):
            start = timeSeries[0]
            end = start + duration
            del timeSeries[0]
            while True:
                if len(timeSeries) == 0:
                    break
                if end < timeSeries[0]:
                    break
                end = timeSeries[0] + duration
                del timeSeries[0]
            res += end - start
        return res


if __name__ == '__main__':
    t = [1, 2]
    d = 2
    s = Solution()
    print(s.findPoisonedDuration(t, d))
