/*
    @LeetCode Problem
    
    Remove Duplicates from Sorted Array
*/

#include <stdio.h>

int removeDuplicates(int* nums, int numsSize) {

    if (numsSize == 0) return 0;

    int nz = 1;

    for (int i=1; i<numsSize; i++)
    {
        if ( nums[i] != nums[i-1] )
        {
            nums[nz] = nums[i];
            nz++;
        }
    }
    return nz;
}

int main()
{
    int sorted[] = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    int sorted_sz = 10;

    int new_sz = removeDuplicates(sorted, sorted_sz);

    for (int i = 0; i < new_sz; i++)
    {
        printf("%d ", sorted[i]);
    }
    
    return 0;
}
