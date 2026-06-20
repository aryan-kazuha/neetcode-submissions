class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> seek;

        for (int i  = 0; i <nums.size();i++){
            int need = target - nums[i];

            if (seek.count(need)){
                return {seek[need],i};
            }

            seek[nums[i]] = i;
        }

        return {};
    }
};
