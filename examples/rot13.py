CELL_MAX_VALUE = 2**8
ARRAY_LENGTH = 30000

array = [0] * ARRAY_LENGTH
pointer = 0
output = []

array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
value = input(f'Current output : {"".join(output)} | Input character : ')
array[pointer] = 0 if value == '' else (int(value[1:]) if value.startswith('\\') else ord(value[0]))
array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE

while array[pointer] > 0:
    array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
    
    while array[pointer] > 0:
        pointer = (pointer + 1) % ARRAY_LENGTH
        pointer = (pointer + 1) % ARRAY_LENGTH
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        
        while array[pointer] > 0:
            pointer = (pointer + 1) % ARRAY_LENGTH
            array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
            array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
            array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
            array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
            array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
            array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
            array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
            array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
            pointer = (pointer - 1) % ARRAY_LENGTH
            array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
            
        pointer = (pointer - 1) % ARRAY_LENGTH
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        pointer = (pointer - 1) % ARRAY_LENGTH
        array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
        
        while array[pointer] > 0:
            pointer = (pointer + 1) % ARRAY_LENGTH
            array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
            pointer = (pointer + 1) % ARRAY_LENGTH
            array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
            pointer = (pointer + 1) % ARRAY_LENGTH
            array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
            
            while array[pointer] > 0:
                pointer = (pointer + 1) % ARRAY_LENGTH
                pointer = (pointer + 1) % ARRAY_LENGTH
                pointer = (pointer + 1) % ARRAY_LENGTH
                
            pointer = (pointer - 1) % ARRAY_LENGTH
            
            while array[pointer] > 0:
                
                while array[pointer] > 0:
                    pointer = (pointer + 1) % ARRAY_LENGTH
                    array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
                    pointer = (pointer - 1) % ARRAY_LENGTH
                    array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
                    
                pointer = (pointer + 1) % ARRAY_LENGTH
                pointer = (pointer + 1) % ARRAY_LENGTH
                array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
                pointer = (pointer + 1) % ARRAY_LENGTH
                
            pointer = (pointer - 1) % ARRAY_LENGTH
            pointer = (pointer - 1) % ARRAY_LENGTH
            pointer = (pointer - 1) % ARRAY_LENGTH
            pointer = (pointer - 1) % ARRAY_LENGTH
            pointer = (pointer - 1) % ARRAY_LENGTH
            array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
            
        
    pointer = (pointer + 1) % ARRAY_LENGTH
    pointer = (pointer + 1) % ARRAY_LENGTH
    pointer = (pointer + 1) % ARRAY_LENGTH
    
    while array[pointer] > 0:
        array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
        
    array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
    pointer = (pointer + 1) % ARRAY_LENGTH
    array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
    array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
    
    while array[pointer] > 0:
        array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
        
        while array[pointer] > 0:
            pointer = (pointer - 1) % ARRAY_LENGTH
            array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
            pointer = (pointer + 1) % ARRAY_LENGTH
            array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
            array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
            array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
            
            while array[pointer] > 0:
                array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
                
            
        
    pointer = (pointer - 1) % ARRAY_LENGTH
    
    while array[pointer] > 0:
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        pointer = (pointer - 1) % ARRAY_LENGTH
        
        while array[pointer] > 0:
            pointer = (pointer + 1) % ARRAY_LENGTH
            array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
            
            while array[pointer] > 0:
                pointer = (pointer + 1) % ARRAY_LENGTH
                array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
                pointer = (pointer + 1) % ARRAY_LENGTH
                pointer = (pointer + 1) % ARRAY_LENGTH
                
            pointer = (pointer + 1) % ARRAY_LENGTH
            
            while array[pointer] > 0:
                array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
                
                while array[pointer] > 0:
                    pointer = (pointer - 1) % ARRAY_LENGTH
                    array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
                    pointer = (pointer + 1) % ARRAY_LENGTH
                    array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
                    
                pointer = (pointer + 1) % ARRAY_LENGTH
                array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
                pointer = (pointer + 1) % ARRAY_LENGTH
                pointer = (pointer + 1) % ARRAY_LENGTH
                
            pointer = (pointer - 1) % ARRAY_LENGTH
            pointer = (pointer - 1) % ARRAY_LENGTH
            pointer = (pointer - 1) % ARRAY_LENGTH
            pointer = (pointer - 1) % ARRAY_LENGTH
            pointer = (pointer - 1) % ARRAY_LENGTH
            array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
            
        pointer = (pointer + 1) % ARRAY_LENGTH
        pointer = (pointer + 1) % ARRAY_LENGTH
        
        while array[pointer] > 0:
            pointer = (pointer - 1) % ARRAY_LENGTH
            array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
            pointer = (pointer + 1) % ARRAY_LENGTH
            array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
            
        pointer = (pointer + 1) % ARRAY_LENGTH
        
        while array[pointer] > 0:
            array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
            
            while array[pointer] > 0:
                array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
                pointer = (pointer - 1) % ARRAY_LENGTH
                pointer = (pointer - 1) % ARRAY_LENGTH
                
                while array[pointer] > 0:
                    array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
                    
                pointer = (pointer + 1) % ARRAY_LENGTH
                pointer = (pointer + 1) % ARRAY_LENGTH
                
            pointer = (pointer - 1) % ARRAY_LENGTH
            pointer = (pointer - 1) % ARRAY_LENGTH
            
            while array[pointer] > 0:
                pointer = (pointer - 1) % ARRAY_LENGTH
                pointer = (pointer - 1) % ARRAY_LENGTH
                array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
                pointer = (pointer + 1) % ARRAY_LENGTH
                pointer = (pointer + 1) % ARRAY_LENGTH
                array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
                
            pointer = (pointer + 1) % ARRAY_LENGTH
            pointer = (pointer + 1) % ARRAY_LENGTH
            
        pointer = (pointer - 1) % ARRAY_LENGTH
        pointer = (pointer - 1) % ARRAY_LENGTH
        
        while array[pointer] > 0:
            pointer = (pointer - 1) % ARRAY_LENGTH
            pointer = (pointer - 1) % ARRAY_LENGTH
            array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
            pointer = (pointer + 1) % ARRAY_LENGTH
            pointer = (pointer + 1) % ARRAY_LENGTH
            array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
            
        
    pointer = (pointer - 1) % ARRAY_LENGTH
    
    while array[pointer] > 0:
        array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
        
    pointer = (pointer - 1) % ARRAY_LENGTH
    output.append(chr(array[pointer]))
    
    while array[pointer] > 0:
        array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
        
    pointer = (pointer - 1) % ARRAY_LENGTH
    array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
    value = input(f'Current output : {"".join(output)} | Input character : ')
    array[pointer] = 0 if value == '' else (int(value[1:]) if value.startswith('\\') else ord(value[0]))
    array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
    

print(''.join(output))
