#include <stdio.h>
#include <string.h>
int main() {
    int t;scanf("%d", &t);
    for(int k=0;k<t;k++){
        int n;scanf("%d", &n);
        int arr[n];
        for(int i=0;i<n;i++){
            scanf("%d", &arr[i]);
        }
        int coins[n-1];
        memset(coins, 0, sizeof coins);
        for(int i=0;i<n-1;i++){
            if(arr[i] < arr[i+1]) {
                coins[i] = 1;
            } else if (arr[i] > arr[i+1]) {
                coins[i] = 0;
            }
        }
        int max = 0;
        for(int start=0;start<n;start++){
            int len=1;
            int prev = (coins[start]) ? 0 : 1;
            for(int i=start;i<n-1;i++){
                if (coins[i] != prev){
                    len++;
                    prev=coins[i];
                }
                else break;
            }
            if (len > max) max = len;
        }
        printf("%d\n", max);
    }
}
