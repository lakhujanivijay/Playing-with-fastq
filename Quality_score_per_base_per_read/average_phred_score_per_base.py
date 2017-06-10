from Bio import SeqIO
import getopt, sys, re

def usage():
    print "Usage: average_phred_score_per_base.py -i <input_fastq> -b <position of base as integer> "
    
try:
    options, remainder=getopt.getopt(sys.argv[1:], 'i:b:h')

except getopt.GetoptError as err:
    print str(err)
    usage()
    sys.exit()

for opt, arg in options:
    if opt in ('-i'):
        input_file=arg
    if opt in ('-h'):
        usage()
	sys.exit()
    elif opt in ('-b'):
        base=arg

pos=int(base)-1


for record in SeqIO.parse(input_file, "fastq"):
    score=record.letter_annotations["phred_quality"]
    if (int(base) <= len(score)) or (int(base) > 0):
        print "Mean of " + str(base) + "th base: " 
        qual.append(score[pos])
    else:
        print "\n Error: invalid position of base. Base position should be <= read length and > 0 !\n"
        sys.exit()

print sum(qual)/len(qual)

