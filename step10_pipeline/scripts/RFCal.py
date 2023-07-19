import os
from csv import writer


def addToCsv(window_pos, normalized_RF, output_csv):
    list = [window_pos, normalized_RF]
    with open(output_csv, 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(list)
        f_object.close()


def rfFilter(file_seqTree, file_refTree, ete3_output, window_pos):
    # if file_seqTree is empty, it means bootstrap < threshold

    os.system("rf " + file_seqTree + " " + file_refTree + " > " + ete3_output)
    with open(ete3_output, 'r') as file:
        normalized_rf = file.read().rstrip()

    output_csv = "results/output.csv"
    with open(output_csv, "a") as f:
        normalized_RF = normalized_rf
        addToCsv(window_pos, normalized_RF, output_csv)


if __name__ == '__main__':
    rfFilter(
        snakemake.input.seq_tree,
        snakemake.params.ref_tree,
        snakemake.output.ete3_output,
        snakemake.wildcards.position
    )
