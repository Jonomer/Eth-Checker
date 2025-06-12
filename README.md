# 🧺 Ethereum Wallet Balance Checker

A Python tool for checking the balance of Ethereum wallets generated from a list of mnemonic seed phrases.
Used mainly for educational or recovery purposes.

---

## 🚀 Features

* Reads mnemonics from a text file (`seeds.txt`)
* Converts them into Ethereum wallets
* Checks ETH balance via Infura Mainnet API
* Saves wallets with non-zero balance into a log file

---

## 🛠️ Requirements

* Python 3.7+
* Infura API Key

Install dependencies:

```bash
pip install web3 eth-account
```

---

## 📄 Usage

1. Put your seed phrases into a file named `seeds.txt`, one per line.
2. Replace `INFURA_URL` in the script with your own Infura key.
3. Run the script:

```bash
python main.py
```

4. Results will be saved in `results.txt`.

---

## ⚠️ Warning

This tool is intended for **educational, testing, or recovery** purposes only.
Using this script for unauthorized access to Ethereum wallets is illegal and unethical.

---

## 🧑‍💻 Author

**Enver**
Cybersecurity Student | Bash Lover | Exploit Curious

---

> *“chmod +x life.sh && ./live”*
