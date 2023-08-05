from Bio import SeqIO


def get_selectedSeq(input_fasta_path, target_sequence_ids, output_fasta_path):
    # Iterate through the input FASTA file and extract the selected sequences
    selected_sequences = []
    with open(output_fasta_path, 'w') as output_fasta:
        for record in SeqIO.parse(input_fasta_path, 'fasta'):
            if record.id in target_sequence_ids:
                selected_sequences.append(record)
                SeqIO.write(record, output_fasta, 'fasta')

    print(
        f"Extracted {len(selected_sequences)} sequences and saved to '{output_fasta_path}'.")


# -----------------------------------
input_fasta_path = 'virusWholeGenome_alin_gblock.fasta'

# Group 1
target_sequence_ids = ['KJ473795-AB085735', 'KJ473796-AB085735', 'KJ473797-AB085735',
                       'KJ473798-AB085735', 'KJ473799-AB085735', 'KJ473800-AB085735']
output_fasta_path = 'AB085735.1_Miniopterus_fuliginosus.fasta'
get_selectedSeq(input_fasta_path, target_sequence_ids, output_fasta_path)

# Group 2
target_sequence_ids = ['EU420138-ON640726']
output_fasta_path = 'ON640726.1_Miniopterus_magnater.fasta'
get_selectedSeq(input_fasta_path, target_sequence_ids, output_fasta_path)

# Group 3
target_sequence_ids = ['MN996532-KP972690']
output_fasta_path = 'KP972690.1_Rhinolophus_affinis.fasta'
get_selectedSeq(input_fasta_path, target_sequence_ids, output_fasta_path)

# Group 4
target_sequence_ids = ['DQ022305-HM134917', 'DQ084199-HM134917', 'DQ084200-HM134917',
                       'FJ588686-HM134917', 'GQ153539-HM134917', 'GQ153540-HM134917',
                       'GQ153541-HM134917', 'GQ153542-HM134917', 'GQ153543-HM134917',
                       'GQ153544-HM134917', 'GQ153545-HM134917', 'GQ153546-HM134917',
                       'GQ153547-HM134917', 'GQ153548-HM134917', 'KC881005-HM134917',
                       'KC881006-HM134917', 'KF367457-HM134917', 'KJ473814-HM134917',
                       'KJ473815-HM134917', 'KJ473816-HM134917', 'KT444582-HM134917',
                       'KY417143-HM134917', 'KY417144-HM134917', 'KY417146-HM134917',
                       'KY417147-HM134917', 'KY417148-HM134917', 'KY417149-HM134917',
                       'KY417150-HM134917', 'KY417151-HM134917', 'KY417152-HM134917',
                       'KY770858-HM134917', 'KY770859-HM134917', 'MG772933-HM134917',
                       'MG772934-HM134917']
output_fasta_path = 'HM134917.1_Rhinolophus_sinicus.fasta'
get_selectedSeq(input_fasta_path, target_sequence_ids, output_fasta_path)

# Group 5
target_sequence_ids = ['DQ412043-KX261916', 'DQ648857-KX261916']
output_fasta_path = 'KX261916.1_Rhinolophus_macrotis.fasta'
get_selectedSeq(input_fasta_path, target_sequence_ids, output_fasta_path)

# Group 6
target_sequence_ids = ['GU190215-MZ936290', 'NC_014470-MZ936290']
output_fasta_path = 'MZ936290.1_Rhinolophus_blasii.fasta'
get_selectedSeq(input_fasta_path, target_sequence_ids, output_fasta_path)

# Group 7
target_sequence_ids = ['JX993987-ON012504']
output_fasta_path = 'ON012504.1_Rhinolophus_pusillus.fasta'
get_selectedSeq(input_fasta_path, target_sequence_ids, output_fasta_path)
