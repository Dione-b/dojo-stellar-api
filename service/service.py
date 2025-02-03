from stellar_sdk import Server, SorobanServer, soroban_rpc

horizon_server = Server(horizon_url="https://horizon-testnet.stellar.org")
soroban_server = SorobanServer(server_url='https://soroban-testnet.stellar.org', client=None)


def get_block_info(block_id: str):
    """
    Search for information from a block through ID
    """
    ledger = horizon_server.ledgers().ledger(block_id).call()
    return ledger


def get_transaction(tx_hash: str) -> soroban_rpc.GetTransactionResponse:
    """
    Search for information from a transaction through Hash
    """
    tx = soroban_server.get_transaction(tx_hash)
    return tx


def get_all_balances(public_key: str):
    """
    Get all balances from a public key
    """
    balances = {"classic_assets": []}

    try:
        account_data = horizon_server.accounts().account_id(public_key).call()
        balances["classic_assets"] = account_data['balances']
        return balances

    except Exception as e:
        print(f"Error fetching balances: {e}")
        return None
