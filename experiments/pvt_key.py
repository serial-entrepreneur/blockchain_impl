import secrets

# Generate a private key
private_key = secrets.token_hex(32) # 32 bytes = 256 bits
print("Private Key:", private_key)