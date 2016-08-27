#!/usr/bin/python3
__author__ = "Vijay Lakhujani"
__credits__ = ["Vijay Lakhujani"]
__version__ = "1.0"
__email__ = "lakhjanivijay@gmail.com"
__status__ = "done"

from Bio import SeqIO

input_file=open("test.fastq")

quality_score=input("Enter your quality threshold score: ")

line_number,rec,count=0,0,0

for record in SeqIO.parse(input_file, "fastq"):
    rec+=1
    score=record.letter_annotations["phred_quality"]
    mean_score=sum(score)/len(score)
    if mean_score<quality_score:
        count+=1    
    score=0
    mean_score=0

print count
