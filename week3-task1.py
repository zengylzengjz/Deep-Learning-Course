import numpy as np
i=1
np.random.seed(612)
r = np.random.uniform(0,1,(1000,))
a = int(input("请输入一个1-100之间的整数："))
print("序号    索引值    随机数")
for d in r[0:1000:a]:
    print(i,end="\t")
    print(a*i,end="\t")
    print(d,end="\n")
    i+=1