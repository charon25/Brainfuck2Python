# Brainfuck 2 Python

This Python scripts converts a Brainfuck code into an equivalent Python code. To use it, just run it with the BF code as an argument :

```
python3 bf2py.py source_code.bf
```

Additional arguments can be used :
 - `-l` (or `--arraylength`) : set the length of the array used by the program. Default value is 30000.
 - `-s` (or `--cellsize`) : set the size (in bytes) of each cell of the array. Can be any integer, does not need to be a power of 2. Default value is 8.
 - `-i` (or `--indentation`) : set the size (in spaces) of indentation to use for the Python code. Default value is 4.
 - `-o` (or `--outputpath`) : set the path of the file containing the Python code. Default value is BF file path with a `.py` extension.

The Python code can then be run as any Python program.

## Inputs

When a Python program made using this script asks for an input, it can be entered in three different ways :
 - An empty input will be considered as a 0 ;
 - An input containing a number preceded by a `\` will use this number as the input value ;
 - In any other case, the input will be the ASCII code of the first character of the input.


## 'Hello world' example

Input Brainfuck code :
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

array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1

while array[pointer] > 0:
    pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
    array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
    array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
    array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
    array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
    
    while array[pointer] > 0:
        pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
        array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
        array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
        pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
        array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
        array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
        array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
        pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
        array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
        array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
        array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
        pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
        array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
        pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
        pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
        pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
        pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
        array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
        
    pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
    array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
    pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
    array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
    pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
    array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
    pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
    pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
    array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
    
    while array[pointer] > 0:
        pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
        
    pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
    array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
    
pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
output.append(chr(array[pointer]))
pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
output.append(chr(array[pointer]))
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
output.append(chr(array[pointer]))
output.append(chr(array[pointer]))
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
output.append(chr(array[pointer]))
pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
output.append(chr(array[pointer]))
pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
output.append(chr(array[pointer]))
pointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1
output.append(chr(array[pointer]))
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
output.append(chr(array[pointer]))
array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
output.append(chr(array[pointer]))
array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
array[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1
output.append(chr(array[pointer]))
pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
output.append(chr(array[pointer]))
pointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
array[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1
output.append(chr(array[pointer]))

print(''.join(output))
```

# Note
This was mostly done for recreational purposes, and is probably not the most efficient way to do it. Nonetheless is seems to work well for every BF program I tried.