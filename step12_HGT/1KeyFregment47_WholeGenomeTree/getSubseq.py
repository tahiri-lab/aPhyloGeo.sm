from Bio import SeqIO


def getSubseq(whole_seq_f, start_pos, end_pos):
    f = open(f'align{start_pos}_{end_pos}.fasta', 'w')

    for record in SeqIO.parse(whole_seq_f, "fasta"):
        f.write('>' + record.id + '\n')
        f.write(str(record.seq[start_pos:end_pos+1])+'\n')

        # print('>'+ record.id + '\n')
        # print(str(record.seq[28400:28551])+'\n')
    f.close()


# aln_orf1ab_f = "1aln_orf1ab_withID.fasta"

# getSubseq(aln_orf1ab_f, 360, 1390)
# getSubseq(aln_orf1ab_f, 550, 1610)
# getSubseq(aln_orf1ab_f, 680, 1680)
# getSubseq(aln_orf1ab_f, 700, 1710)
# getSubseq(aln_orf1ab_f, 2060, 3090)
# getSubseq(aln_orf1ab_f, 2130, 3250)

aln_spike_f = "1aln_spike_withID.fasta"

getSubseq(aln_spike_f, 10, 510)
getSubseq(aln_spike_f, 50, 560)
getSubseq(aln_spike_f, 170, 710)
getSubseq(aln_spike_f, 230, 730)
