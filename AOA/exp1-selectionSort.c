#include <stdio.h>
#define size 5

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void main() 
{
    int array[size];
    printf("Enter elements of the array\n");
    for( int i = 0; i < size; i++)
    {
        printf("array[%d]: ", i);
        scanf("%d", &array[i]);
    }
    int i = 0;

    for(i = 0; i < size-1; i++)
    {
        int min_index = i;
        for(int j = i+1; j < size; j++)
        {
            if(array[j] < array[min_index])
                min_index = j;
        }
        swap(&array[min_index], &array[i]);
    }

    printf("Sorted array: \n");
    for(int i = 0; i < size; i++)
    {
        printf("%d\t", array[i]);
    }
    printf("\n");

}

// ---------OUTPUT---------
// student@student-X556UQK:~/Desktop/workspace/sem4-uni/AOA$ gcc exp1-selectionSort.c -o exp1 && ./exp1
// Enter elements of the array
// array[0]: 9
// array[1]: 3
// array[2]: 5
// array[3]: 91
// array[4]: 5
// Sorted array: 
// 3       5       5       9       91
// student@student-X556UQK:~/Desktop/workspace/sem4-uni/AOA$