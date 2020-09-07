# python3
from itertools import combinations


def compute_inversions_naive(a):
    """
    This naive function computes and returns the number of inversions in an array
    by checking every combination of a pair of two array elements.
    """
    number_of_inversions = 0
    # since the input sequence "range(len(a)) is sorted, combination output will also be sorted
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def merge(arr1, arr2):
    """
    This function merges two sorted, input arrays arr1, arr2 into a sorted array arr_sorted,
    and returns the sorted array and the inversion count i.e. the number of pairs (a, b) in arr1, arr2 such that a > b
    """
    # create an empty array, an inversion count, and a count of the number of elements removed from arr2 during the merging process
    arr_sorted, inv_count, arr2_removal_count = [], 0, 0

    # merge the two arrays into a sorted array
    while arr1 and arr2:
        a, b = arr1[0], arr2[0]
        if a > b:  # an inversion is found in current pair (a, b)
            arr_sorted.append(b)
            arr2_removal_count += 1
            inv_count += 1
            del arr2[0]
        else:
            # No inversion. Because arr1 is sorted, for any element x in arr1 that comes after a, x > a,
            # implying x is greater than all elements in arr2 which were previously removed
            # Therefore, increment the inv_count by the number of elements in arr2 previously removed
            if len(arr1) != 1:
                inv_count += arr2_removal_count
            arr_sorted.append(a)
            del arr1[0]

    if len(arr1) > 0:
        arr_sorted += arr1
        # For all remaining elements x in arr1, x is greater than elements in arr2 previously remove
        # Therefore, increment the inv_count by the multiple of arr2_removal_count and (the number of remaining elements in arr1 - 1),
        # reason being for arr1[0], we already counted the inversion instances in previous comparisons
        inv_count += arr2_removal_count * (len(arr1) - 1)

    if len(arr2) > 0:
        # when there are only elements in arr2 remaining, there is no additional inversion
        arr_sorted += arr2

    return arr_sorted, inv_count


def compute_inversions(a):
    """
    This function sorts the input array A and returns the number of inversions in A in the form of a tuple
    E.g.:
    input:
    A = [2, 3, 9, 2, 9]
    output:
    ([2, 2, 3, 9, 9], 2)
    explanation: there are 2 inversions here: a[1] and a[3] (3 > 2); a[2] and a[3] (9 > 2)
    """
    # if array is of length 1, the array is already sorted and has no inversion
    if len(a) == 1:
        return a, 0

    # split array A in two unsorted halves, sort them,
    # and return the sorted halves B,C along with the number of inversions in each half
    mid = len(a) // 2
    b = compute_inversions(a[0:mid])
    c = compute_inversions(a[mid:len(a)])

    # merge the two sorted halves B[0], C[0] into a single sorted array,
    # return the sorted array along with the number of pairs (b,c) in B and C such as b > c
    # in the form of a tuple
    a_sorted = merge(b[0], c[0])

    # return the total number of inversions in A
    return a_sorted[0], b[1] + c[1] + a_sorted[1]


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print((compute_inversions(elements))[1])  # print the number of inversion
