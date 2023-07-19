import os


def runRaxMl(inputfile, prefix):
    # our data type is protein

    os.system("raxml-ng --all --model Blosum62+G --msa " + inputfile + " --prefix results/RaxMl/" + prefix +
              " --msa-format FASTA --tree pars{5} --seed 239 --threads 2 --force --bs-trees 100 --bs-metric fbp")


if __name__ == '__main__':
    runRaxMl(
        snakemake.input[0],
        snakemake.wildcards.position
    )
