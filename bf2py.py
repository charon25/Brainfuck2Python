import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument('filepath', help='Path to the brainfuck file.')
parser.add_argument('-l', '--arraylength', help='Length of the memory array. Defaults to 30000.', default='30000')
parser.add_argument('-s', '--cellsize', help='Size of a memory cells in bits. Defaults to 8.', default='8')
parser.add_argument('-i', '--indentation', help='Number of spaces in each indentation. Defaults to 4.', default='4')
parser.add_argument('-o', '--outputpath', help='Path of the output Python file. Defaults to the same as the brainfuck file with a ".py" extension.', default='_')
args = parser.parse_args()

try:
    filepath = args.filepath
    array_length = int(args.arraylength)
    array_length = max(1, array_length)
    cell_size = int(args.cellsize)
    cell_size = max(1, cell_size)
    indentation = int(args.indentation)
    indentation = max(1, min(10, indentation))
    output_path = args.outputpath
    if output_path == '_':
        output_path = filepath + '.py'
except Exception:
    print('Wrong arguments.')
    sys.exit()

try:
    with open(filepath, 'r', encoding='utf-8') as fi:
        bf_code = fi.read()
except Exception:
    print(f"Cannot open file '{filepath}'.")
    sys.exit()

VALID_CHARS = '+-<>[].,'

CODE_LINES = {
    '+': '%TABarray[pointer] = 0 if array[pointer] == CELL_MAX_VALUE - 1 else array[pointer] + 1',
    '-': '%TABarray[pointer] = CELL_MAX_VALUE - 1 if array[pointer] == 0 else array[pointer] - 1',
    '>': '%TABpointer = 0 if pointer == ARRAY_LENGTH - 1 else pointer + 1',
    '<': '%TABpointer = ARRAY_LENGTH - 1 if pointer == 0 else pointer - 1',
    '.': '%TABoutput.append(chr(array[pointer]))',
    ',': "%TABvalue = input(f'Current output : {\"\".join(output)} | Input character : ')\n%TABarray[pointer] = 0 if value == '' else (int(value[1:]) if value.startswith('\\\\') and value[1:].isnumeric() else ord(value[0]))",
    '[': '%TAB\n%TABwhile array[pointer] > 0:',
    ']': '%TAB'

}

python_code = [
    f'CELL_MAX_VALUE = 2**{cell_size}',
    f'ARRAY_LENGTH = {array_length}',
    '',
    'array = [0] * ARRAY_LENGTH',
    'pointer = 0',
    'output = []',
    ''
]

tab_level = 0
TAB = ' ' * indentation

for char in bf_code:
    if not char in VALID_CHARS:
        continue

    line = CODE_LINES[char].replace('%TAB', TAB * tab_level)
    python_code.append(line)

    if char == '[':
        tab_level += 1
    elif char == ']':
        tab_level -= 1

python_code.extend([
    '',
    "print(''.join(output))",
    ''
])

try:
    with open(output_path, 'w', encoding='utf-8') as fo:
        fo.write('\n'.join(python_code))
except Exception:
    print(f"Cannot write into file '{output_path}'.")
