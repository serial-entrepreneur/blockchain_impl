import ecdsa

# Use the private key to derive the public key
private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) # uses SECP256k1 curve
public_key = private_key.get_verifying_key()

# Print the keys
print("Private Key:", private_key.to_string().hex())
print("Public Key:", public_key.to_string().hex())