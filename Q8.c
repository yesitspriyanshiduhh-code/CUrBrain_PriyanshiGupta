#include <stdio.h>

int main(void) {
    int n, k;
    int count = 0;

    printf("Enter n and k: ");
    scanf("%d %d", &n, &k);

    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {  // i is a factor of n
            count++;

            if (count == k) {
                printf("%d\n", i);
                return 0;
            }
        }
    }

    printf("-1\n");  // n has fewer than k factors
    return 0;
}