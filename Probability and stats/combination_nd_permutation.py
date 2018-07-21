#Normal combination have nCr
#other approach is to think outside circle
#i.e summation of i=0 to n (n i)=2^n
#i.e summation of i=0 to n-1 (n  i)=2^n -1

#Pascals Identity
#(n+1 k)=(n k)+(n  k-1)

#multinomial
"""Anagrams no. or how many times different 
combination can be made from different set
Eg: MISSISSIPPI
sequence over {M,I,S,P}  
letter M,I,S,P
#times 1,4,4,2  so total length=11

hence we have (11   1,4,4,2)=11!/(1!*4!*4!*2)=34650"""
#eg: (x+y+z)^2=(2!   2!,0!,0!)x^2+(2! 0!,0!,2!)+y^2......like that but below should be sum as above


#When we have to find the number of ways 
#in which k number should be used to find 
#sum as n
#we have formula (n-1  k-1) i.e n-1 C k-1
#eg: 8 as a sum of 4 positive integer
#(8-1  4-1)=(7 3)=35

#Any sum to n when n=3  we have 2^(n-1)=2^2=4

#For non negative number we have (n+k-1   k-1)

#for unique example letter of 4 from 26 letter
# 26^4/4!

#number of non negative number when sum<=n when k is there
#formula= (n+k  k)



#nICE QUESTION
"""No. of slots = 8
No. of cars = 6

6 cars in 8 slots can be arranged in 8C6 ways. 
8C6 = 28.

Now, these 6 cars can be arranged in 6! ways.

Therefore the answer you're looking for is 
28 x 6! = 20,160 ways."""

import itertools


#permutations sample
A={1,2,3}
print(set(itertools.permutations(A)))

#For k items
k=2
print(set(itertools.permutations(A,k)))

#For Binomial Coefficient that is nCk
from scipy.special import binom
print(binom(6,2))

#For combinations

print(set(itertools.combinations(A,k)))
