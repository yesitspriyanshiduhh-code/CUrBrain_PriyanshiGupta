#include<stdio.h>
int gcd(int a,int b){
    int r;
    while(b!=0){
        r=a%b;
        a=b;
        b=r;
     }
    return a;
}
int main(void){
    int a[100],n,rgcd;
    printf("Enter no. of elements: ");
    scanf("%d",&n);
    printf("Enter those elements: ");
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    rgcd=a[0];
    for(int i=0;i<n;i++){
        rgcd=gcd(rgcd,a[i]);
    }
    printf("%d",rgcd);
    return 0;
}