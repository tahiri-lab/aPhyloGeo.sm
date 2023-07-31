from io import StringIO
from Bio import SeqIO
from Bio import Entrez
import os
import pandas as pd


def downFromNCBI(db_type, accession_list, file_name):
    Entrez.email = "806981384wl@gmail.com"  # Always tell NCBI who you are

    if not os.path.isfile(file_name):
        # Downloading...
        net_handle = Entrez.efetch(
            db=db_type, id=accession_list, rettype="fasta", retmode="text"
        )
        out_handle = open(file_name, "w")
        out_handle.write(net_handle.read())
        out_handle.close()
        net_handle.close()
        print("Saved")


df = pd.read_csv("id_info.csv")
accession_list = set(df.V_Accession_full)
# accession_list = set(df.Host_Accession)
print(accession_list)
print(len(accession_list))

file_name = "seq_full_47virus.fasta"
# file_name = "seq_cytb_bat.fasta"


downFromNCBI("nucleotide", accession_list, file_name)
