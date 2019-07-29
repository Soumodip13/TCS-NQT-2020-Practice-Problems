number = int(input())
binary = bin(number)
# Prints the binary equivalent of a decimal replacing 0b from the front
print binary.replace("0b", "")