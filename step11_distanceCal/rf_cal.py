import os
from csv import writer
import subprocess


def addToCsv(window_pos, normalized_RF, output_csv):
    list = [window_pos, normalized_RF]
    with open(output_csv, 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(list)
        f_object.close()


def rfCal(file_seqTree, file_refTree):
    command = "rf " + file_seqTree + " " + file_refTree
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    return_code = process.returncode

    if return_code != 0:
        # Handle any errors if needed
        print("Error occurred while running 'rf' command.")
        print("Stderr:", stderr.decode())
        return None

    output_lines = stdout.decode().splitlines()[0]
    return output_lines


def rfForWindows(folder_seqTree, file_refTree, outputCSV):

    columns_name = ["window_pos", "normalized_RF"]
    with open(outputCSV, 'w') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(columns_name)
        f_object.close()

    seqTree_lst = os.listdir(folder_seqTree)

    for fileName in seqTree_lst:
        file_seqTree = folder_seqTree + '/' + fileName
        normalized_RF = rfCal(file_seqTree, file_refTree)
        window_pos = fileName.split('.')[0]
        # print(window_pos, normalized_RF)
        addToCsv(window_pos, normalized_RF, outputCSV)
    print("RF calculation is finished")


# ----------------------------------------------------------
# seq tree folder
trees_folder_spike = '../step10_pipeline/output_spike_100_10step/RAxML'
trees_folder_pp1ab = '../step10_pipeline/output_pp1ab_100_10step/RAxML'
# reference file
file_refTree = 'hostTree.newick'
# output file
spike_rf_csv = "rf_spike.csv"
pp1ab_rf_csv = "rf_pp1ab.csv"
# print(os.listdir(trees_folder_pp1ab))


rfForWindows(trees_folder_spike, file_refTree, spike_rf_csv)
rfForWindows(trees_folder_pp1ab, file_refTree, pp1ab_rf_csv)
