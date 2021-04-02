import bisect

# It does tell you where to place the value but your list should be sorted. If your list has randomly things placed in it then module may lead to wrong conclusion. Also it doesn't give you any warning that your list is not sorted.
lis = [1,2,5,10,15,17,28,35,59,61]
print(bisect.bisect(lis, 55))

# Output:
# 8

import bisect

lis1 = ["a","e", "h", "m", "o", "s"]
print(bisect.bisect(lis1, "k"))

# Output:
# 3

import bisect

lis = [1,2,5,10,15,17,28,35,59,61]
print(bisect.bisect(lis, 55))
bisect.insort(lis, 55)
print(lis)

# Output:
# 8
# [1, 2, 5, 10, 15, 17, 28, 35, 55, 59, 61]

import bisect

lis1 = ["a","e", "h", "m", "o", "s"]
print(bisect.bisect(lis1, "k"))
bisect.insort(lis1, "k")
print(lis1)

# Output:
# 3
# ['a', 'e', 'h', 'k', 'm', 'o', 's']