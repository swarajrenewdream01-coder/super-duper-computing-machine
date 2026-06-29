/*
Find Missing And Repeating
==========================

Given an unsorted array Arr of size N of positive integers. One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. Find these two numbers.

Example 1:
Input:
N = 2
Arr[] = {2, 2}
Output: 2 1
Explanation: Repeating number is 2 and 
smallest positive missing number is 1.

Example 2:
Input:
N = 3
Arr[] = {1, 3, 3}
Output: 3 2
Explanation: Repeating number is 3 and 
smallest positive missing number is 2.
Your Task:
You don't need to read input or print anything. Your task is to complete the function findTwoElement() which takes the array of integers arr and n as parameters and returns an array of integers of size 2 denoting the answer ( The first index contains B and second index contains A.)

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105
1 ≤ Arr[i] ≤ N
*/

class Solution:
    def findTwoElement(self, arr, n):
        xor_value = 0

        # XOR of array elements and numbers from 1 to n
        for i in range(n):
            xor_value ^= arr[i] ^ (i + 1)

        # Rightmost set bit
        set_bit = xor_value & -xor_value

        bucket1 = 0
        bucket2 = 0

        # Divide into two groups
        for i in range(n):

            if arr[i] & set_bit:
                bucket1 ^= arr[i]
            else:
                bucket2 ^= arr[i]

            if (i + 1) & set_bit:
                bucket1 ^= (i + 1)
            else:
                bucket2 ^= (i + 1)

        # Determine which is repeating
        if bucket1 in arr:
            return [bucket1, bucket2]
        else:
            return [bucket2, bucket1]