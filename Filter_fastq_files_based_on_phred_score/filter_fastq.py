#!/usr/bin/python3
__author__ = "Vijay Lakhujani"
__credits__ = ["Vijay Lakhujani"]
__version__ = "1.0"
__email__ = "lakhjanivijay@gmail.com"
__status__ = "done"

from Bio import SeqIO

input_file=open("test.fastq")

quality_score=input("Enter your quality threshold score: ")
read_percentage=input("Enter your threshold for no of reads: ")

count=0

for record in SeqIO.parse(input_file, "fastq"):
    scores=record.letter_annotations["phred_quality"]
    good=0
    for entry in scores:
        if entry>=quality_score:
            good+=1
    if float(good) / len(scores) >= read_percentage:
        count += 1
print count
