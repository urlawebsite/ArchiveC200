from time import perf_counter, time
import random as rn
import math


# The dictionary for the transation (this dictionary will store the DAN-amino acids mapping)
aa_d = {}

# the FASTA file (this list will store the FASTA file)
DNA_d = []

# the correct translation (is given for cross-checking)
actual = "PLHSPHPANFCVFSRD-IPYSEHLRRGALDPGRFRGPRSELSEIERARSRDLRRGPGPPGGEAAARRPLEAAGPLAGPRRRSGVAGRGGFQRGDGAVRGGPGAGARPVEEAGQQRRRLHDRGPGKVRQAGRPRPQGPSLPKPPGRASPTFLSQDLPGFPRHEDLLLPPGPEPRLLTSQSPRPEGGGRAEPRRGAPGRPTPRAVRAEPPARVPAASGPGQLPGERLPCWAPVPGRAPAGWVRGACGAGAGE-ALSARRSSWATACW-PSPGTTPETSAPRCRRRWTSS-ATLSRRWFPSTAELWVGGRGIPRRPSPCLSKASPRSSLLAVLSRGQDARGRR"

#INPUT name of amino acid file (make sure that you keep the amino_acids.txt under Assignment8 folder)
#RETURN a dictionary 
#Key is a tuple (c0, c1, ... , cn) where ci are codons
#Value is a pair [name, abbreviation] for the amino acid
#make sure to close the file after reading it
def get_amino_acids(name):
    pass

#INPUT file name of the DNA file (make sure that you keep the DNA.txt under Assignment8 folder)
#RETURN a list [header, DNA]
#header is first line in the file
#DNA is a string of letters from remainder of file
#no whitespace
#make sure to close the file
def get_DNA(name):
    pass

#INPUT FAST file
#RETURN a string representing the protein (convert the DNA to amino acids)
#using the dictionary
def translate(DNA_d):
    pass


#PROBLEM 2
def time_it(f,n):
    start = perf_counter()
    f(n)
    return (perf_counter() - start)


#Traditional quick sort
def qs(lst):
    pass

#INPUT lst numbers, percent to calculate pivot mean
#RETURN sorted list--also uses qs if data size < 50
def qso(lst,percent):
    pass

    
# ! Important !

# To test the code of Problem-1, You may not run it directly in VSC (due to File not found error), 
# please follow the instructions below.

# 1. Open a new Terminal in VSC. 

# Run the below command in the terminal i.e. after typing in the command, hit enter
# 2. cd Assignment8

# Now run the a8.py in the newly opened terminal i.e. type the below command and hit enter
# 3. python3 a8.py

# It should print output on the terminal based on how much of the problem have you completed. Using this way
# of running, you can easily monitor your progress on this problem.


if __name__ == "__main__":
    '''for your use'''
    
    # #PROBLEM 1
    # #do not change file names
    # fn1,fn2 = "amino_acids.txt","DNA.txt"
    # aa_d = get_amino_acids(path, fn1)
    # DNA_d = get_DNA(path,fn2 )
    # protein = translate(DNA_d)

    # print("Dictionary")
    # print(aa_d)
    # print("FASTA file")
    # print(DNA_d)
    # print("Translations match:", str(protein == actual))

    # #should return "PLHS"    
    # print(translate(["nothing", "CCACTGCACTCA"]))

    # #should returns "D-"
    # print(translate(["nothing", "GACTAA"]))

    # #PROBLEM 2
    # lst = [rn.randint(0,100000) for _ in range(1000000)]
    # print("Data size 1000000")
    # print(f" qs      {time_it(qs,lst):.2} sec")
    # for percent in [1,5,10,20]:
    #     print(f" qso {percent:<2}% {time_it(qs,lst):.2} sec")