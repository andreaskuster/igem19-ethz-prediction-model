import Bio
from Bio import Entrez, SeqIO

_DEBUG = True

if _DEBUG:
    print("Library Version")
    print("biopython: {}".format(Bio.__version__))

Entrez.email = "igem@ethz.ch"
handle = Entrez.efetch(db="nucleotide", id="NC_001604.1", rettype="gb", retmode="text")

records = SeqIO.parse(handle, "gb")
for record in records:
    print("%s, length %i, with %i features" % (record.name, len(record), len(record.features)))
    print("DNA Sequence: {}".format(record.seq))
