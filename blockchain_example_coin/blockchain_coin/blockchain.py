import hashlib
import json
import requests
from time import time
from urllib.parse import urlparse

class Blockchain(object):
    def __init__(self):
        """Constructor"""
        self.chain = []
        self.current_transactions = []
        self.nodes = set()

        # Create the genesis block (first block in the blockchain).
        self.new_block(previous_hash = 1, proof = 100)

    def proof_of_work(self, last_proof):
        """Uses the proof of work custom algorithm to demonstrate work."""
        proof = 0

        # Find p' (See proof of work algorithm).
        while self.valid_proof(last_proof, proof) is False:
            proof = proof + 1

        return proof

    def register_node(self, address):
        """Registers new nodes to the current node."""
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def new_block(self, proof, previous_hash = None):
        """Adds a block to the blockchain."""
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []

        self.chain.append(block)

        return block

    def new_transaction(self, sender, recipient, quantity):
        """Creates a new transaction and schedules a block for it."""
        self.current_transactions.append({
            'sender' : sender,
            'recipient' : recipient,
            'amount' : quantity,
        })
        
        return self.last_block['index'] + 1

    def validate_chain(self, chain):
        """Checks that an entire blockchain is valid."""
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]

            if block['previous_hash'] != self.hash(last_block):
                return False

            if not self.valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block
            current_index = current_index + 1

        return True

    def resolve(self):
        """Runs the consensus algorithm, cross-validating with each registered peer (node) in the current node."""
        peers = self.nodes
        new_chain = None
        max_length = len(self.chain)

        for node in peers:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                if length > max_length and self.validate_chain(chain):
                    max_length = length
                    new_chain = chain

        if new_chain:
            self.chain = new_chain
            return True

        return False

    @property
    def last_block(self):
        """Returns the last block in the blockchain."""
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """Calculates a block's hash."""
        primaryString = json.dumps(block, sort_keys = True).encode()
        hashString = hashlib.sha256(primaryString).hexdigest()

        return hashString

    @staticmethod
    def valid_proof(last_proof, proof):
        """Verifies that a proof is valid."""
        proof_guess = f'{last_proof}{proof}'.encode()
        proof_guess_hash = hashlib.sha256(proof_guess).hexdigest()

        return proof_guess_hash[:4] == "0000"
