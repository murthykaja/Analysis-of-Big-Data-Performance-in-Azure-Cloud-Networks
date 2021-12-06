import os
import sys
# lines = ["trail_1_rtt.data"]
ans=[]
lines = []
for i in range(400):
    lines.append("trial_"+str(i+1)+"_rtt.data")
for l in lines:
    outter=[]
    with open(l) as f:
        outter = f.readlines()
    if len(outter)!=0:
        temp=0
        n=0
        for o in outter:
            temp+=float(o)
            n+=1
        ans.append(temp/n)
print(ans)
outFile = open("rtt.data",'w')
outFile.write('\n'.join(str(w1) for w1 in ans))
