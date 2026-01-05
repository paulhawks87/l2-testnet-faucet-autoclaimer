from web3 import Web3
from .tx_builder import build_base_tx, sign_and_send


FAUCET_ABI_PLACEHOLDER = [
    # Placeholder ABI - replace with your contract ABI
    {
        "inputs": [{"internalType": "address", "name": "recipient", "type": "address"}],
        "name": "claim",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    }
]


class FaucetContractClaimer:
    """
    Generic contract-based claimer (placeholder).
    Replace ABI + function name/params to match your faucet distributor contract.
    """

    def __init__(self, w3: Web3, contract_address: str):
        self.w3 = w3
        self.contract = w3.eth.contract(
            address=Web3.to_checksum_address(contract_address),
            abi=FAUCET_ABI_PLACEHOLDER,
        )

    def claim(self, from_address: str, private_key: str, recipient: str) -> str:
        from_addr = Web3.to_checksum_address(from_address)
        recipient_addr = Web3.to_checksum_address(recipient)

        base_tx = build_base_tx(self.w3, from_addr)
        tx = self.contract.functions.claim(recipient_addr).build_transaction(base_tx)

        return sign_and_send(self.w3, tx, private_key)
