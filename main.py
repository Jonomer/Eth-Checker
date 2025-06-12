import os
from web3 import Web3
from eth_account import Account


Account.enable_unaudited_hdwallet_features()

INFURA_URL = "https://mainnet.infura.io/v3/YOU_INFURA_KEY"

web3 = Web3(Web3.HTTPProvider(INFURA_URL))
if not web3.is_connected():
    print("Error: Unable to connect to the Ethereum node.")
    exit()

def load_seeds(file_path="seeds.txt"):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        exit()
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def check_balance(address):
    try:
        balance = web3.eth.get_balance(address)
        return Web3.from_wei(balance, "ether")  
    except Exception as e:
        print(f"Error checking balance for {address}: {e}")
        return None


def save_results(results, filename="results.txt"):
    with open(filename, "w") as file:
        file.write("\n".join(results))
    print(f"Results saved to {filename}")

def main():
    seeds = load_seeds()
    print(f"Loaded {len(seeds)} seed phrases.")
    results = []

    try:
        for i, seed in enumerate(seeds, 1):
            try:
                wallet = Account.from_mnemonic(seed)
                address = wallet.address
                print(f"[{i}/{len(seeds)}] Checking wallet: {address}")

                
                balance = check_balance(address)
                if balance and balance > 0:
                    print(f"Wallet {address} has a balance of {balance} ETH.")
                    results.append(f"{address} - {balance} ETH (Seed: {seed})")
                else:
                    print(f"Wallet {address} has no balance.")
            except Exception as e:
                print(f"Error with seed: {seed}, {e}")

    except KeyboardInterrupt:
        print("\nProcess interrupted by user (Ctrl+C). Saving results so far...")

    
    if results:
        save_results(results)
    else:
        print("No wallets with balance found.")

if __name__ == "__main__":
    main()