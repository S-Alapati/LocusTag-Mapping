import pandas as pd

def extract_cds_from_gbff(gbff_file, output_fasta):
    """
    Extract CDS sequences and locus tags from a GBFF file using Bioawk.
    """
    import subprocess
    # Run bioawk to extract CDS sequences
    command = f"bioawk -c genbank '{{if ($feature == \"CDS\") print \">\"$locus_tag\"\\n\"$seq}}' {gbff_file} > {output_fasta}"
    subprocess.run(command, shell=True, check=True)

def run_blast(query, db, output):
    """
    Run BLAST and save results in tabular format.
    """
    import subprocess
    command = f"blastn -query {query} -db {db} -outfmt 6 -out {output}"
    subprocess.run(command, shell=True, check=True)

def find_reciprocal_best_hits(blast1_to_2, blast2_to_1):
    """
    Find reciprocal best hits (RBH) between two BLAST result files.
    """
    # Load BLAST results
    blast1_to_2_df = pd.read_csv(blast1_to_2, sep='\t', header=None, 
                                 names=['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 
                                        'gapopen', 'qstart', 'qend', 'sstart', 'send', 
                                        'evalue', 'bitscore'])
    blast2_to_1_df = pd.read_csv(blast2_to_1, sep='\t', header=None, 
                                 names=['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 
                                        'gapopen', 'qstart', 'qend', 'sstart', 'send', 
                                        'evalue', 'bitscore'])

    # Get top hits for each query
    top_hits_1_to_2 = blast1_to_2_df.sort_values('bitscore', ascending=False).drop_duplicates('qseqid')
    top_hits_2_to_1 = blast2_to_1_df.sort_values('bitscore', ascending=False).drop_duplicates('qseqid')

    # Find reciprocal best hits
    rbh = []
    for idx, row in top_hits_1_to_2.iterrows():
        geneA = row['qseqid']  # Locus tag from genome 1
        geneB = row['sseqid']  # Locus tag from genome 2
        # Check if geneB's top hit is geneA
        if geneB in top_hits_2_to_1['qseqid'].values:
            if top_hits_2_to_1[top_hits_2_to_1['qseqid'] == geneB].iloc[0]['sseqid'] == geneA:
                rbh.append((geneA, geneB))  # Add reciprocal best hit to the list

    # Save mappings to a TSV file
    rbh_df = pd.DataFrame(rbh, columns=['LocusTag1', 'LocusTag2'])
    rbh_df.to_csv('locus_tag_mappings.tsv', sep='\t', index=False)

    print(f"Reciprocal best hits saved to 'locus_tag_mappings.tsv'. Found {len(rbh)} mappings.")

if __name__ == "__main__":
    # Input GBFF files
    gbff_file1 = "file1.gbff"
    gbff_file2 = "file2.gbff"

    # Output files
    cds1_fasta = "cds1.fasta"
    cds2_fasta = "cds2.fasta"
    blast1_vs_2 = "blast1_vs_2.txt"
    blast2_vs_1 = "blast2_vs_1.txt"

    # Step 1: Extract CDS sequences from GBFF files
    print("Extracting CDS sequences from GBFF files...")
    extract_cds_from_gbff(gbff_file1, cds1_fasta)
    extract_cds_from_gbff(gbff_file2, cds2_fasta)

    # Step 2: Create BLAST databases
    print("Creating BLAST databases...")
    import subprocess
    subprocess.run(f"makeblastdb -in {cds1_fasta} -dbtype nucl -out db1", shell=True, check=True)
    subprocess.run(f"makeblastdb -in {cds2_fasta} -dbtype nucl -out db2", shell=True, check=True)

    # Step 3: Run reciprocal BLAST
    print("Running BLAST...")
    run_blast(cds1_fasta, "db2", blast1_vs_2)
    run_blast(cds2_fasta, "db1", blast2_vs_1)

    # Step 4: Find reciprocal best hits
    print("Finding reciprocal best hits...")
    find_reciprocal_best_hits(blast1_vs_2, blast2_vs_1)
