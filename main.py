
blockchain =[]
from Block import Block
genesis_block = Block('Chancellor on the brink...', ['Satoshi  sent 1 BTC to Kubunio',
'Kubunio sent 10 BTC to Niki'])
second_block = Block(genesis_block.block_hash, ['Klimek sent 20 BTC to Mrowa'])
print(second_block.transaction)
print(second_block.block_hash)
