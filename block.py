from datetime import datetime
from hashlib import sha256

class Block:
  def __init__(self, transactions, previous_hash, nonce = 0):
    self.timestamp = datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = nonce
    self.hash = self.generate_hash()
    
  def print_block(self):
    # prints block contents
    print("timestamp:", self.timestamp)
    print("transactions:", self.transactions)
    print("current hash:", self.generate_hash())
    
  def generate_hash(self):
    # hash the blocks contents
    data = [self.timestamp, self.transactions, self.nonce, self.previous_hash]
    
    block_contents=''
    for d in data:
      block_contents +=str(d)
    
    block_hash = sha256(block_contents.encode())
    
    return block_hash.hexdigest()