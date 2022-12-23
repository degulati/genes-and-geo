import os
import sys

vcf_filename = "ALL.chr22.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf"
panel_filename = "phase1_integrated_calls.20101123.ALL.panel"

from pysam import VariantFile
vcf_in = VariantFile(vcf_filename)
# vcf_out = VariantFile('-', 'w', header=vcf_in.header)

# print(vcf_in.header)

for rec in vcf_in.fetch():
    #vcf_out.write(rec
    #print(rec)
    #print(list(rec.samples))
    try: 
        print(rec.ref)
        print(rec.alts)
        alts = [alt for alt in rec.alts]
        print(alts)
        # print(list(rec.format))
        # print(list(rec.samples))

        # print(rec.samples.values())
        
        genotypes = [s['GT'] for s in rec.samples.values()]
        print(genotypes)
        # flush output here to force SIGPIPE to be triggered
        # while inside this try block.
        sys.stdout.flush()

    except BrokenPipeError:
        # Python flushes standard streams on exit; redirect remaining output
        # to devnull to avoid another BrokenPipeError at shutdown
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        sys.exit(1)  # Python exits with error code 1 on EPIPE

    # print(rec.ref)
    # print(rec.alt)
    break
# print('hello ')
# vcf_in.close()