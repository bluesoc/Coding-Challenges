void moveZeroes(int* nums, int numsSize) {
    for (int i=0; i<numsSize; i++) {
        if (nums[i] == 0) {
            // Hit zero
            for (int x = i+1; x<numsSize; x++) {
                // Search next number non zero
                if ( nums[x] != 0 ) {
                    // swap
                    nums[i] = nums[x];
                    nums[x] = 0;
                    break;
                }
            }
        }
    }
}
