# import scikit-allel
import allel
# check which version is installed
print(allel.__version__)

callset = allel.read_vcf('ALL.chr22.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf')

sorted(callset.keys())