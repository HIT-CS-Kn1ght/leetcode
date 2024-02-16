import heapq


class Solution(object):
    def numsGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # initial
        DP = [0]
        larger_sum, smaller_sum = 0, nums[0]
        larger_arr, smaller_arr = [], [-nums[0]]

        # DP
        for i in range(1, len(nums)):
            new = nums[i] - i
            heapq.heappush(smaller_arr, -new)
            smaller_sum += new
            flag = False
            if len(larger_arr) == 0:
                if len(smaller_arr) == 2:
                    flag = True
            elif -smaller_arr[0] > larger_arr[0] or len(smaller_arr) == len(larger_arr) + 2:
                flag = True
            if flag:    # move from smaller to larger
                a = -heapq.heappop(smaller_arr)
                smaller_sum -= a
                heapq.heappush(larger_arr, a)
                larger_sum += a

            if len(smaller_arr) == len(larger_arr) - 1:  # move back one
                a = heapq.heappop(larger_arr)
                larger_sum -= a
                heapq.heappush(smaller_arr, -a)
                smaller_sum += a

            if i & 1:   # even
                DP.append((larger_sum - smaller_sum) % 1000000007)
            else:
                DP.append((larger_sum - smaller_sum - smaller_arr[0]) % 1000000007)

        return DP


if __name__ == '__main__':
    s = Solution()
    n = [471, 626, 848]
    print(s.numsGame(n))
