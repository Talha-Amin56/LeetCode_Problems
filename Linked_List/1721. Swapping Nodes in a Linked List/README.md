# Swap Nodes in Linked List

## Problem Description
You are given the head of a linked list and an integer `k`. The task is to return the head of the linked list after swapping the values of the `k`th node from the beginning and the `k`th node from the end (the list is 1-indexed).

### Example 1
**Input:**  
`head = [1,2,3,4,5]`, `k = 2`  
**Output:**  
`[1,4,3,2,5]`

### Example 2
**Input:**  
`head = [7,9,6,6,7,8,3,0,9,5]`, `k = 5`  
**Output:**  
`[7,9,6,6,8,7,3,0,9,5]`

## Constraints
- The number of nodes in the list is `n`.
- `1 <= k <= n <= 10^5`
- `0 <= Node.val <= 100`

## Objective
Write a function that swaps the values of the `k`th node from the beginning and the `k`th node from the end in a given linked list and returns the modified list.

## Requirements
- Efficiently handle large linked lists with up to `10^5` nodes.
