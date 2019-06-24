#! /usr/bin/python

#Creating file with CDS of DEG genes
#Use the URGI IDs associated with each DEG in the Pearce et al (2014) Paper; see supplementary file 12870_2014_368_MOESM2_ESM.zip 
#504 DEG in URGI_ID file

import commands
import optparse
from optparse import OptionParser
import sets
import stat
import string

#pass FASTA files
def parse_FASTA(FASTA_file_name):
    FASTA_file = open(FASTA_file_name, 'r')
    gene_sequence = {}
    for line in FASTA_file.readlines():
        sline = string.split(line)
        if len(line) > 0:
            if line[0] == '>':
                fline = string.split(sline[0],"_")
                ID = fline[1]
                gene_sequence[ID] = ''
            else:
                gene_sequence[ID] += sline[0]
    FASTA_file.close()
    return gene_sequence



#import IDs
ID = {}
##open the list of URGI IDs
Pearce_iDs = open('URGI_ID_file.txt', 'r')
for line in Pearce_iDs.readlines():
    sline = string.split(line)
    ID[sline[0]] = {}
Pearce_iDs.close()

#Write all cds into new file: pearce_DEG_cds.fa
cds_file = open('pearce_DEG_cds.fa' , 'w')

for key, value in ID.iteritems() :
    newkey = string.split(key,"-l")
    nextkey = string.split(newkey[1], ":")
    lastkey = string.split(nextkey[0], "-")
    cdsLen = string.split(nextkey[1],"-")
    #print(cdsLen)
    #print("/nbi/group-data/ifs/NBI/Cristobal-Uauy/IWGSC_data/css_all/" + newkey[0] + ".fa.longerthan_200.fa")
	##extract the URGI contig sequence from the old CSS scaffolds (IWGSC 2014)
    cds = parse_FASTA("/nbi/group-data/ifs/NBI/Cristobal-Uauy/IWGSC_data/css_all/" + newkey[0] + ".fa.longerthan_200.fa")
    cds_file.write('>' + key + '\n')
    cds_file.write(cds[lastkey[2]][int(cdsLen[0]):int(cdsLen[1])] + '\n')
cds_file.close()
