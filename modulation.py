def bpskmod(bit_sequence: list):
    symbol_sequence = []
    symbol0 = -1
    symbol1 = 1
    for i in bit_sequence:
        if i == 1:
            symbol_sequence.append(symbol1)
        else:
            symbol_sequence.append(symbol0)
    return symbol_sequence
