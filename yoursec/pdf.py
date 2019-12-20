import sys
from glob import glob


MALICIOUS = (
    b'GoToR',
    b'GoToE',
    b'AA',
    b'Launch',
    b'JS',
    b'JavaScript',
    b'SubmitForm',
)

import string
INSTRUCTION_CHARS = [i.encode('ascii') for i in (string.digits + string.ascii_letters)]

for i in sys.argv[1:]:
    with open(i, 'rb') as f:
        stream_block_open = False
        instruction_name = b''
        instruction_block = b''
        instruction_block_level = 0
        instruction_name_open = False
        comment_open = False
        last = b''
        buff = b''
        while True:
            c = f.read(1)
            if not c:
                break

            if not comment_open and c == b'%':
                comment_open = True
            elif comment_open and c in (b'\n', b'\r'):
                comment_open = False
                continue

            if comment_open:
                continue

            if buff.endswith(b'endstream'):
                stream_block_open = False
            elif buff.endswith(b'stream'):
                stream_block_open = True

            if not stream_block_open:
                if last == c == b'<':
                    instruction_block_level += 1
                elif last == c == b'>':
                    if instruction_block_level > 0:
                        instruction_block_level -= 1

                if instruction_block_level:
                    instruction_block += c
                    if c == b'/':
                        if instruction_name_open:
                            if instruction_name in MALICIOUS:
                                print('malicious instruction', i, instruction_name)
                                #print('block start', instruction_block[0:200])
                                #print('block end', instruction_block[-12:])
                            instruction_name = b''
                        else:
                            instruction_name_open = True
                    elif instruction_name_open:
                        if c in INSTRUCTION_CHARS:
                            instruction_name += c
                        else:
                            instruction_name_open = False
                            if instruction_name in MALICIOUS:
                                print('malicious instruction', i, instruction_name)
                                #print('block start', instruction_block[0:120])
                                #print('block end', instruction_block[-12:])
                            instruction_name = b''
                else:
                    instruction_block = b''

            last = c
            buff += c
