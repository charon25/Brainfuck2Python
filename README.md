# Brainfuck 2 Python

This Python scripts convert a brainfuck code into an equivalent Python code. To use it, just run it with the BF code as an argument :

```
python3 bf2py.py source_code.bf
```

Additional arguments can be used :
 - `-l` (or `--arraylength`) : set the length of the array used by the program. Default value is 30000.
 - `-s` (or `--cellsize`) : set the size (in bits) of each cell of the array. Can be any integer, does not need to be a power of 2. Default value is 8.
 - `-i` (or `--indentation`) : set the size (in spaces) of indentation to use for the Python code. Default value is 4.
 - `-o` (or `--outputpath`) : set the path of the file containing the Python code. Default value is BF file path with a `.py` extension.

The Python code can then be run as any Python program.

# 'Hello world' example

Input brainfuck code :
```brainfuck
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
```
Output Python code (with default parameters) :
```python
CELL_MAX_VALUE = 2**8
ARRAY_LENGTH = 30000

array = [0] * ARRAY_LENGTH
pointer = 0
output = []

array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
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
    
    while array[pointer] > 0:
        pointer = (pointer + 1) % ARRAY_LENGTH
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        pointer = (pointer + 1) % ARRAY_LENGTH
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        pointer = (pointer + 1) % ARRAY_LENGTH
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        pointer = (pointer + 1) % ARRAY_LENGTH
        array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
        pointer = (pointer - 1) % ARRAY_LENGTH
        pointer = (pointer - 1) % ARRAY_LENGTH
        pointer = (pointer - 1) % ARRAY_LENGTH
        pointer = (pointer - 1) % ARRAY_LENGTH
        array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
        
    pointer = (pointer + 1) % ARRAY_LENGTH
    array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
    pointer = (pointer + 1) % ARRAY_LENGTH
    array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
    pointer = (pointer + 1) % ARRAY_LENGTH
    array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
    pointer = (pointer + 1) % ARRAY_LENGTH
    pointer = (pointer + 1) % ARRAY_LENGTH
    array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
    
    while array[pointer] > 0:
        pointer = (pointer - 1) % ARRAY_LENGTH
        
    pointer = (pointer - 1) % ARRAY_LENGTH
    array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
    
pointer = (pointer + 1) % ARRAY_LENGTH
pointer = (pointer + 1) % ARRAY_LENGTH
output.append(chr(array[pointer]))
pointer = (pointer + 1) % ARRAY_LENGTH
array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
output.append(chr(array[pointer]))
array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
output.append(chr(array[pointer]))
output.append(chr(array[pointer]))
array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
output.append(chr(array[pointer]))
pointer = (pointer + 1) % ARRAY_LENGTH
pointer = (pointer + 1) % ARRAY_LENGTH
output.append(chr(array[pointer]))
pointer = (pointer - 1) % ARRAY_LENGTH
array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
output.append(chr(array[pointer]))
pointer = (pointer - 1) % ARRAY_LENGTH
output.append(chr(array[pointer]))
array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
output.append(chr(array[pointer]))
array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
output.append(chr(array[pointer]))
array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] - 1) % CELL_MAX_VALUE
output.append(chr(array[pointer]))
pointer = (pointer + 1) % ARRAY_LENGTH
pointer = (pointer + 1) % ARRAY_LENGTH
array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
output.append(chr(array[pointer]))
pointer = (pointer + 1) % ARRAY_LENGTH
array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
array[pointer] = (array[pointer] + 1) % CELL_MAX_VALUE
output.append(chr(array[pointer]))

print(''.join(output))
```

# Note
This was mostly done for recreational purposes, and is probably not the most efficient way to do it. Nonetheless is seems to work well for every BF program I tried.