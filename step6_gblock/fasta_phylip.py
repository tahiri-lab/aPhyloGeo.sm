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


# Example usage
# input_fa = "./data_genomeSeq/2Gblocks/Gblocks_Cleaned_sequences.fasta"
# output_phy = "./data_genomeSeq/2Gblocks/Gblocks_Cleaned_sequences.phy"

input_fa_bat = "./aln_host_paco.fas"
output_phy_bat = "./1aln_host_paco.phylip"

fasta_to_phylip(input_fa_bat, output_phy_bat)

input_fa_orf1ab = "./orf1ab_paco/aln_orf1ab.fasta"
output_phy_orf1ab = "./1aln_orf1ab.phylip"

fasta_to_phylip(input_fa_orf1ab, output_phy_orf1ab)

input_fa_spike = "./spike_paco/aln_spike.fasta"
output_phy_spike = "./1aln_spike.phylip"

fasta_to_phylip(input_fa_spike, output_phy_spike)
