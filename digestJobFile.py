opcodeFile = open("hex.bin", "r")

for line in opcodeFile.readlines():
    inputs = int(line[2:],16)
    firstTwoBitMask = 0b11000000000000000000000000000000
    opcodeBitMask = 0b00111111000000000000000000000000;
    twoBits = (inputs & firstTwoBitMask) >> 30;
    opcode = (inputs & opcodeBitMask) >> 24;

    print(line.rstrip() + " " + str(twoBits) + " "  + str(opcode))





