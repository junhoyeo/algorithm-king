#include <stdio.h>
int tri(int a, int b, int c) {
    if ((a + b > c) && (a + c > b) && (b + c > a))
        return 1;
    return 0;
}
int main(){
    int a,b,c;
    scanf("%d%d%d", &a, &b, &c);
    int t;
    for(t=0;;t++){
        if (tri(a,b,c)){
            // printf("[!] t=%d %d %d %d\n", t, a, b, c);
            break;
        }
        if(a<=b && a<=c) a++;
        if(b<=a && b<=c) b++;
        if(c<=a && c<=b) c++;
        // printf("[*] t=%d %d %d %d\n", t, a, b, c);
    }
    printf("%d", t);
    return 0;
}
