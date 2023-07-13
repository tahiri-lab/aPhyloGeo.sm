from Bio import SeqIO
import pandas as pd

# relabel the id of aln_orf1ab
# remove the description


def relabel(in_file, out_file, id_dict):
    with open(out_file, "w") as outputs:
        for r in SeqIO.parse(in_file, "fasta"):
            if "_" in r.id:
                r.id = id_dict[r.id]
            else:
                key = r.id.split('.')[0]
                r.id = id_dict[key]
            r.description = ""
            SeqIO.write(r, outputs, "fasta")
    print("done")


df = pd.read_csv("id_info.csv")
id_orf1ab = dict(zip(df['ORF1ab'], df['Id']))
id_spike = dict(zip(df['spike'], df['Id']))
id_host = dict(zip(df['Host_Accession'], df['Id']))

orf1ab_fasta = "aln_orf1ab.fasta"
spike_fasta = "aln_spike.fasta"
host_fasta = "aln_host_paco.fasta"

orf1ab_output = "1aln_orf1ab_withID.fasta"
spike_output = "1aln_spike_withID.fasta"
host_output = "1aln_host_withID.fasta"

relabel(orf1ab_fasta, orf1ab_output, id_orf1ab)
# relabel(spike_fasta, spike_output, id_spike)
# relabel(host_fasta, host_output, id_host)
