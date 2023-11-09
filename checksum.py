import random #import random to provide random function in order to gives random input data

#This function generates a checksum for a given set of datawords using the ones' complement sum method.
def Checksum_gen(dataword, num_blocks): 
    # Calculate the sum of all datawords
    sum = 0
    for i in range(num_blocks):
        sum += int(dataword[i], 2)
        
    # Compute the 1's complement of the sum and convert it to binary
    checksum = bin(~sum & 0xff)[2:].zfill(8)
    
    return checksum #returns an 8-bit binary checksum

#This function checks the validity of a given codeword using the ones' complement sum method.
def Checksum_check(codeword, num_blocks):
    # Calculate the sum of all datawords and the checksum
    sum = 0
    for i in range(num_blocks):
        sum += int(codeword[i], 2)
    sum += int(codeword[num_blocks], 2)
    
    # Verify that the sum is equal to 0xff (all 1's)
    if sum == 0xff:
        return 0 # is equal, PASS
    else:
        return -1 #is not equal, FAIL

#This function is a test both function
def test_Checksum():
    num_blocks = random.randint(2, 4) 
    data_length = random.randint(2, 8) 
    datawords = ["".join(random.choice(['0', '1']) for j in range(data_length)) for i in range(num_blocks)] 
    print("Input datawords:", datawords) 
    print("Number of blocks:", num_blocks) 
    checksum = Checksum_gen(datawords, num_blocks) #generate checksum output
    print("Generated checksum:", checksum) 
    codeword = datawords + [checksum] 
    expected_validity = 0
    actual_validity = Checksum_check(codeword, num_blocks) #check the true validity by Checksum_check()function.
    if actual_validity == expected_validity: #if true
        print("Codeword is valid")
    else:
        print("Codeword is invalid") #if false
    print("Expected validity:", expected_validity)
    print("Actual validity:", actual_validity)
    print()#use two above print to compare result and use print() to start new line

for i in range(10): #sample 10 times to produce 10 trials of output
    print(f"Trial {i+1}:") # Trial time
    test_Checksum() #use test_Checksum() function