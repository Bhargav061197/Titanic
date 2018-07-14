#cartesian product
from itertools import product
num1=set({1,2,3})
num2=set({4,5})
for i in product(num1,num2):
	print(i)
#Output
"""
(1, 4)
(1, 5)
(2, 4)
(2, 5)
(3, 4)
(3, 5)"""

#A delta B means (A-B) union (B-A)

#for union
#A | B
#for intersection
#A & B
# for (A U B)'  
#U-A & U-B   here U means universal
#for A'
#U-A