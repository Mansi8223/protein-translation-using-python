#genetic code dictionary
import os;
os.chdir("E:\MANSI\work");
abc=open("genetic_code.txt","r")
pqr=abc.readlines();
abc.close();
genetic_code={};
for i in range(11,len(pqr[0])):
    aa=pqr[0][i];
    codon=pqr[2][i]+pqr[3][i]+ pqr[4][i];
    genetic_code[codon]=aa;
#print(genetic_code)

#sequence dictionary
import re;
sq=open("brca1.fasta","r");
seq=sq.readlines()
sq.close();
sequence={}
for i in seq:
    i=i.rstrip("\n");
    res=re.match('>',i)
    if(res):
        temporarykey=i;
        sequence[i]="";
    else:
        sequence[temporarykey]=sequence[temporarykey]+i;
#print(sequence)

#translation code
header=sequence.keys()
for j in header:
    myseq=sequence[j]
    aminoacid=""
    a=0;
    while(a<len(myseq)-2):
        mycodon = myseq[a]+myseq[a+1]+myseq[a+2]
        if(mycodon in genetic_code.keys()):
            aminoacid=aminoacid+genetic_code[mycodon]
        a=a+3;
    print(j + "\n" + myseq+ "\n\n" + aminoacid + "\n\n\n")


    
        

