# Locus Tag Mapping between Two Genomes

This repository contains a Python script to map locus tags between two genomes using their GenBank (GBFF) files and BLAST results.

---

## **Requirements**

1. **Python 3** (with `pandas` installed)
2. **Bioawk** (for extracting CDS sequences from GBFF files)
3. **BLAST+** (for sequence alignment)

### **Install Dependencies**

#### **On Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip bioawk ncbi-blast+
pip3 install pandas
```

#### **On macOS:**
```bash
brew install python3 bioawk blast
pip3 install pandas
```

---

## **Usage**

### **Clone this repository:**
```bash
git clone https://github.com/yourusername/locus-tag-mapping.git
cd locus-tag-mapping
```

### **Place your GBFF files in the repository directory:**
Rename them as `file1.gbff` and `file2.gbff`.

### **Run the script:**
```bash
python3 locustag_mapping.py
```

### **Output:**
The script will generate the following files:

- `cds1.fasta`: CDS sequences from `file1.gbff`.
- `cds2.fasta`: CDS sequences from `file2.gbff`.
- `blast1_vs_2.txt`: BLAST results of `cds1.fasta` vs `cds2.fasta`.
- `blast2_vs_1.txt`: BLAST results of `cds2.fasta` vs `cds1.fasta`.
- `locus_tag_mappings.tsv`: Mapped locus tags in TSV format.

---

## **Workflow**

1. Extract CDS sequences from GBFF files using Bioawk.
2. Create BLAST databases for both genomes.
3. Run reciprocal BLAST to find homologous sequences.
4. Identify reciprocal best hits (RBH) and map locus tags.

---

## **Example Output**

The output file `locus_tag_mappings.tsv` will look like this:

```
LocusTag1    LocusTag2
tag1_genome1 tag1_genome2
tag2_genome1 tag2_genome2
...
```

---

## **License**

This project is licensed under the MIT License. See the LICENSE file for details.

---

## **Contact**

For questions or issues, please open an issue on GitHub or contact [your email].

---

## **GitHub Repository Structure**

Your GitHub repository should look like this:
```
locus-tag-mapping/
├── locustag_mapping.py
├── README.md
├── file1.gbff
├── file2.gbff
├── cds1.fasta
├── cds2.fasta
├── blast1_vs_2.txt
├── blast2_vs_1.txt
└── locus_tag_mappings.tsv
```

---

## **How to Use**

1. Clone the repository.
2. Place your GBFF files (`file1.gbff` and `file2.gbff`) in the repository directory.
3. Run the script (`python3 locustag_mapping.py`).
4. Check the output files for results.


