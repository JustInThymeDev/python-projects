#Begin dna_analyzer program
def dna_analyzer():
    #Print intro statements
    print("This program reports information about DNA")
    print("nucleotide sequences that may encode proteins.")
    #Grab i/o file names
    inFile = input("Input file name? ")
    outFile = input("Output file name? ")
    #File opening and data gnabbing
    f = open(inFile,'r')
    fw = open(outFile, 'w')
    lines = f.readlines()
    flag = 0
    write_file = ""
    for line in lines:
        if flag == 0:
            write_file += "Region Name: " + line
            flag = 1
        else:
            line = line.upper()
            write_file += "Nucleotides: " + line
            codons = []
            currentCodon = ""
            for i in range(0, len(line)):
                if line[i] != '-':
                    currentCodon += line[i]
                    if len(currentCodon) == 3:
                        codons.append(currentCodon)
                        currentCodon = ""
            line = list(line)
            #Mass multiplication section
            count = []
            count.append(line.count('A'))
            count.append(line.count('C'))
            count.append(line.count('G'))
            count.append(line.count('T'))
            junk = line.count('-')
            mass = []
            mass.append(count[0] * 135.128)
            mass.append(count[1] * 111.103)
            mass.append(count[2] * 151.128)
            mass.append(count[3] * 125.107)
            total_mass = sum(mass)
            total_mass += junk * 100.000
            for i in range(0,len(mass)):
                mass[i] = mass[i] / total_mass * 100
                mass[i] = round(mass[i], 1)
            total_mass = round(total_mass, 1)
            write_file += "Nuc. Counts: [" + str(count[0]) + ", " + str(count[1]) + ", " + str(count[2]) + ", " + str(count[3]) + "]\n"
            write_file += "Total Mass%: [" + str(mass[0]) + ", " + str(mass[1]) + ", " + str(mass[2]) + ", " + str(mass[3]) + "] of " + str(total_mass) + "\n"
            write_file += "Codons List: ["
            for i in range(0, len(codons)-1):
                write_file += codons[i] + ", "
            write_file += codons[-1] + "]\n"
            if (codons[0] == "ATG") and (codons[-1] == "TAA" or codons[-1] == "TAG" or codons[-1] == "TGA") and (len(codons) >= 5) and (mass[1] + mass[2] >= 30):
                write_file += "Is Protein?: YES\n\n"
            else:
                write_file += "Is Protein?: NO\n\n"
            flag = 0
    fw.write(write_file)
    f.close()
    fw.close()
def main():
    dna_analyzer()
main()
