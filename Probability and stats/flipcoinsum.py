import numpy as np
x=2*(np.random.rand(100000,1)>0.5)-1
S=np.sum(x,axis=0)
print(S)
#as total sum wont exceed around 1400
#2*boolean mask 
#so all are 0 and 2 then -1 so we get 1 and -1 combo
# as |Sk|>4*sqrt(k)  if k-->infinity 4/sqrt(k)--->0
#hence at k--->infinity sk/k--->0
#as it is centered around 0

"""AS probability theory is a math framework 
for computing the probability of complex events"""
#statistics is about analyzing real world data 
#and drawing conclusions