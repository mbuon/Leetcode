static const auto _____ = []()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return nullptr;
}();

class Solution {
public:
    int removeElementOriginal(vector<int>& nums, int val) {
        int j = -1;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                j++;
                nums[j] = nums[i];
            }
        }
        
        return j + 1;
    }
    
    int removeElement(vector<int>& nums, int val) {
        int n = nums.size();
        int i = 0;
        
        while (i < n) {
            if (nums[i] == val) {
                int temp = nums[i];
                nums[i] = nums[n - 1];
                nums[n - 1] = temp;
                n--;
            }
            else {
                i++;
            }
        }
        return n;
    }
};