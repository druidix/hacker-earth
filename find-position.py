#!/usr/local/bin/python3

# This is not needed in this implementation
how_many = int(input())

nums = input().split()
int_to_find = None

for idx, val in enumerate(nums):
  nums[idx] = int(val)

int_to_find = int(input())

print(nums.index(int_to_find))