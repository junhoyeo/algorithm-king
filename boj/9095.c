#include <stdio.h>
int dp(int n){
    if (n==1) return 1;
    else if (n==2) return 2;
    else if (n==3) return 4;
    return dp(n-3) + dp(n-2) + dp(n-1);
}
int main(){
    int t;
    scanf("%d", &t);
    for (int i=0;i<t;i++){
        int n;
        scanf("%d", &n);
        printf("%d\n", dp(n));
    }
}
