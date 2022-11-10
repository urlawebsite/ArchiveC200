# The dictionary for the transation (this dictionary will store the DAN-amino acids mapping)
aa_d = {}

# the FASTA file (this list will store the FASTA file)
DNA_d = []

# the correct translation (is given for cross-checking)
actual = "PLHSPHPANFCVFSRD-IPYSEHLRRGALDPGRFRGPRSELSEIERARSRDLRRGPGPPGGEAAARRPLEAAGPLAGPRRRSGVAGRGGFQRGDGAVRGGPGAGARPVEEAGQQRRRLHDRGPGKVRQAGRPRPQGPSLPKPPGRASPTFLSQDLPGFPRHEDLLLPPGPEPRLLTSQSPRPEGGGRAEPRRGAPGRPTPRAVRAEPPARVPAASGPGQLPGERLPCWAPVPGRAPAGWVRGACGAGAGE-ALSARRSSWATACW-PSPGTTPETSAPRCRRRWTSS-ATLSRRWFPSTAELWVGGRGIPRRPSPCLSKASPRSSLLAVLSRGQDARGRR"

# INPUT name of amino acid file (make sure that you keep the amino_acids.txt under Assignment8 folder)
# RETURN a dictionary
# Key is a tuple (c0, c1, ... , cn) where ci are codons
# Value is a pair [name, abbreviation] for the amino acid
# make sure to close the file after reading it


def get_amino_acids(name):
    with open(name, "r") as aminoFile:
        contents = aminoFile.read()
        lines = contents.splitlines()
        for i in lines:
            a = i.split(",")
            x = tuple(a[2:])
            aa_d[x] = a[0], a[1]
        return aa_d


# INPUT file name of the DNA file (make sure that you keep the DNA.txt under Assignment8 folder)
# RETURN a list [header, DNA]
# header is first line in the file
# DNA is a string of letters from remainder of file
# no whitespace
# make sure to close the file


def get_DNA(name):
    with open(name, "r") as dnaFile:
        contents = dnaFile.read()
        lines = contents.splitlines()
        a = ""
        for i in lines:
            if i == ">HSGLTH1 Human theta 1-globin gene":
                DNA_d.append(i)
            else:
                a += i
        DNA_d.append(a)
        return (DNA_d)
    # with open(name, "r") as dnaFile:
    #     contents = dnaFile.read()
    #     lines = contents.splitlines()
    #     a = ""
    #     for i in lines:
    #         if i == ">HSGLTH1 Human theta 1-globin gene":
    #             DNA_d.append(i)
    #         else:
    #             a += i
    #     DNA_d.append(a)
    #     return (DNA_d)
    # INPUT FAST file
    # RETURN a string representing the protein (convert the DNA to amino acids)
    # using the dictionary


def translate(DNA_d):
    lst = DNA_d
    group = []
    nlst = []
    nlst2 = []
    b = ""

    for i in range(1, len(lst)):
        for j in range(0, len(lst[i]), 3):
            group.append(lst[i][j:j+3])
    for cod in group:
        for k, v in aa_d.items():
            for values in k:
                if cod in ["AA", "CC", "GG", "TT", "CA", "CG", "CT", "GA", "GC", "GT", "TA", "TC", "TG", "AC", "AG", "AT", "A", "G", "C", "T"]:
                    nlst2.append(cod)
                else:
                    if cod in values:
                        nlst.append(v[1])

    for letter in nlst:
        b += letter
    return b

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
    # fn1, fn2 = "amino_acids.txt", "DNA.txt"
    # aa_d = get_amino_acids(fn1)
    # # DNA_d = get_DNA(fn2)
    # # # protein = translate(DNA_d)

    # # # print("Dictionary")
    # print(aa_d)
    # # print("FASTA file")
    # # print(DNA_d)
    # # # print(protein)
    # # print("Translations match:", str(protein == actual))

    # # # #should return "PLHS"
    # # print(translate(["nothing", "CCACTGCACTCA"]))

    # # # #should returns "D-"
    # print(translate(["nothing", "GACTAA"]))
    # print(translate(["nothing", "GGAAGGCGC"]))
    # print(translate(["noting", "CCACTGCA"]))
    # print(translate(["noting", "GCGGGGTC"]))
    # print(translate(["noting", "GGTGCGGGGGG"]))
