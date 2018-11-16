// Solved using sieve of Eratosthenes
// C++ usually provides a better runtime for the same logic than Python
// i goes from 0 to root of n: this is because say n is 100, no number greater than 10 multiplied with another number greater than 10 will get us
// a number less than 100
// j goes from i to n/i: this is because we are checking say we checkfor 5 * 4, we would have already checked for 4 * 5.

class Solution {
public:
    int countPrimes(int n) {
        vector<bool> primes(n, true);
        primes[0] = false;
        primes[1] = false;
        
        for (int i = 0; i * i <= n; i++) {
            if (primes[i] == true) {
                for (int j = i; j <= n/i; j++) {                    
                    primes[i * j] = false;
                }
            }
        }
        
        return count(primes.begin(), primes.end(), true);
    }
};