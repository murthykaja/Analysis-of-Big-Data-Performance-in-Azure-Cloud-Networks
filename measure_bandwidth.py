import os
import sys
#os.system("iperf3 -c 127.0.0.1 -i 1 -t 60 > log.out")
os.system("mkdir -p Bandwidth")
lines = []
inargs=sys.argv[1]
outargs=sys.argv[2]
infile=str(inargs)
with open(infile) as f:
    lines = f.readlines()
def parse_iperf3_output(line):
    if ("Gbits/sec" in line) or ("Mbits/sec" in line):
        lines=line.split(" ")
        for i in range(len(lines)):
            if "Gbits/sec" == lines[i]:
                return lines[i-1]
            if "Mbits/sec" ==lines[i]:
                return str(float(lines[i-1])/1000)
def parse_iperf3(lines):
    out = []
    #print(lines[3].split())
    #print(lines[10].split())
    for i in range(len(lines)):
        if  lines[i].split() == ["[","ID]","Interval","Transfer","Bitrate","Retr"]:
            out.append(parse_iperf3_output(lines[i+1]))
        #if "-" == lines[i][0]:
            #break
    return out
w = parse_iperf3(lines)
print(w)
path="Bandwidth/"+str(outargs)
outFile = open(path,'w')
outFile.write('\n'.join(str(w1) for w1 in w))
#for w1 in w:
#    outFile.write(w)
outFile.flush()
outFile.close()
