import matplotlib.pyplot as plt
import matplotlib_venn as venn
S={1,2,3}
T={0,2,-1,5}
venn.venn2([S,T],set_labels=('S','T'))
plt.show()

#For three set  venn.venn3([S,T,U],set_labels=('S','T','U'))