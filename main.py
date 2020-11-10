from Block import Block
from Blockchain import Blockchain
import time

blockchain = Blockchain()

def new_transaction(author, content):
    data = {}
    data['timestamp'] = time.time()
    data['author'] = author
    data['content'] = content
    blockchain.add_new_transaction(data)

def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return {"length": len(chain_data), "chain": chain_data}

def mine_unconfirmed_transactions():
    result = blockchain.mine()
    if not result:
        return "No transactions to mine"
    return "Block #{} is mined.".format(result)

def get_pending_tx():
    return blockchain.unconfirmed_transactions

new_transaction('Kilmek','wisisz mi dychę')
print('Added new block.\n')
print('Pending transactions:\n', get_pending_tx())
mine_unconfirmed_transactions()
print('\nMining complete.\n')
print('Pending transactions:\n', get_pending_tx())
print('\nChain:\n', get_chain())
