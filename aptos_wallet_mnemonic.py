from mnemonic import Mnemonic
from utils import PublicKeyUtils
from aptos_sdk.account import Account
import csv

wallets_amount = int(input("How many wallets to generate ?: "))

csv_filename = "aptos_wallets.csv"

with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Wallet", "Private Key", "Seed Phrase"])  # Write header

    for _ in range(wallets_amount):
        words = Mnemonic("english").generate()
        path = f"m/44'/637'/1'/0'/0'"
        pt = PublicKeyUtils(words, path)
        apt_account = Account.load_key(pt.private_key.hex())

        data = [(apt_account.address(), f"0x{pt.private_key.hex()}", words)]

        writer.writerows(data)  # Write the data rows
