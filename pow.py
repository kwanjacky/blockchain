# proof of work
import numpy as np

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

# import sha256
from hashlib import sha256
# sets the amount of leading zeros that must be found in the hash produced by the nonce
difficulty = 2
nonce = 0

# creating the proof 
text = str(nonce)+str(new_transactions)
hash_result = sha256(text.encode())
proof = hash_result.hexdigest()

# printing proof
print(proof)
  
# finding a proof that has 2 leading zeros
final_proof=''
for nonce in range(1000):
  text = str(nonce)+str(new_transactions)
  hash_result = sha256(text.encode())
  proof = hash_result.hexdigest()
  if proof[:difficulty] == '0'*difficulty:
    final_proof = proof
    break

# printing final proof that was found
print(nonce)
print(final_proof)