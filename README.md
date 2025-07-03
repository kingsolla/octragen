# octragen
octra wallet generacrot

⚡ How to install dependencies
Create a file called requirements.txt with:

bip-utils
pynacl
base58
rich
Then install:

pip install -r requirements.txt
🚀 How to run
After installing dependencies:

python Gen_wallet.py
You will be prompted:

Number of wallets to generate

Address prefix (e.g. oct, etc.)

📂 What files will it create?
Assuming you enter prefix = lumera, it will generate these files:

✅ oct_wallets.json
Contents: Full JSON dump of all wallets.

Each entry contains:

mnemonic (24-word phrase)

private_key_b64 (Base64)

public_key_b64 (Base64)

address (prefix + Base58(SHA256(pubkey)))

entropy (internal identifier)

Purpose: Complete backup, import/export, auditing.

✅ lumera_mnemonic.txt
Contents: All generated mnemonic phrases, one per line.

Purpose: Human-readable backup of recovery phrases.

Usage: Can be used to restore wallet access anywhere.

✅ oct_private_key.txt
Contents: Base64-encoded private keys, one per line.

Purpose: Wallet signing authority.

⚠️ WARNING: Do not share! Whoever owns this can control the funds.

✅ oct_public_key.txt
Contents: Base64-encoded public keys, one per line.

Purpose: For verification and identity.

Usage: Safe to share for verifying signatures.
