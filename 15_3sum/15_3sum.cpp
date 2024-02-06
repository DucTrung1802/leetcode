#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

/**
 * Not my solution
 */

class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        int index = 0;
        int left = index + 1;
        int right = nums.size() - 1;
        sort(nums.begin(), nums.end());
        vector<vector<int>> res = {};
        int target;

        while (index <= nums.size() - 3)
        {
            // cout << *it1 << endl;
            left = index + 1;
            right = nums.size() - 1;
            target = 0 - nums[index];
            while (left < right)
            {
                if (nums[left] + nums[right] == target)
                {
                    res.push_back({nums[index], nums[left], nums[right]});
                    // Skip to another different value
                    while (nums[left] == nums[++left] && left < right)
                    {
                    }
                    while (nums[right] == nums[--right] && left < right)
                    {
                    }
                }
                else if (nums[left] + nums[right] < target)
                {
                    left++;
                }
                else
                {
                    right--;
                }
            }
            while (nums[index] == nums[++index] && index <= nums.size() - 3)
            {
            }
        }

        return res;
    }
};

int main()
{
    Solution solution;
    vector<int> vect = {-1, -2, -3, 3, 5, 3, 3, 3};
    vector<vector<int>> result;
    result = solution.threeSum(vect);
    for (int i = 0; i < result.size(); i++)
    {
        for (int j = 0; j < 3; j++)
        {
            std::cout << result[i][j] << "\t";
        }
        std::cout << std::endl;
    }
    return 0;
}