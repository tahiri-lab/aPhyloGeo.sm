from Bio import SeqIO


def getSubseq(whole_seq_f, start_pos, end_pos):
    f = open(f'align{start_pos}_{end_pos}.fasta', 'w')

    for record in SeqIO.parse(whole_seq_f, "fasta"):
        f.write('>' + record.id + '\n')
        f.write(str(record.seq[start_pos:end_pos+1])+'\n')

        # print('>'+ record.id + '\n')
        # print(str(record.seq[28400:28551])+'\n')
    f.close()


whole_seq_f = "1aln_orf1ab_withID.fasta"

getSubseq(whole_seq_f, 520, 680)
getSubseq(whole_seq_f, 770, 870)
getSubseq(whole_seq_f, 2930, 3070)
getSubseq(whole_seq_f, 4910, 5080)
