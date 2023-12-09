# Solution to part 2

Starting from a `A` node, find a cycle that comes back to any `Z` node.

We are interested in the number of steps needed to come back to a `Z` node a second time since we left the `A` node.

Let's call this number X.

The solution to the puzzle in the LCM of all the `X` we found.

**Note**

The input is such that any `A` node leads to only one `Z` node, which makes the puzzle easier than it should be.

Our solution try to find all the shortest cycle for each `Z` node, and find the minimum LCM over all combinations. 
