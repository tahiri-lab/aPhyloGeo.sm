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


# df = pd.read_csv("filterdByPACo.csv")
# orf1ab_paco1 = set(df.ORF1ab)
# orf1ab_paco = list(filter(lambda a: a != 'HAVE 1a &1b', orf1ab_paco1))
# spike_paco = set(df.spike)


# print(orf1ab_paco1)
# print(len(orf1ab_paco1))
# print(orf1ab_paco)
# print(len(orf1ab_paco))
# print(spike_paco)
# print(len(spike_paco))
# print('-----------------------------------------------------------------')
# orf1ab_paco_f = "orf1ab_paco.fasta"
# spike_paco_f = "spike_paco.fasta"
# downFromNCBI("protein", orf1ab_paco, orf1ab_paco_f)
# downFromNCBI("protein", spike_paco, spike_paco_f)

# print("===================================================================================================")


# df1 = pd.read_csv("filteredByParaFit.csv")
# orf1ab_ParaFit1 = set(df1.ORF1ab)
# orf1ab_ParaFit = list(filter(lambda a: a != 'HAVE 1a &1b', orf1ab_ParaFit1))
# spike_ParaFit = set(df1.spike)


# print(orf1ab_ParaFit1)
# print(len(orf1ab_ParaFit1))
# print(orf1ab_ParaFit)
# print(len(orf1ab_ParaFit))
# print(spike_ParaFit)
# print(len(spike_ParaFit))
# print('-----------------------------------------------------------------')
# orf1ab_ParaFit_f = "orf1ab_ParaFit.fasta"
# spike_ParaFit_f = "spike_ParaFit.fasta"
# downFromNCBI("protein", orf1ab_ParaFit, orf1ab_ParaFit_f)
# downFromNCBI("protein", spike_ParaFit, spike_ParaFit_f)

# print("===================================================================================================")
# For Host

paco = pd.read_csv("filterdByPACo.csv")
paco_host_lt = set(paco.Host_Accession.to_list())
print("PACo, number of related host", len(paco_host_lt))
print("Host List: ", paco_host_lt)

host_f = "host_paco.fasta"
downFromNCBI("nucleotide", paco_host_lt, host_f)
