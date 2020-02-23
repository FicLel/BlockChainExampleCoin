import hasblib
import json
from time import time

class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
    def newBlock(self, proof,previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transacctions,
            'proof': proof
        }
        self.current_transactions = []

        self.chain.append(block)
        return block
    def newTransaction(self,sender, recipient, amount):
        self.current_transactions.append({
            'sender' : sender,
            'recipient' : recipient,
            'amount' : amount
        })
        
        return self.last_block['index'] + 1
    @property
    def lastBlock(self):
        return self.chain[-1]
    def hash(block):
        primaryString = json.dumps(block,sort_keys=True).encode()
        hashString = hashlib.sha256(primaryString).hexdigest()
        return hashString
