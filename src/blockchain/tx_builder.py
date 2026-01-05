from web3 import Web3
from web3.types import TxParams


def build_base_tx(w3: Web3, from_address: str) -> TxParams:
    nonce = w3.eth.get_transaction_count(from_address)
    return {
        "from": from_address,
        "nonce": nonce,
    }


def sign_and_send(w3: Web3, tx: TxParams, private_key: str) -> str:
    # Note: gas values are placeholders; you should estimate gas for real usage.
    if "gas" not in tx:
        tx["gas"] = 250000
    if "gasPrice" not in tx:
        tx["gasPrice"] = w3.eth.gas_price

    signed = w3.eth.account.sign_transaction(tx, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    return tx_hash.hex()
