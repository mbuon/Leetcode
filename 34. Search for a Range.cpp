#include <vector>

using namespace std;

class Solution {

	int binarySearch(vector<int>& nums, int low, int high, int target) {
		int mid = (low + high) / 2;

		printf("Low: %d High: %d Mid: %d\n", low, high, mid);

		if ((nums[mid] < target) &&(nums[mid + 1] == target)) {

			return mid + 1;
		}
		else if (nums[mid] >= target) {

			if (mid == 0) {
				return 0;
			}
			return binarySearch(nums, low, mid, target);
		}
		else {
			return binarySearch(nums, mid, high, target);
		}
	}

public:
    vector<int> searchRange(vector<int>& nums, int target) {

    	// Search starting position

    	int low = 0;
    	int high = nums.size() - 1;
		int start = binarySearch(nums, low, high, target);
		int end = -1;

		printf("Starting position of 8: %d", (int) start);

		vector<int> result;
		result.push_back(start);
		result.push_back(end);

		return result;
	}
};

int main(int argc, char const *argv[])
{
	Solution S;
	vector<int> nums;
	nums.push_back(3);
	nums.push_back(7);
	nums.push_back(7);
	nums.push_back(8);
	nums.push_back(8);
	nums.push_back(8);
	nums.push_back(8);
	nums.push_back(8);
	nums.push_back(8);
	
	S.searchRange(nums, 8);
	return 0;
}