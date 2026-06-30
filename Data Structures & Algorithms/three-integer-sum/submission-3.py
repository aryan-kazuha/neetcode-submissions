class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans  =[]

        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            
            i = k+1
            j = len(nums) -1

            while j>i:
                val = nums[k]+ nums[i] + nums[j]
                
                if val == 0:
                    res = [nums[k],nums[i] , nums[j]]

                    if res not in ans:
                        ans.append(res)
                        
                    i+=1
                    j-=1
                
                elif val>0:
                    j -=1
                
                else:
                    i+=1
        return ans
            