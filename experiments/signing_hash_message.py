import ecdsa
import hashlib

# Message to be signed
message = "This is a test message".encode('utf-8')
message_corrupted = "This is a corrupted message".encode('utf-8')

# Hash the message
hashed_message = hashlib.sha256(message).digest()
hashed_message_corrupted = hashlib.sha256(message_corrupted).digest()

# Sign the hashed message with the private key
private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) # uses SECP256k1 curve
signature = private_key.sign(hashed_message)

# Print the signature
print("Signature:", signature.hex())

# Verify the signature with the public key
public_key = private_key.get_verifying_key()
verified = public_key.verify(signature, hashed_message)
print("Signature verified:", verified)

# Verify the signature with the corrupted message
try:
    verified_corrupted = public_key.verify(signature, hashed_message_corrupted)
    print("Signature verified (corrupted message):", verified_corrupted)
except ecdsa.BadSignatureError:
    print("Signature verification failed (corrupted message)")