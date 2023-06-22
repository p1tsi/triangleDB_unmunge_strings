import sys

from binascii import unhexlify

if len(sys.argv) <= 1:
    print("Usage: python3 triangleDB_deobfuscate.py <obfuscated_string> [ <obfuscated_string>]")
    exit(0)

for obfuscated_string in sys.argv[1:]:
    try:
        obfuscated_bytes = unhexlify(obfuscated_string)
    except:
        print(f"{obfuscated_string} ->  * NOT AN HEX STRING *")
        continue

    final_string = ""
    key = 0

    for i in range(len(obfuscated_bytes)):

        if i == 0:
            final_string += chr(obfuscated_bytes[i])
        else:
            final_string += chr(obfuscated_bytes[i] ^ key)

        key = obfuscated_bytes[i]

    print(f"{obfuscated_string} -> {final_string}")
