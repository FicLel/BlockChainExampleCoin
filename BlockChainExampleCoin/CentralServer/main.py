from flask import Flask, jsonify, request

app = Flask(__name__)

node_id = str(uuid4()).replace('-', '')

# Endpoint for nodes in the network to mine.
@app.route('/mine', methods=['GET'])
def mine():
    return 'Mine'

# Endpoint for clients to make transactions.
@app.route('/transactions', methods=['POST'])
def create_transaction():
    values = request.get_json()

    # Fields that are required in the requests body to create a new transaction.
    required = ['sender', 'recipient', 'quantity']

    # Check that request body has all the required fields.
    if not all (value in values for x in required):
        return 'Missing required values.', 400

    # Create new transaction.
    index = "use blockchain class to create new transaction."

    response = {'message': f'Transaction scheduled to be in block {index}'}

    return jsonify(response), 201

# Endpoint that returns the entire blockchain.
@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': 'add chain here.',
        'length': 'get chaing length here.'
    }

    return jsonify(response), 200

@app.route('/register', methods=['POST'])
def register_node():
    values = request.get_json()

    nodes_to_register = values.get('nodes')

    if nodes is None:
        return "No nodes register.", 400

    for node in nodes:
        # Register nodes.
        return 0

    response = {
        'nodes': 'list nodes here.'
    }

    return jsonify(response), 201

@app.route('/consensus', methods=['GET'])
def consensus():
    replaced = 'put blockchain.consensus here'

    if replaced:
        response = {
            'chain': 'place new chain here.'
        }
    else:
        response = {
            'chaing': 'place old chain here.'
        }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='localhost', port=5000)

