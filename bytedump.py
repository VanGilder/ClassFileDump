f = open("hello.txt", "rb")

chunksize = 1

while True:
    byte = f.read(chunksize)
    if not byte:
        break
    decimal = ord(byte)
    binary = bin(decimal)[2:]
    hexadecimal = hex(decimal)[2:]
    symbol = "No display"
    if decimal >= 32 and decimal <= 126:
        symbol = chr(decimal)

    pdec = str(decimal).rjust(3, " ")
    phex = hexadecimal.rjust(2, "0")
    pbin = binary.rjust(8, "0")

    print(pdec, phex, pbin, symbol)
