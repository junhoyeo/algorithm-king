#include <stdio.h>
#include <math.h>

int main() {
    int n;scanf("%d",&n);
    int bot[n];
    int max=0;
    for(int i=0;i<n;i++){
        scanf("%d", &bot[i]);
        if(bot[i] > max) max = bot[i];
    }
    int t;scanf("%d", &t);
    int min = 0; int min_cap = 0;
    for(int cap=max;cap>0;cap--) {
        int budget = 0;
        int price = t+cap;
        for(int i=0;i<n;i++){
            budget += price * ceil((bot[i] + cap - 1)/cap); // 필요 병 수 = 물질 양 / 용량
        }
        if (cap == max || (budget <= min && cap < min_cap)){
            min = budget;
            min_cap = cap;
        }
        // printf("[*] %d %d\n", budget, cap);
    }
    printf("%d %d", min, min_cap);
}
