// First time using C

#include <stdio.h>

#define ARRAYLENGTH(x) (int)(sizeof x / sizeof x[0])

void SortArray(float arr[], int length);
void PrintArray(float arr[], int length);

int main()
{
    float nums[] = {89.9, 4.76, 6.6, 3.56, 2.9, 13.8};
    int len = ARRAYLENGTH(nums);
    printf("The length of this array is: %d\n", len);
    printf("Sorting...\n");
    SortArray(nums, len);
    PrintArray(nums, len);
    printf("Done.");
    return 0;
}

void SortArray(float arr[], int length)
{
    for (int i = 0; i < length; i++)
    {
        for (int j = 0; j < length - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                float temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void PrintArray(float arr[], int length)
{
    for (int i = 0; i < length; i++)
    {
        printf("%f\n", arr[i]);
    }
}
