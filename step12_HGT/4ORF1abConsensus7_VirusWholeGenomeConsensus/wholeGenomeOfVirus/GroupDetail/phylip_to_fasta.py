
phylip_file = 'virusWholeGenome_alin_gblock.phylip'
fasta_file = 'virusWholeGenome_alin_gblock.fasta'


sequences = {}

with open(phylip_file, 'r') as phylip:
    lines = phylip.readlines()
    num_sequences, seq_length = map(int, lines[0].split())

    for line in lines[1:]:
        parts = line.strip().split()
        sequence_id = parts[0]
        sequence = ''.join(parts[1:])
        sequences[sequence_id] = sequence

with open(fasta_file, 'w') as fasta:
    for sequence_id, sequence in sequences.items():
        fasta.write(f'>{sequence_id}\n{sequence}\n')

print(f'Converted {phylip_file} to {fasta_file}')
