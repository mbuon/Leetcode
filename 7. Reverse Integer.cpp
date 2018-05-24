#include <iostream>
#include <sstream>

using namespace std;

class Solution {
public:
    int reverse(int x) {

        stringstream buffer;
        buffer << x;
        string X = buffer.str();
       
        int left = 0;
        int right = X.length() - 1;
        bool minus = false;
       
        if (x < 0) {

            left += 1;
            minus = true;
        }
        
        while (left < right) {
            char temp = X[left];
            X[left] = X[right];
            X[right] = temp;

            left++;
            right--;
        }
        
        stringstream result;

        result << X;
        result >> x;
        
        return x;
    }
};

int main(int argc, char const *argv[])
{
    Solution S;
    printf("%d", S.reverse(123456789));
    return 0;
}