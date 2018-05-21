#include <vector>

using namespace std;

class Solution {

	int binarySearchStart(vector<int>& nums, int low, int high, int target) {
		
		int	mid = (low + high) / 2;

		if ((nums[mid] == target) && ((mid == 0) || (nums[mid - 1] < target))) {
			return mid;
		}
		else if (low >= high) {
			return -1;
		}
		else if (nums[mid] >= target) {
			high = mid;
			return binarySearchStart(nums, low, high, target);
		}
		else {
			low = mid + 1;
			return binarySearchStart(nums, low, high, target);
		}
	}

	int binarySearchEnd(vector<int>& nums, int low, int high, int target) {
		
		int	mid = (low + high) / 2;

		if ((nums[mid] == target) && ((mid == nums.size() - 1) || (nums[mid + 1] > target))) {
			return mid;
		}
		else if (low >= high) {
			return -1;
		}
		else if (nums[mid] <= target) {
			low = mid + 1;
			return binarySearchEnd(nums, low, high, target);
		}
		else {
			high = mid;
			return binarySearchEnd(nums, low, high, target);
		}
	}

public:
    vector<int> searchRange(vector<int>& nums, int target) {

    	vector<int> result;

        if (nums.size() == 0) {
            
			result.push_back(-1);
			result.push_back(-1);
            return result;
        }
        
    	int low = 0;
    	int high = nums.size() - 1;
		int start = binarySearchStart(nums, low, high, target);
        int end = -1;
       
        if (start != -1) {
            end = binarySearchEnd(nums, start, high, target);
        }

		result.push_back(start);
		result.push_back(end);
        
		return result;
	}
};

int main(int argc, char const *argv[])
{
	Solution S;

	vector<int> nums;
	nums.push_back(1);
	nums.push_back(7);
	nums.push_back(7);
	nums.push_back(8);
	nums.push_back(8);
	nums.push_back(8);
	nums.push_back(8);
	nums.push_back(8);
	nums.push_back(8);
	nums.push_back(8);
	nums.push_back(9);

	for (int i = 0; i < nums.size(); i++) {
		printf("%d ", nums[i]);
	}

	printf("\n");

	S.searchRange(nums, 0);

	return 0;
}