CELL_MAX_VALUE = 2**8
ARRAY_LENGTH = 30000

array = [0] * ARRAY_LENGTH
pointer = 0
output = []

pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
value = input(f'Current output : {"".join(output)} | Input character : ')
array[pointer] = 0 if value == '' else (int(value[1:]) if value.startswith('\\') else ord(value[0]))

while array[pointer] > 0:
    pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
    pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
    value = input(f'Current output : {"".join(output)} | Input character : ')
    array[pointer] = 0 if value == '' else (int(value[1:]) if value.startswith('\\') else ord(value[0]))
    
pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1

while array[pointer] > 0:
    
    while array[pointer] > 0:
        pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
        pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
        
    pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
    pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
    pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
    pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
    
    while array[pointer] > 0:
        pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
        pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
        
        while array[pointer] > 0:
            pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
            array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
            pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
            pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
            array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
            pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
            array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
            
        pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
        pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
        
        while array[pointer] > 0:
            pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
            array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
            pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
            pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
            pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
            pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
            
            while array[pointer] > 0:
                array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
                pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
                
            pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
            
            while array[pointer] > 0:
                pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
                
            pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
            pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
            array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
            
        pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
        pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
        pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
        
        while array[pointer] > 0:
            
            while array[pointer] > 0:
                array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
                
            pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
            pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
            
            while array[pointer] > 0:
                pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
                array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
                pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
                array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
                
            pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
            pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
            
            while array[pointer] > 0:
                pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
                pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
                pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
                array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
                pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
                pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
                pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
                array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
                
            
        pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
        pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
        
        while array[pointer] > 0:
            
            while array[pointer] > 0:
                pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
                array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
                pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
                array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
                
            pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
            pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
            
        pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
        
    pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
    pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
    
    while array[pointer] > 0:
        pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
        pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
        array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
        pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
        pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
        array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
        
    pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
    pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
    
pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1

while array[pointer] > 0:
    output.append(chr(array[pointer]))
    pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
    pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
    

print(''.join(output))
