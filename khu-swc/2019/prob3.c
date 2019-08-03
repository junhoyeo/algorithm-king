#include <stdio.h>
#include <string.h>
int main(){
    int n;
    scanf("%d", &n);
    int cards[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    // for(int i=0;i<10;i++){
    //     scanf("%d", &cards[i]);
    // }
    int deck[10] = {0,};
    for(int i=0;i<n;i++){
        int left[5], right[5];
        memcpy(left, cards, 5 * sizeof(int)); 
        memcpy(right, &cards[5], 5 * sizeof(int)); 
        int left_idx = 0;
        int right_idx = 0;
        for(int j=0;j<10;j++) {
            if (j%2==0) {
                // left부터
                deck[j] = left[left_idx++];
            }
            else deck[j] = right[right_idx++];
        }
        memcpy(cards, deck, 10 * sizeof(int)); 
    }
    for(int i=0;i<10;i++){
        printf("%d ", deck[i]);
    }
}
