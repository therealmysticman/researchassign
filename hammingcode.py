import random #import random to provide random function in order to gives random input data

#This function generates a Hamming code from a dataword
def hamming_gen(dataword):
    # Calculate number of redundant bits needed
    r = 1
    while 2**r < len(dataword) + r + 1:
        r += 1
    
    # Create codeword with placeholders for redundant bits
    codeword = [0] * (len(dataword) + r)
    
    # Fill in data bits
    j = 0
    for i in range(len(codeword)):
        if i+1 != 2**j:
            if j < len(dataword):
                codeword[i] = int(dataword[j])
                j += 1
            else:
                break
    
    # Calculate and fill in redundant bits
    for i in range(r):
        p = 2**i
        sum = 0
        j = p - 1
        while j < len(codeword):
            if codeword[j] is not None:
                sum += codeword[j]
            j += 2*p
        
        if sum % 2 == 1:
            codeword[p-1] = 1
        else:
            codeword[p-1] = 0
    
    # Convert codeword to string representation
    codeword_str = ''.join(str(bit) for bit in codeword)
    
    return codeword_str

# function checks for errors in a received Hamming code
def hamming_check(codeword):
    # Calculate number of redundant bits used
    r = 1
    while 2**r < len(codeword) + 1:
        r += 1
    
    error = 0
    # Check each redundant bit
    for i in range(r):
        p = 2**i
        sum = 0
        j = p - 1
        while j < len(codeword):
            sum += int(codeword[j])
            j += 2*p
        
        if sum % 2 != int(codeword[p-1]):
            error += p
    
    return error

# Testing the functions
def test_hamming():
    # Generate random input of length 4-10
    dataword = [random.randint(0, 1) for _ in range(random.randint(2, 8))]
    # Encode dataword using Hamming code
    codeword = hamming_gen(dataword)
    # Introduce one bit error in codeword
    error_pos = random.randint(0, len(codeword)-1)
    codeword = codeword[:error_pos] + str(1 - int(codeword[error_pos])) + codeword[error_pos+1:]
    # Check for errors in codeword
    error = hamming_check(codeword)
    # Print results
    print("Input dataword:", dataword)
    print("Encoded codeword:", codeword)
    if error == 0:
        print("No errors detected.")
    else:
        print("Error detected at position", error)
    print()
for i in range(10): #sample 10 times to produce 10 trials of output
    print(f"Trial {i+1}:") # Trial time
    test_hamming() #use test_Checksum() function