import json
from flask import Flask, jsonify, request, Response
from service.service import get_block_info, get_transaction, get_all_balances

app = Flask(__name__)


@app.route('/block/<string:block_id>', methods=['GET'])
def get_block_number(block_id: str):
    """
    Get block information by ID
    """
    try:
        block_info = get_block_info(block_id)
        return jsonify(block_info), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/transaction/<string:tx_hash>', methods=['GET'])
def get_transaction_route(tx_hash: str):
    """
    Get transaction information by Hash
    """
    try:
        transaction_info = get_transaction(tx_hash)
        transaction_dict = {k: v for k, v in transaction_info.__dict__.items() 
                          if not k.startswith('_')}
        return jsonify(transaction_dict), 200 
    except Exception as e:
        return jsonify({
            "error": str(e),
            "transaction_hash": tx_hash
        }), 500


@app.route('/balance/<string:public_key>', methods=['GET'])
def get_balance(public_key: str):
    """
    Get wallet balance by public key
    """
    try:
        balance_info = get_all_balances(public_key)
        return jsonify(balance_info), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(port=5000)
