import random #import random to provide random function in order to gives random input data
def parity_gen(dataword, parity_type,array_size):

    codeword = [] #make codeword array to store encoded codeword and analyze the parity_type
    if parity_type == 'one-dimensional-even':
        for word in dataword:           
            count = 0
            for bit in word:
            	if(bit == '1'):
                	count+=1

            if count % 2 == 0: # if divide with 2 and don't have remainder
            	codeword.append(word + '0') #append 0
            else:            	
            	codeword.append(word + '1') #append 1
                
    elif parity_type == 'one-dimensional-odd':
        for word in dataword:
            count = 0
            for bit in word:
            	if(bit == '1'):
                	count+=1

            if count % 2 == 0: # if divide with 2 and don't have remainder
            	codeword.append(word + '1') #append 0
            else:            	
            	codeword.append(word + '0') #append 1
                
    elif parity_type == 'two-dimensional-even': 
        col_no = array_size #column num related to array size
        row_no = len(dataword) #row num related to data_length
        for i in range(len(dataword)):
            if len(dataword[i]) < col_no:
                dataword[i] = dataword[i] + "0" * (col_no - len(dataword[i]))
        
        for words in dataword:  
            word = ""
            j=0
            count = 0
            while j < col_no:
                word+= words[j]
                if(words[j] == '1'):
                    count+=1
                j+=1
            if count % 2 == 0: # if divide with 2 and don't have remainder
                codeword.append(word + '0') #append 0
            else:
                codeword.append(word + '1') #append 1
                
        col_data = ""
        j=0
        count_lst_row = 0
        while j < col_no:
            count = 0
            word = ""
            for words in dataword:
                word+=words[j]
                if(words[j] == '1'):
                    count+=1
            if count % 2 == 0:
                col_data += '0'
            else:
                col_data += '1'
                count_lst_row += 1
            j+=1
        
        if count_lst_row % 2 == 0: # if last row is even
            codeword.append(col_data + '0') #append 0
        else:
            codeword.append(col_data + '1') #append 1
    elif parity_type == 'two-dimensional-odd':
        col_no = array_size #column num related to array size
        row_no = len(dataword) #row num related to data_length
        for i in range(len(dataword)):
            if len(dataword[i]) < col_no:
                dataword[i] = dataword[i] + "0" * (col_no - len(dataword[i]))
        
        for words in dataword:  
            word = ""
            j=0
            count = 0
            while j < col_no:
                word+= words[j]
                if(words[j] == '1'):
                    count+=1
                j+=1
            if count % 2 == 0: # if divide with 2 and don't have remainder
                codeword.append(word + '1') #append 1
            else:
                codeword.append(word + '0') #append 0
                
        col_data = ""
        j=0
        count_lst_row = 0
        while j < col_no:
            count = 0
            word = ""
            for words in dataword:
                word+=words[j]
                if(words[j] == '1'):
                    count+=1
            if count % 2 == 0:
                col_data += '1'
                count_lst_row += 1
            else:
                col_data += '0'
            j+=1
        
        if count_lst_row % 2 == 0: # if last row is even
            codeword.append(col_data + '1') #append 1
        else:
            codeword.append(col_data + '0') #append 0

    return codeword

def parity_check(codeword, parity_type, array_size):
    valid = 0
    
    if parity_type == 'one-dimensional-even':
        for word in codeword:           
            count = 0
            for bit in word:
            	if(bit == '1'):
                	count+=1
            if count % 2 == 1: # if not divisor of 2 and have remainder
                valid = -1
                break                
    elif parity_type == 'one-dimensional-odd':
        
        for word in codeword:
            count = 0
            for bit in word:
                if(bit == '1'):
                    count+=1
            if count % 2 == 0: # if divide with 2 and don't have remainder
                valid = -1
                break
    elif parity_type == 'two-dimensional-odd':
        col_no = array_size #column num related to array size
        row_no = len(codeword) #row num related to data_length
        
        for words in codeword:  
            word = ""
            j=0
            count = 0
            while j < col_no:
                word+= words[j]
                if(words[j] == '1'):
                    count+=1
                j+=1
            if count % 2 == 0: # if divide with 2 and don't have remainder
                valid = -1 #fail
                return valid
                
        col_data = ""
        j=0
        count_lst_row = 0
        while j < col_no:
            count = 0
            word = ""
            for words in codeword:
                word+=words[j]
                if(words[j] == '1'):
                    count+=1
            if count % 2 == 0:# if divide with 2 and don't have remainder
                valid = -1 #fail
                return valid
            j+=1
    elif parity_type == 'two-dimensional-even':
        col_no = array_size #column num related to array size
        row_no = len(codeword) #row num related to data_length
        
        for words in codeword:  
            word = ""
            j=0
            count = 0
            while j < col_no:
                word+= words[j]
                if(words[j] == '1'):
                    count+=1
                j+=1
            if count % 2 == 1: # if not divisor of 2 and have remainder
                valid = -1 #fail
                return valid
                
        col_data = ""
        j=0
        count_lst_row = 0
        while j < col_no:
            count = 0
            word = ""
            for words in codeword:
                word+=words[j]
                if(words[j] == '1'):
                    count+=1
            if count % 2 == 1: # if not divisor of 2 and have remainder
                valid = -1 #fail
                return valid
            j+=1
    else:
        print("Invalid parity type")
        valid = -1 #fail
    
    return valid #default:pass

def test_parity():
        # generate random input parameters
        array_size = random.randint(2, 8)
        dataword = [''.join(random.choice(['0', '1']) for _ in range(random.randint(2, 8))) for _ in range(array_size)]
        parity_type = random.choice(['one-dimensional-even', 'one-dimensional-odd', 'two-dimensional-even', 'two-dimensional-odd'])
        
        
        # generate codeword and check if it's valid
        codeword = parity_gen(dataword, parity_type, array_size)
        valid = parity_check(codeword, parity_type, array_size)
        
        # display the results
        print(f'Input parameters: dataword={dataword}')
        print(f'Array size={array_size}')
        print(f'Parity type={parity_type}') 
        print(f'Generated codeword: {codeword}')
        print(f'Codeword is {"valid" if valid == 0 else "invalid"}')
        print()
for i in range(10):
    print(f"Trial {i+1}:") # Trial time
    test_parity()