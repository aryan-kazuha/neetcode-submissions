class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i,a in enumerate(nums):
            if i>0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            k = len(nums) -1

            while j<k:

                sum_3 = a + nums[k] + nums[j]

                if sum_3 == 0:
                    res = [a,nums[j],nums[k]]

                    if res not in ans:
                        ans.append(res)

                    j+=1
                    k-=1

                elif sum_3 >0:
                    k -=1
                else:
                    j+=1
        return ans
