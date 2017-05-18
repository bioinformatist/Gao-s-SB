from Bio import Entrez
from Bio import SeqIO

Entrez.email = "sun_yu@mail.nankai.edu.cn"

accession_list = ['NC_001665.2','NC_005089.1']


handle = Entrez.efetch(db="nuccore", rettype = 'gb', id=accession_list)
records = list(SeqIO.parse(handle, "gb"))
print(records[1].seq[15355:16299])
