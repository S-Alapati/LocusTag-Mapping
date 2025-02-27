# LocusTag-Mapping
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

brew install python3 bioawk blast
pip3 install pandas

