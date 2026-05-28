import base64

def hex_to_base64(hex: str):
    raw_bytes = bytes.fromhex(hex)
    base64_bytes = base64.b64encode(raw_bytes)
    return base64_bytes.decode()

print(hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))