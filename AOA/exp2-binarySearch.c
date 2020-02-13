#include <stdio.h>
#include "exp1-selectionSort-e.c"

void selectionSort(int array[], int n);

int binarySearch(int array[], int key)
{
    int low = 0, high = sizeof(array) / sizeof(array[0]) - 1;
    while (high >= low)
    {
        int mid = (low + high) / 2;
        if (key == array[mid])
        {
            printf("Element found!\n");
            return 0;
        }

        else if (key < array[mid])
            high = mid - 1;
        else
            low = mid + 1;
    }
    printf("\nKey not found!\n");
    return -1;
}

int main()
{
    int n, key;
    printf("Enter the size of array: ");
    scanf("%d", &n);

    int array[n];
    printf("Enter elements of the array\n");
    for (int i = 0; i < n; i++)
    {
        printf("array[%d]: ", i);
        scanf("%d", &array[i]);
    }
    selectionSort(array, n);
    printf("Enter key to search: ");
    scanf("%d", &key);
    binarySearch(array, key);
}

// -----OUTPUT-----
// student@student-X556UQK:~/Desktop/workspace/sem4-uni/AOA$ gcc exp2-binarySearch.c -o exp2 && ./exp2
// Enter the size of array: 6
// Enter elements of the array
// array[0]: 3
// array[1]: 9
// array[2]: 4
// array[3]: 6
// array[4]: 0
// array[5]: 1
// Enter key to search: 0
// Element found!