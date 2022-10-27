# Problem 2:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.



# Example 1:
# Input: nums = [2,7,11,15], target = 9 , Output: [0,1]
# Example 2:
# Input: nums = [3,2,4], target = 6 , Output: [1,2]


def get_target(nums, target):
    diff = {}

    for num in nums:
        if num in diff.keys():
            i1 = nums.index(diff[num])
            i2 = nums.index(num)

            return [i1, i2]

        diff[target-num] = num

print(get_target(nums = [2,7,11,15], target = 9))
print(get_target(nums = [3,2,4], target = 6))


def get_target(nums, target):

    diff = {}
    for i, num in enumerate(nums):
        need = target - num

        if need in diff:
            return [diff[need], i]

        diff[num] = i

print(get_target(nums = [2,7,11,15], target = 9))
print(get_target(nums = [3,2,4], target = 6))