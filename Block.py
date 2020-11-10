import hashlib

class Block(object):
    """docstring for Block."""

    def __init__(self, previous_hash, transaction):
        self.previous_hash = previous_hash
        self.transaction = transaction
        string_to_hash = ''.join(transaction) + previous_hash
        self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()
