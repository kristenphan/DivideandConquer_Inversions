# Divide and Conquer Algorithm: Number of Inversions in a Sequence
<br/>

__Repo description__
<br/>

This repo stores the code written by myself, Kristen Phan, as part of a Coursera course (https://www.coursera.org/learn/algorithmic-toolbox/). Please refrain from checking out the script if you're currently taking the course. 
<br/>

__Problem Introduction__
<br/>

An inversion of a sequence 𝑎0, 𝑎1, . . . , 𝑎𝑛−1 is a pair of indices 0 ≤ 𝑖 < 𝑗 < 𝑛 such
that 𝑎𝑖 > 𝑎𝑗 . 
<br/>
The number of inversions of a sequence in some sense measures how
close the sequence is to being sorted. For example, a sorted (in non-descending
order) sequence contains no inversions at all, while in a sequence sorted in descending
order any two elements constitute an inversion (for a total of 𝑛(𝑛 − 1)/2
inversions).
<br/>

__Problem Description__
<br/>

__Task__
<br/>
The goal in this problem is to count the number of inversions of a given sequence.
Input Format. The first line contains an integer 𝑛, the next one contains a sequence of integers
𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
<br/>
__Constraints__
<br/>
1 ≤ 𝑛 ≤ 105, 1 ≤ 𝑎𝑖 ≤ 109 for all 0 ≤ 𝑖 < 𝑛.
<br/>
__Output Format__
<br/>
Output the number of inversions in the sequence.
__Sample 1__
<br/>
Input:
<br/>
5
<br/>
2 3 9 2 9
<br/>
Output:
<br/>
2
<br/>
<br/>
The two inversions here are (1, 3) (𝑎1 = 3 > 2 = 𝑎3) and (2, 3) (𝑎2 = 9 > 2 = 𝑎3).
<br/>

__What To Do__
<br/>
This problem can be solved by modifying the merge sort algorithm. For this, we change both the Merge and
MergeSort procedures as follows:
<br/>

∙ Merge(𝐵, 𝐶) returns the resulting sorted array and the number of pairs (𝑏, 𝑐) such that 𝑏 ∈ 𝐵, 𝑐 ∈ 𝐶,
and 𝑏 > 𝑐;
<br/>

∙ MergeSort(𝐴) returns a sorted array 𝐴 and the number of inversions in 𝐴.

