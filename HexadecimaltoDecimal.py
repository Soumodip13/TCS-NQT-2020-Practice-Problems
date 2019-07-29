hex_number = str(raw_input())
hexadecimal = ''.join('0x' + hex_number)
# Prints Decimal equivalent of a hexadecimal number
print int(hexadecimal, 16)
