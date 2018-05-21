#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {

    	if (strs.size() == 0) {
    		return "";
    	}
    	string prefix = strs[0];
    	for (int i = 1; i < strs.size(); i++) {

    		for (int j = 0; j < prefix.size(); j++) {

    			if (prefix[j] != strs[i][j]) {
    				prefix = prefix.substr(0, j);
    			}
    		}
    	}

    	return prefix;
    }

	string longestCommonPrefixIterator(vector<string>& strs) {
	    int index = 0;
	    bool valid = true;
	    
	    // For each index 0:length
	    for (int index = 0; valid = true; index ++) {
	        // For each string
	        
	        if (strs[0].size() > index) {
	            
	            char element = strs[0][index];
	            
	            for (int i = 1; i < strs.size(); i++) {
	                if ((strs[i].size() > index)) {
	                    if (strs[i][index] != element) {
	                        valid = false;
	                        break;
	                    }
	                }
	                else {
	                    valid = false;
	                    break;
	                }
	            }
	        }
	        else {
	            valid = false;
	            break;
	        }
	    }
	    
	    return strs[0].substr(0,index);
	}
};

int main(int argc, char const *argv[])
{
	string A("flowe!");
	string B("flo");
	string C("flowers");

	vector<string> strings;
	strings.push_back(A);
	strings.push_back(B);
	strings.push_back(C);

	Solution S;
	cout << S.longestCommonPrefix(strings);
	return 0;
}
