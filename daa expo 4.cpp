#include <stdio.h>

int findKthSmallest(int arr[], int n, int k) {
    int i, j, minIndex, temp;

    for (i = 0; i < k; i++) {
        minIndex = i;
        for (j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        if (minIndex != i) {
            temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }

    return arr[k - 1];   
}

int main() {
    int n, k, i;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    int arr[n];
    printf("Array: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter k: ");
    scanf("%d", &k);

    int result = findKthSmallest(arr, n, k);

    printf("%d", k);

    if (k % 10 == 1 && k % 100 != 11) printf("st");
    else if (k % 10 == 2 && k % 100 != 12) printf("nd");
    else if (k % 10 == 3 && k % 100 != 13) printf("rd");
    else printf("th");

    printf(" Smallest Element = %d\n", result);

    return 0;
}
