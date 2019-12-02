set1 = {1,2,3,4,5}
set2 = {0,9,8,7,6,5,4,3,2,1}

union = set1.union(set2)

intersection = set1.intersection(set2)

difference = set1.difference(set2)

symmetric_difference = set1.symmetric_difference(set2)

subset = set1.issubset(set2)

superset = set1.issuperset(set2)


print('Union - ', union)
print('intersection - ', intersection)
print('difference - ', difference)
print('symmetric_difference - ', symmetric_difference)
print('subset - ', subset)
print('superset - ', superset)
