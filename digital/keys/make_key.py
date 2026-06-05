#should be run ONLY ONCE. DO NOT RUN THIS OR STUFF MIGHT BE MESSED UP
print("this code generates a new key. you should not need to ever run this.")
exit(1)
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature
import base64, time

# KEYGEN
key = Ed25519PrivateKey.generate()
open("private.pem","wb").write(key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()))
open("public.pem","wb").write(key.public_key().public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo))
