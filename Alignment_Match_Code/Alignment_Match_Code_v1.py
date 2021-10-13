# -*- coding: utf-8 -*-


import streamlit as st
from PIL import Image

##############
#Page Title##
############

image = Image.open("DNA.jpg")

st.image(image, use_column_width=True)

st.write("""
# Bioinformatic tools for working with Nucleotides
By Justinkxc

1. Conversion of DNA to RNA
2. Obtaining the reverse complement of a DNA sequence
3. Obtaining the nucleotide contents of a DNA sequence
4. Alignment of 2 sequences

***
""")



################
#--DNA to RNA--#
################

import re

st.header("1. Converting DNA to RNA")

DNA = ">\nATCGTAGCATCGATCGACTAGCATCGATCGACTAGCTAGCTACGATCGATCGATATCGAGCAGCAT"
DNAseq = st.text_area("DNA Sequence", DNA, height=250)
DNAseq = DNA.splitlines()
RNA = re.sub("T", "U", DNA)
RNAseq = st.text_area("RNA Sequence", RNA, height = 250)
print("RNA Seq:", RNA)

st.write("""
***
""")


########################
#--Reverse Complement--#
########################

st.header("2. DNA Reverse Complement")

import re

seqx = "ATCGTAGCATCGATCGACTAGCATCGATCGACTAGCTAGCTACGATCGATCGATATCGAGCAGCAT"

#--converting seq to complement--#
seqx = re.sub("T", "U", seqx)
seqx = re.sub("A", "T", seqx)
seqx = re.sub("U", "A", seqx)
seqx = re.sub("G", "X", seqx)
seqx = re.sub("C", "G", seqx)
seqx = re.sub("X", "C", seqx)

seqx_textbox = st.text_area("DNA Sequence", seqx, height = 250)

revseqx = seqx[::-1]
print("Reverse complement of seq = 5'", revseqx, "3'")

revseqx_textbox = st.text_area("Reverse Complement", revseqx, height = 250)

st.write("""
***
""")

####################
#Nucleotide Content#
####################

st.header("3. Nucleotide Content")

import pandas as pd
import altair as alt

seqcount = ">DNA Query \nATCGATTGATGTAGCTACGATCGACGATATAAAATAGTAAAA"

sequence = st.text_area("Sequence input", seqcount, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

def nucleotide_count(seq1):
    x = dict([
        ("A", seqcount.count("A")),
        ("T", seqcount.count("T")),
        ("C", seqcount.count("C")),
        ("G", seqcount.count("G"))
        ])
    return x

y = nucleotide_count(seqcount)
GC = ((seqcount.count("G")) + seqcount.count("C")) / len(seqcount) * 100

st.subheader("Nucleotide Composition")
st.write("There are " + str(y["A"]) + ' adenine (A) nucleotides')
st.write("There are " + str(y["T"]) + ' thymine (T) nucleotides')
st.write("There are " + str(y["C"]) + ' cytosine (C) nucleotides')
st.write("There are " + str(y["G"]) + ' guanine (G) nucleotides')
st.write("GC content: ", GC, "%")

st.subheader("Data Frame")
df = pd.DataFrame.from_dict(y,orient = "index")
df = df.rename({0: "count"}, axis = "columns")
df.reset_index(inplace = True)
df = df.rename(columns = {"index" : "nucleotide"})
st.write(df)

st.subheader("Bar Chart")
z = alt.Chart(df).mark_bar().encode(
    x = "nucleotide",
    y = "count"
)
z = z.properties(height = 150, width = alt.Step(80))
st.write(z)

st.write("""
***
""")

########################
#--Sequence Alignment--#
########################

st.header("4. Sequence Alignment")

seq1 = "\nATCGATTGATGTAGCTACGATCGACGATATAAAATCGATCGACTGACTAGCGTCTGCGCGTCTGCTGCATAGACTAGCTAGCTAGCACGGAGACTAGCTAATCGACTAAAA"
seq2 = "\nATCGATTGATGTAGCTACGATCATATCAGCTAGCATCGATCGATCGACAGCGACGACGACGTACGTAGCTACGATCGACGCGTAGTCGTCTAGCTCTGACT"

seq1_text = st.text_area("DNA Sequence 1", seq1 , height=250)
seq2_text = st.text_area("DNA Sequence 2", seq2, height=250)

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
#print(seq1)
#print(match)
#print(seq2)
#print()

st.subheader("Alignment")
#--Slice long sequence into multiple short sequences to print out--#
nchar = 60

length_seq = len(match)
index = 0
while index < length_seq:
    index_2 = index + nchar
    if index_2 > length_seq:
        index_2 = length_seq

    st.write("Seq 1", x_s1[index:index_2])
    st.write(match[index:index_2])
    st.write("Seq 2", x_s2[index:index_2])
    st.write()

    index = index_2

st.subheader("Overlap")
# Calculate percentage
percent_1 = match.count("|") / len(seq1) * 100
percent_2 = match.count("|") / len(seq2) * 100


st.write("seq1 Consensus:", match.count("|"), "/", len(seq1))
st.write("% Overlap of Seq1:", str(percent_1), "%")
st.write()
st.write("seq2 consensus:", match.count("|"), "/", len(seq2))
st.write("% Overlap of Seq2:", str(percent_2), "%")
