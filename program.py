
def sum67(nums):
    print([i for i in nums if i == 6])
    return sum(nums) - 13/6 * sum([i for i in nums if i == 6])

print(sum67([1,2,3,4,6,7,12]))
#print([[ (x == y and 1 or 0) for x in range(4) for i in range(4)] for y in range(4) ] + [[ (i == y and 1 or 0) for x in range(4) for i in range(4)] for y in range(4) ] + [[ ( ( abs(x - 1) <= 1 and abs(y - y2) <= 1 and not (abs(x - 1) == 0 and abs(y - y2) == 0) ) and 1 or 0) for x in range(4)  for y in range(4)] for y2 in range(1, 3) ] + [[ ( ( abs(x - 2) <= 1 and abs(y - y2) <= 1 and not (abs(x - 2) == 0 and abs(y - y2) == 0) ) and 1 or 0) for x in range(4)  for y in range(4)] for y2 in range(1, 3) ] + [[ ( ( abs(x - x2) == 1 or abs(x - x2) == 0 and (y == 0 or y == 3)) and 1 or 0) for x in range(4)  for y in range(4)] for x2 in range(1, 3) ] + [[ ( ( abs(y - y2) == 1 or abs(y - y2) == 0 and (x == 0 or x == 3)) and 1 or 0) for x in range(4)  for y in range(4)] for y2 in range(1, 3) ])
