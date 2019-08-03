#include <stdio.h>
int main(){
    int n, m;
    scanf("%d%d", &n, &m);
    int dp[300];
    dp[0] = n-1; // n*1 줄짜리 초콜릿은 n-1번 잘라야 함
    for(int i=1;i<m;i++){
        // n*1줄에서 n*m줄로 한 줄씩 늘릴 때마다 이전 줄보다 n번 더 잘라야 함
        // dp[i] = dp[i-1] + (n-1) + 1;
        dp[i] = dp[i-1] + n;
    }
    printf("%d", dp[m-1]);
}
