def fixed_xor(buffer1: str, buffer2: str):
    final_hex = []

    for i in range(0, len(buffer1), 2):
        bin1 = decimal_to_binary(hex_to_decimal(buffer1[i:i+2])).zfill(8)
        bin2 = decimal_to_binary(hex_to_decimal(buffer2[i:i+2])).zfill(8)

        xor = []

        for bit1, bit2 in zip(bin1, bin2):
            xor.append(str(int(bit1) ^ int(bit2)))
        
        xor_bin = "".join(xor)

        final_hex.append(decimal_to_hex(binary_to_decimal(xor_bin)).zfill(2))

    return "".join(final_hex)
        

def hex_to_decimal(value: str):
    hex_base = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    decimal = 0
    for i in range(len(value)):
        decimal = decimal*16 + hex_base.index(value[i])
    
    return str(decimal)

def decimal_to_binary(value: str):
    value_int = int(value)
    if value_int == 0:
        return "0"
    binary_digits = []

    while value_int > 0:
        remainder = value_int % 2
        binary_digits.append(str(remainder))
        value_int //= 2

    binary_digits.reverse()
    return "".join(binary_digits)

def binary_to_decimal(value: str):
    decimal = 0

    reversed_bits = value[::-1]

    for i, bit in enumerate(reversed_bits):
        if bit == "1":
            decimal +=  2 ** i
    return str(decimal)

def decimal_to_hex(value: str):
    value_int = int(value)
    hex_base = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

    hex_digits = []
    while value_int > 0:
        remainder = value_int % 16
        hex_digits.append(hex_base[remainder])
        value_int //= 16

    hex_digits.reverse()
    return "".join(hex_digits)

print(fixed_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"))