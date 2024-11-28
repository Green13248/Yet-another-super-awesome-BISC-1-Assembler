Readdir = input("Read: ")
writedir = input("Write: ")
writefile = open(writedir, "w")
f = open(Readdir, "r")
Loops = []
linenum = 0
Followdata = 0
for line in f:
    currentreg = ""
    linenum += 1
    if ";" in line:
        global result
        result = line.split(' ;')[0]
    else:
        result = line
    tabresult = result.split("\t")[0]
    Onehalf = tabresult.rsplit(" ")
    Sechalf = tabresult.rsplit(",")
    if "," in result:
        if Sechalf[0] == "JMP":
            for x in Loops:
                y = x.rsplit("/")
                Noenter = Sechalf[1].split("\n")[0]
                z = " " + y[0]
                if Noenter == z:
                    writefile.write("01000101")
                    writefile.write(y[1])
            
        if "%" in result:
            Nopercent = Sechalf[1].rsplit("%")
            Followdata = bin(int(Nopercent[1]))[2:].zfill(8)
        if "!" in result:
            if Onehalf[1] == "!A\n":
                currentreg = "00"
            if Onehalf[1] == "!B\n":
                currentreg = "01"
            if Onehalf[1] == "!C\n":
                currentreg = "10"
            if Onehalf[1] == "!D\n":
                currentreg = "11"
            else:
                if Onehalf[1] != "!A\n":
                    if Onehalf[1] != "!B\n":
                        if Onehalf[1] != "!C\n":
                            if Onehalf[1] != "!D\n":
                                print("Error at line " + str(linenum))
                                break        
        if Sechalf[0] == "DTB":
            writefile.write("01011001")
            writefile.write(Followdata)
        if Onehalf[0] == "BTR,":
            writefile.write(currentreg + "001100")
        if Onehalf[0] == "RTB,":
            writefile.write(currentreg + "001011")
    if Onehalf[0] == "ADD":
        writefile.write("00000001")
    if Onehalf[0] == "SUB":
        writefile.write("00000010")
    if Onehalf[0] == "MUL":
        writefile.write("00000011")
    if Onehalf[0] == "DIV":
        writefile.write("00000100")
    if ":" in result:
        loopname = result.split(":")[0]
        Loops.append(loopname + "/" + bin(int(linenum))[2:].zfill(8))
    if Onehalf[0] == "CMP":
        writefile.write("00000110")
    if Onehalf[0] == "CMG":
        writefile.write("00000111")
    if Onehalf[0] == "CGE":
        writefile.write("00001000")
    if Onehalf[0] == "BTA":
        writefile.write("00001101")
    if Onehalf[0] == "BTM":
        writefile.write("00001111")
writefile.close()
