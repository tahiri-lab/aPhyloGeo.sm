def fasta_to_phylip(fasta_file, phylip_file):
    sequences = {}
    max_length = 0

    # Read the FASTA file and store sequences
    with open(fasta_file, 'r') as f:
        header = ''
        sequence = ''
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if header != '':
                    sequences[header] = sequence
                    if len(sequence) > max_length:
                        max_length = len(sequence)
                header = line[1:]
                sequence = ''
            else:
                sequence += line
        sequences[header] = sequence
        if len(sequence) > max_length:
            max_length = len(sequence)

    # Write sequences in PHYLIP format
    with open(phylip_file, 'w') as f:
        f.write(f"{len(sequences)} {max_length}\n")
        for header, sequence in sequences.items():
            # Pad with gaps if necessary
            sequence += '-' * (max_length - len(sequence))
            f.write(f"{header} {sequence}\n")


input_fa_virus = "./1wholeGenomeConsGroupByHost.fasta"
output_phy_virus = "./1wholeGenomeConsGroupByHost.phylip"

fasta_to_phylip(input_fa_virus, output_phy_virus)
