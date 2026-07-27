#include <stdio.h>

void selectionSort(int arr[], int n, int *comparisons, int *swaps) {
    int i, j, minIndex, temp;

    for (i = 0; i < n - 1; i++) {
        minIndex = i;
        for (j = i + 1; j < n; j++) {
            (*comparisons)++;             
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        if (minIndex != i) {
            temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
            (*swaps)++;                    
        }
    }
}

int main() {
    int n, i;
    int comparisons = 0, swaps = 0;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    int arr[n];
    printf("Elements: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    selectionSort(arr, n, &comparisons, &swaps);

    printf("Sorted Array: ");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    printf("Comparisons: %d\n", comparisons);
    printf("Swaps: %d\n", swaps);

    return 0;
}
