!pip install biopython
from Bio import Align
aligner = Align.PairwiseAligner(match_score=1.0)

#Defining the sequences for alignment

seq_a = "GGTTAACCCCCCAAT"
seq_b = "GGTTAACCCCCCAAT"

#Call the Aligner to assign scores

score=aligner.score(seq_a, seq_b)

#To print the align score
print(f"the alignment score{score}")
#For the exact alignment map in global alignment

Alignments = aligner.align(seq_a, seq_b)

#Using for loop

for alignment in Alignments:
    print(alignment)
  #For the alignment score in local alignment

Align.mode="Local"

seq_1 = 'AATTCCGG'
seq_2 = 'ATTCG'
Local_score = aligner.score(seq_1,seq_2)
print(f"the local alignment score is {Local_score}")

#For the alignment map in local alignment

Align_Local = aligner.align(seq_1,seq_2)

for alignment in Align_Local:
    print(alignment)
