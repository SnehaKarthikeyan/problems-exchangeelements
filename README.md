# problems-exchangeelements

Question:

Given a number N, array of N integers, print the resultant array after interchanging first and last elements in the given array. Input Size : |N| <= 1000000

Input Description:

The first line contains an integer N. The second line contains N space-separated integers, which denotes array elements.

Output Description:

Print the resultant array after interchanging first and last elements in the given array.

Hints:

Swap the first and the last elements in the given array.

Sample Input:

7\n 
1 4 6 2 9 7 3

Sample Output:

3 4 6 2 9 7 1

Explanation:

After interchanging first and last elements in the given array, the resultant array is 3 4 6 2 9 7 1

Testcase 1:

Input:

40\n 
34 56 78 67 22 43 54 66 23 45 68 11 25 45 55 67 11 73 67 34 56 78 87 67 23 45 68 11 25 45 55 67 11 73 67 34 56 78 67 22

Output:

22 56 78 67 22 43 54 66 23 45 68 11 25 45 55 67 11 73 67 34 56 78 87 67 23 45 68 11 25 45 55 67 11 73 67 34 56 78 67 34

Testcase 2:

Input:

22\n
45 78 93 22 45 23 56 79 99 54 51 12 34 43 34 78 66 32 44 35 67 29

Output:

29 78 93 22 45 23 56 79 99 54 51 12 34 43 34 78 66 32 44 35 67 45

Testcase 3:

Input:

15\n
56 32 43 11 78 33 11 23 89 33 12 45 78 23 66

Output:

66 32 43 11 78 33 11 23 89 33 12 45 78 23 56

Testcase 4:

Input:

38\n
11 78 33 11 23 89 33 12 45 23 56 79 99 54 51 12 34 43 34 78 66 32 44 35 45 78 23 66 34 56 78 87 67 23 45 68 11 25

Output:

25 78 33 11 23 89 33 12 45 23 56 79 99 54 51 12 34 43 34 78 66 32 44 35 45 78 23 66 34 56 78 87 67 23 45 68 11 11

Testcase 5:

Input:

54\n
11 25 45 55 67 11 73 67 23 56 79 99 54 51 12 34 43 34 78 66 32 44 34 56 78 87 67 23 45 68 11 25 34 56 78 67 22 43 54 66 23 45 68 45 55 67 11 73 67 34 56 78 67 22

Output:

22 25 45 55 67 11 73 67 23 56 79 99 54 51 12 34 43 34 78 66 32 44 34 56 78 87 67 23 45 68 11 25 34 56 78 67 22 43 54 66 23 45 68 45 55 67 11 73 67 34 56 78 67 11
