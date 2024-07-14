<b>Comparison of Sorting Algorithm Performance</b>

<b>Introduction</b>

This study compares the performance of three sorting algorithms: Merge Sort, Insertion Sort, and Timsort (a built-in sorting function in Python). The comparison is based on the execution times of the algorithms for different data sets.

Algorithms

Merge Sort

Merge Sort is a divide-and-conquer algorithm with a time complexity of O(n log n).

Insertion Sort

Insertion Sort is a simple comparative algorithm with a time complexity of O(n^2).

Timsort

Timsort is a hybrid algorithm derived from merge sort and insertion sort, with a worst-case time complexity of O(n log n) and a best-case time complexity of O(n).

Methodology

We tested the algorithms on data sets of various sizes (100, 1000, 5000, 10000) and forms (random, sorted, and reverse sorted). The average execution time was recorded using the timeit module.

Results

Lp.    Data Size       Data Type  Insertion Sort  Merge Sort  Timsort (sorted)
0         100          random        0.000290    0.000186          0.000012
1         100          sorted        0.000016    0.000193          0.000005
2         100  reverse_sorted        0.000471    0.000166          0.000006
3        1000          random        0.032153    0.002439          0.000117
4        1000          sorted        0.000151    0.002019          0.000014
5        1000  reverse_sorted        0.056693    0.002089          0.000063
6        5000          random        0.894695    0.015876          0.000681
7        5000          sorted        0.000777    0.012853          0.000069
8        5000  reverse_sorted        1.754333    0.013140          0.000263
9       10000          random        3.436013    0.034043          0.001453
10      10000          sorted        0.001551    0.035166          0.000245
11      10000  reverse_sorted        7.059202    0.041636          0.000544

<b>Conclusions</b>

The results show that Timsort outperforms both Merge Sort and Insertion Sort in all tested scenarios. This efficiency stems from Timsort's hybrid nature, combining the best aspects of merge sorting and insertion sorting. As a result, programmers often rely on built-in algorithms such as Timsort due to their efficiency and reliability.
