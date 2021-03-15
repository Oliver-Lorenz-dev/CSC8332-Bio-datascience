#!/usr/bin/env python3

import pandas as pd
import gzip

input_file = gzip.open("/opt/data/report_pfam/pfam-a.seed.stk.gz")
output = gzip.open("/home/c0059478/Documents/8332/data/proteins.csv.gz", "wt")
# write header
output.write("pfam_id,pfam_accession,uniprot_id,sequence\n")

for line in input_file:
    line = line.decode("utf-8", errors="ignore")
    if line.startswith("#=GF ID"):
        pfam_id = line.split()[2]
    if line.startswith("#=GF AC"):
        pfam_accession = line.split()[2]
    if line[0] not in "#/":
        uniprot_id, sequence = line.split()
        uniprot_id, _ = uniprot_id.split("/")
        output.write(f"{pfam_id},{pfam_accession},{uniprot_id},{sequence}\n")
output.close()

protein_data = pd.read_csv("/home/c0059478/Documents/8332/data/proteins.csv.gz")

# select top 20 familes
top = protein_data.pfam_id.value_counts()[:6].index
selection = protein_data.pfam_id.isin(top)
protein_data_final = protein_data[selection]

# remove . from sequence
protein_data_final.sequence = protein_data_final.sequence.str.replace('.', '')

protein_data_final.to_csv("/home/c0059478/Documents/8332/data/proteins.csv.gz", compression='gzip',header=True, index = False)


