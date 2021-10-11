# -*- coding: utf-8 -*-

"""
###############
#--DNA<->RNA--#
###############
import re

seq1 = input(str("Input Sequence 1: "))

#--Converting DNA to RNA--#
DNA = input("DNA Seq: ")
RNA = re.sub("T", "U", DNA)
print("RNA Seq:", RNA)


#--Converting RNA to DNA--#
RNA = input("DNA Seq: ")
DNA = re.sub("T", "U", RNA)
print("RNA Seq:", DNA)
"""

"""
########################
#--Reverse Complement--#
########################
import re

seq1 = input(str("Input DNA Sequence: "))

#--converting seq1 to complement--#
seq1 = re.sub("T", "U", seq1)
seq1 = re.sub("A", "T", seq1)
seq1 = re.sub("U", "A", seq1)
seq1 = re.sub("G", "X", seq1)
seq1 = re.sub("C", "G", seq1)
seq1 = re.sub("X", "C", seq1)

revseq1 = seq1[::-1]
print("Reverse complement of seq1 = 5'", revseq1, "3'")
"""

"""
####################
#Nucleotide Content#
####################

import pandas as pd
import altair as alt

seq1 = input(str("Input DNA Sequence: "))

def nucleotide_count(seq1):
    x = dict([
        ("A", seq1.count("A")),
        ("T", seq1.count("T")),
        ("C", seq1.count("C")),
        ("G", seq1.count("G"))
        ])
    return x

y = nucleotide_count(seq1)

df = pd.DataFrame.from_dict(y,orient = "index")
df = df.rename({0: "count"}, axis = "columns")
df.reset_index(inplace = True)
df = df.rename(columns = {"index" : "nucleotide"})
print(df)

GC = ((seq1.count("G")) + seq1.count("C")) / len(seq1) * 100
print("GC content: ", GC, "%")

z = alt.Chart(df).mark_bar().encode(
    x = "nucleotide",
    y = "count"
).show()
z = p.properties(height = 150, width = alt.Step(80))
print(z)
"""


########################
#--Sequence Alignment--#
########################

seq1 = input(str("Input Sequence 1: "))
seq2 = input(str("Input Sequence 2: "))

#--Assuming two sequeces are aligned from beginning--#
#--Append "-" to the end of the shorter sequence--#
if len(seq1) >= len(seq2):
    x_s2 = seq2 + "-" * (len(seq1) - len(seq2))
    x_s1 = seq1
else:
    x_s1 = seq1 + "-" * (len(seq2) - len(seq1))
    x_s2 = seq2

#--matching the two sequences--#
match = ""  # blank
for i in range(len(x_s1)):
    if x_s1[i] == x_s2[i]:
        match = match + "|"  # fill in the blank with |
    else:
        match = match + "X"  # fill in the blank with X

#--print two sequences and match--#
print(seq1)
print(match)
print(seq2)
print()

#--Slice long sequence into multiple short sequences to print out--#
nchar = 60

length_seq = len(match)
index = 0
while index < length_seq:
    index_2 = index + nchar
    if index_2 > length_seq:
        index_2 = length_seq

    print(x_s1[index:index_2])
    print(match[index:index_2])
    print(x_s2[index:index_2])
    print()

    index = index_2

# Calculate percentage
percent_1 = match.count("|") / len(seq1) * 100
percent_2 = match.count("|") / len(seq2) * 100


print("seq1 Consensus:", match.count("|"), "/", len(seq1))
print("% Overlap of Seq1:", str(percent_1), "%")
print()
print("seq2 consensus:", match.count("|"), "/", len(seq2))
print("% Overlap of Seq2:", str(percent_2), "%")


