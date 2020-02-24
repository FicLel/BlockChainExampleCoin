from ..blockchain_coin.blockchain import Blockchain
from flask import Flask, jsonify, request
from uuid import uuid4

app = Flask(__name__)

node_id = str(uuid4()).replace('-', '')
blockchain = Blockchain()

# Endpoint for nodes in the network to mine.
@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    blockchain.new_transaction(sender = "0", recipient = node_id, quantity = 1)

    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }

    return jsonify(response), 200

# Endpoint for clients to make transactions.
@app.route('/transactions', methods=['POST'])
def create_transaction():
    values = request.get_json()

    # Fields that are required in the requests body to create a new transaction.
    required = ['sender', 'recipient', 'quantity']

    # Check that request body has all the required fields.
    if not all (value in values for x in required):
        return {'error': 'Missing required values.'}, 400

    # Create new transaction.
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['quantity'])

    response = {'message': f'Transaction scheduled to be in block {index}'}

    return jsonify(response), 201

# Endpoint that returns the entire blockchain.
@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }

    return jsonify(response), 200

@app.route('/register', methods=['POST'])
def register_node():
    values = request.get_json()

    nodes_to_register = values.get('nodes')

    if nodes_to_register is None:
        return {'error': 'No nodes registered.'}, 400

    
    # Register nodes.
    for node in nodes_to_register:
        blockchain.register_node(node)

    response = {
        'nodes': list(blockchain.nodes),
    }

    return jsonify(response), 201

@app.route('/nodes', methods=['GET'])
def get_nodes():
    response = {
        'nodes': list(blockchain.nodes),
    }

    return jsonify(response), 200

@app.route('/consensus', methods=['GET'])
def consensus():
    replaced = blockchain.resolve()

    if replaced:
        response = {
            'message': 'Blockchain replaced',
            'chain': blockchain.chain,
        }
    else:
        response = {
            'message': 'Blockchain conserved.',
            'chain': blockchain.chain,
        }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

