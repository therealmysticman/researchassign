import random #import random to provide random function in order to gives random input data
def CRC_gen(dataword, CRC_type):
    # CRC divisor lookup table
    crc_divisors = {
        'CRC-8': '100000111',
        'CRC-16': '11000000000000101',
        'CRC-32': '100000100110000010001110110110111'
    }
    # initialize the CRC register
    crc_register = '0' * (len(crc_divisors[CRC_type]) - 1)
    # perform modulo-2 division on dataword and CRC divisor
    for i in range(len(dataword)):
        crc_register = crc_register[1:] + dataword[i]
        if crc_register[0] == '1':
            crc_register = ''.join(['1' if crc_register[j] != crc_divisors[CRC_type][j] else '0' for j in range(len(crc_register))])
        else:
            crc_register = ''.join(['0' for j in range(len(crc_register))])
    # append the CRC bits to the dataword to form the codeword
    codeword = dataword + crc_register
    return codeword


def CRC_check(codeword, CRC_type):
    # CRC divisor lookup table
    crc_divisors = {
        'CRC-8': '100000111',
        'CRC-16': '11000000000000101',
        'CRC-32': '100000100110000010001110110110111'
    }
    # initialize the CRC register
    crc_register = '0' * (len(crc_divisors[CRC_type]) - 1)
    # perform modulo-2 division on codeword and CRC divisor
    for i in range(len(codeword)):
        crc_register = crc_register[1:] + codeword[i]
        if crc_register[0] == '1':
            crc_register = ''.join(['1' if crc_register[j] != crc_divisors[CRC_type][j] else '0' for j in range(len(crc_register))])
        else:
            crc_register = ''.join(['0' for j in range(len(crc_register))])
    # if the CRC register is all zeros, the codeword is valid
    if crc_register == '0' * (len(crc_divisors[CRC_type]) - 1):
        return 0  # PASS
    else:
        return -1  # FAIL

def test_crc():
    # CRC divisor lookup table
    crc_divisors = {
        'CRC-8': '100000111',
        'CRC-16': '11000000000000101',
        'CRC-32': '100000100110000010001110110110111'
    }
    # generate a random dataword
    dataword = ''.join([str(random.randint(0, 1)) for i in range(8)])
        
    # generate a random CRC type
    crc_type = random.choice(['CRC-8', 'CRC-16', 'CRC-32'])
        
    # generate the CRC codeword for the dataword
    codeword = CRC_gen(dataword, crc_type)
        
    # check the validity of the codeword
    validity = CRC_check(codeword, crc_type)
        
    # print the test results
    print("Input dataword:", dataword)
    print("CRC:", crc_type)
    print("codeword", codeword)
    if validity == 0:
        print("Codeword is valid")
    else:
        print("Codeword is invalid")
    print()
for i in range(10):
    print(f"Trial {i+1}:") # Trial time    
    test_crc()