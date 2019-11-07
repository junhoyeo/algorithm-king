// error
#include <stdio.h>
#include <math.h>
int main() {
    long long int a, b;
    scanf("%lld%lld", &a, &b);
    long long int count = 0;
    for (long long int n = a; n <= b; n++) {
        for (long long int i = 1; i <= sqrt(n); i++) { 
            if (n % i == 0) { 
                if (n / i == i) 
                    count++; 
    
                else
                    count += 2; 
            } 
        } 
    }
    printf("%lld\n", count);
}
