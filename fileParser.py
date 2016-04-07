from Bio import SeqIO

# in biopython tut examples file could be:
# "ls_orchid.fasta" for fastaParsing or
# "ls_orchid.gbk" for genbankParsing

def fastaPrinter(file):
	for seq_record in SeqIO.parse(file, "fasta"):
		print(seq_record.id)
		print(repr(seq_record.seq))
		print(len(seq_record))

def genbankPrinter(file):
	for seq_record in SeqIO.parse(file, "genbank"):
		print(seq_record.id)
		print(repr(seq_record.seq))
		print(len(seq_record))

def fastaParse(file):
	fastaList = []
	for seq_record in SeqIO.parse(file, "fasta"):
		fastaList.append(seq_record)
	return fastaList

def genbankParse(file):
	genbankList = []
	for seq_record in SeqIO.parse(file, "genbank"):
		genbankList.append(seq_record)
	return genbankList