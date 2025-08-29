import re

# 1. Mengambil file original
file_path = './preproinsulin-seq.txt'
original_text= open(file_path).read()
print(original_text)

# 2. Cleaning text
clean_origin = re.sub(r"ORIGIN", "", original_text)
clean_text = re.sub(r"[^a-zA-Z]", "", clean_origin)
print(clean_text)
open("asam_amino_clean/preproinsulin-seq-clean.txt","x").write(clean_text)

#3. Menyiapkan file
file1= "asam_amino_clean/lsinsulin-seq-clean.txt"
file2= "asam_amino_clean/binsulin-seq-clean.txt"
file3= "asam_amino_clean/cinsulin-seq-clean.txt"
file4= "asam_amino_clean/ainsulin-seq-clean.txt"

#4. Bikin File
open(file1, "x").write(clean_text[:24])
open(file2, "x").write(clean_text[24:54])
open(file3, "x").write(clean_text[54:89])
open(file4, "x").write(clean_text[89:110])