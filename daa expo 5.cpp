#include <stdio.h>

void selectionSort(int marks[], int n) {
    int i, j, minIndex, temp;

    for (i = 0; i < n - 1; i++) {
        minIndex = i;
        for (j = i + 1; j < n; j++) {
            if (marks[j] < marks[minIndex]) {
                minIndex = j;
            }
        }
        if (minIndex != i) {
            temp = marks[i];
            marks[i] = marks[minIndex];
            marks[minIndex] = temp;
        }
    }
}

int main() {
    int n, i;

    printf("Enter number of students: ");
    scanf("%d", &n);

    int marks[n];
    printf("Marks: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &marks[i]);
    }

    selectionSort(marks, n);

    printf("Sorted Marks: ");
    for (i = 0; i < n; i++) {
        printf("%d ", marks[i]);
    }
    printf("\n");

    return 0;
}
