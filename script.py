from blockchain import Blockchain

block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}
fake_transactions = {"sender": "Bob", "receiver":"Cole, Alice", "amount":"25"}

# Verify Genesis Block
local_blockchain = Blockchain()
local_blockchain.print_blocks()

add_blocks = [block_one_transactions, 
              block_two_transactions, 
              block_three_transactions]

for b in add_blocks:
  local_blockchain.add_block(b)
  local_blockchain.print_blocks()

# Modify the 2nd block in local_blockchain by changing the block’s transactions to fake_transactions
# Check to see if the blockchain is still valid
local_blockchain.chain[1].transactions = fake_transactions
local_blockchain.validate_chain()
