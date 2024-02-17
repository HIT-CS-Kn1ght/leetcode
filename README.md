[TOC]

### Solutions

##### 103.py	binary-tree-zigzag-level-order-traversal

Given the `root` of a binary tree, return *the zigzag level order traversal of its nodes' values*. (i.e., from left to right, then right to left for the next level and alternate between).

##### 107.py	binary-tree-level-order-traversal-ii

Given the `root` of a binary tree, return *the bottom-up level order traversal of its nodes' values*. (i.e., from left to right, level by level from leaf to root).

##### 236.py	lowest-common-ancestor-of-a-binary-tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

##### 419.py	battleships-in-a-board

Given an `m x n` matrix `board` where each cell is a battleship `'X'` or empty `'.'`, return *the number of the **battleships** on* `board`.

**Battleships** can only be placed horizontally or vertically on `board`. In other words, they can only be made of the shape `1 x k` (`1` row, `k` columns) or `k x 1` (`k` rows, `1` column), where `k` can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

##### 429.py	n-ary-tree-level-order-traversal

Given an n-ary tree, return the *level order* traversal of its nodes' values.

*Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).*

##### 495.py	teemo-attacking

Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly `duration` seconds. More formally, an attack at second `t` will mean Ashe is poisoned during the **inclusive** time interval `[t, t + duration - 1]`. If Teemo attacks again **before** the poison effect ends, the timer for it is **reset**, and the poison effect will end `duration` seconds after the new attack.

You are given a **non-decreasing** integer array `timeSeries`, where `timeSeries[i]` denotes that Teemo attacks Ashe at second `timeSeries[i]`, and an integer `duration`.

Return *the **total** number of seconds that Ashe is poisoned*.

##### 987.py	vertical-order-traversal-of-a-binary-tree

Given the `root` of a binary tree, calculate the **vertical order traversal** of the binary tree.

For each node at position `(row, col)`, its left and right children will be at positions `(row + 1, col - 1)` and `(row + 1, col + 1)` respectively. The root of the tree is at `(0, 0)`.

The **vertical order traversal** of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return *the **vertical order traversal** of the binary tree*.

##### LCP24.py	Number game

Little Code finds a number game at the entrance to the Autumn market. The organizer has a total of N counters, numbered from 0 to n-1. A number is displayed on each counter, and the button stores the displayed numbers in the array `nums` in ascending order of the counter number. There are two buttons on each counter to increment or decrement the displayed number by one. Button Each operation can select a counter, press the button of increment or decrement.

Please answer an array of length N with the i-th element `(0 ≤ i ≤ N)` means to operate the initial number of counters 0 to i to satisfy all conditions `nums[a]+1 == nums[a+1]` the minimum number of operations of. Answer correctly to enter the autumn market.

Since the answer can be large, mod 1,000,000,007 for each smallest operand.

### Utils

##### n_ary_tree.py	building the n-ary tree locally with the array

##### binary_tree.py	building the binary tree locally with the array