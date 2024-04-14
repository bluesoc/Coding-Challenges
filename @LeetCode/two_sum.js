/**
* @param {number[]} nums
* @param {number} target
* @return {number[]}
*/
var twoSum = function(nums, target) {
   let map = {}
    for (let i=0; i < nums.length; i++) {
        if ( target - nums[i] in map )
        {
          return [ i, map[target - nums[i]] ]
        }
      	if ( !map[nums[i]] ) {
          map[nums[i]] = i
        }
    }
    return []
}
