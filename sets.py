set1 = { 10, 20, 30, 40, 50 , 'Dilen', 10}
print(set1)
print(type(set1))

set2 = { 20, 40, 60, 80, 100 }
print(set2)
print(set1.union(set2))
print(set1.intersection(set2))  
print(set1.difference(set2))
print(set2.difference(set1))

set3 = { 10, 20, 30 }
print(set1 | set3)