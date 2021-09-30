# -*- coding: utf-8 -*-
"""
Created on Tue May 12 20:52:05 2020
"""

seq1 = input(str("Input Sequence 1: "))
seq2 = input(str("Input Sequence 2: "))


## Assuming two sequeces are aligned from beginning
## Append "-" to the end of the shorter sequence
if len(seq1) >= len(seq2):
    seq2 = seq2 + "-"*(len(seq1) - len(seq2) )
else:
    seq1 = seq1 + "-"*(len(seq2) - len(seq1) )
    
## matching the two sequences 
match="" #blank
for i in range (len(seq1)):			
    if seq1[i]==seq2[i]:				
        match=match+"|" #fill in the blank with |
    else:
        match=match+"X" #fill in the blank with X

## print two sequences and match        
print(seq1)
print(match)
print(seq2)
print()


####### Slice long sequence into multiple short sequences to print out
nchar = 60

length_seq = len(match)
index = 0
while index < length_seq:
    index_2 = index + nchar
    if index_2 > length_seq:
        index_2 = length_seq
        
    print(seq1[index:index_2])
    print(match[index:index_2])
    print(seq2[index:index_2])
    print()
        
    index = index_2
    

print("seq1 Consensus:", match.count("|"), "/", len(seq1))
print("seq2 consensus:", match.count("|"), "/", len(seq2))
