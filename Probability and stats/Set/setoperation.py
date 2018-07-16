#length
print(len({1,2}))
#sum
print(sum({1,2}))
#min and max
print(min({1,2}))
print(max({1,2}))

#|AUB| =|A| +|B|-|A intersection B|
#for three set
#|AUBUC|=|A|+|B|+|C|-|A intersection C|-|A intersection B|-|B intersection C| +|A intersectetion B intersection C|
#for n set
#sum of all |Ai|-sum of all|Ai intersection Aj|+(-1)^n-1|intersectin of all Ai|

#|AxB|=|BxA|=|A|x|B|

#cartesian power is product of itself multiple time
#eg |A|^n=|A|x.......n
#in Power set P(s) that is power of subset IS ALSO A SET
#|P(S)|=2^|S|
#In fuction we have
#function from a to b
#|b^|a||=|b|^|a|
#implication in python
import itertools
print(set(itertools.product({2,3,4},repeat=2)))


#double exponential
#ps   2^(2^n)
#function from 2^n to 2
#function 2^(2^n)
#example n binary input and one binary output
#implement in function 2^(2^n)

#to solve a problem like for sequence of
#two digit without q
#we have 26+26-1=|A|+|B|-|A intersection B|
#25^2-52-1

#but it is fine with number like 4 digit number 
#with non 0
#9^4

#proper set if a set contains in other set 
#all value inside but not similar 



#find the proper subset of 5 element
#However, you only want to know the number of proper subsets, the power set contains all valid subsets. There is only 1 subset of A we don’t want to use and that’s the one that’s equal to itself.
#2^5-1