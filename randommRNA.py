from random import randint

num_ = int(input())

base = ['A', 'C', 'G', 'U']

mRNA = []

for i in range(num_) :
    randomint = randint(0,3)
    mRNA_ = base[randomint]
    mRNA.append(mRNA_)

for i in range(len(mRNA)) :
    print(mRNA[i], end='')