This program takes a fastq file as an input and gives out the mean phred score for the
user defined base position.

A mean of phred scores will be calculated for user provided base position across all the
reads in the user provided fastq file as provided by "Per Base Sequence Quality" metric
of FastQC tool.

Usage:
average_phred_score_per_base.py -i <input_fastq> -b <position of base as integer>

Example:
average_phred_score_per_base.py -i input_fastq -b 30

Output Example:
Mean of 30th base: 23

Dependencies:
Biopython

