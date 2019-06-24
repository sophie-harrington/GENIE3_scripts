#!/bin/bash
#SBATCH -p nbi-short # partition (queue)
#SBATCH -c 1 # number of cores
#SBATCH --mem=10000
#SBATCH -J blast
#SBATCH -o blast
#SBATCH -e blast
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=Anna.Backhaus@jic.ac.uk

##This script is for the BLAST between the Pearce DEG at 12 DAA against the HC and LC v1.1 CDS sequences

source blast+-2.2.30
user='/nbi/group-data/ifs/NBI/Cristobal-Uauy/Anna'

#blast against HC gene annotation
refseq='/nbi/group-data/ifs/NBI/Cristobal-Uauy/WGAv1.0/annotation/IWGSC_v1.1_HC_20170706_cds.fasta'
blastn -query $user/pearce_DEG_cds.fa -db $refseq -num_alignments 1 -outfmt 6 -out $user/Pearce_DEG_ID_translation_ref1_1

#Make refseq file for LC blast
makeblastdb -in /nbi/group-data/ifs/NBI/Cristobal-Uauy/WGAv1.0/annotation/IWGSC_v1.1_LC_20170706_cds.fasta -parse_seqids -dbtype nucl

#blast against LC gene annotation
refseq='/nbi/group-data/ifs/NBI/Cristobal-Uauy/WGAv1.0/annotation/IWGSC_v1.1_LC_20170706_cds.fasta'
blastn -query $user/pearce_DEG_cds.fa -db $refseq -num_alignments 1 -outfmt 6 -out $user/URGI_against_LC.txt
