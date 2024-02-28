from web3 import Web3
from eth_account import Account

# Connect to an Ethereum node (replace with your actual Infura project ID)
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/your_infura_project_id'))

# Generate a new Ethereum account
def create_account():
    account = Account.create()
    return account

# Function to send ETH from one address to another
def send_eth(from_address, to_address, amount, private_key_hex):
    nonce = w3.eth.get_transaction_count(from_address)
    transaction = {
        'to': to_address,
        'value': w3.toWei(amount, 'ether'),
        'gas': 21000,  # Adjust gas based on network conditions
        'gasPrice': w3.eth.gas_price,
        'nonce': nonce,
        'chainId': 1  # Mainnet
    }
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key_hex)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return w3.toHex(tx_hash)

# Example usage
if __name__ == "__main__":
    # Create a new account
    new_account = create_account()
    print("New Account Address:", new_account.address)
    print("New Account Private Key:", new_account.key.hex())

    # Sender's address and private key (for testing purposes)
    sender_address = '0x456789'  # Replace with a valid sender address
    sender_private_key_hex = '445657888'  # Assuming a valid private key here (without the '0x' prefix)

    # Send ETH from sender's address to the newly created account
    tx_hash = send_eth(sender_address, new_account.address, 0.1, sender_private_key_hex)
    print("Transaction Hash:", tx_hash)
