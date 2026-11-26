import base64
import hashlib
import json
import argparse
import datetime
import base58
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator
from nacl.signing import SigningKey
from rich import print


def generate_wallet(prefix):
    mnemonic = Bip39MnemonicGenerator().FromWordsNumber(24)
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    entropy = hashlib.sha256(seed_bytes).hexdigest()[:32]
    signing_key = SigningKey(seed_bytes[:32])
    verify_key = signing_key.verify_key
    priv_key_bytes = signing_key.encode()
    pub_key_bytes = verify_key.encode()
    sha_pub = hashlib.sha256(pub_key_bytes).digest()
    address_body = base58.b58encode(sha_pub).decode()
    address = prefix + address_body
    return {
        "mnemonic": str(mnemonic),
        "private_key_b64": base64.b64encode(priv_key_bytes).decode(),
        "public_key_b64": base64.b64encode(pub_key_bytes).decode(),
        "address": address,
        "entropy": entropy
    }


def save_wallets_json(wallets, prefix):
    with open(f"{prefix}_wallets.json", "w") as f:
        json.dump(wallets, f, indent=4)
    print(f"✅ Saved: {prefix}_wallets.json")


def save_wallets_txt_components(wallets, prefix):
    with open(f"{prefix}_mnemonic.txt", "w") as f_mnemonic, \
         open(f"{prefix}_private_key.txt", "w") as f_priv, \
         open(f"{prefix}_public_key.txt", "w") as f_pub, \
         open(f"{prefix}_address.txt", "w") as f_addr:
        for w in wallets:
            f_mnemonic.write(w["mnemonic"] + "\n")
            f_priv.write(w["private_key_b64"] + "\n")
            f_pub.write(w["public_key_b64"] + "\n")
            f_addr.write(w["address"] + "\n")
    print(f"✅ Saved: {prefix}_mnemonic.txt")
    print(f"✅ Saved: {prefix}_private_key.txt")
    print(f"✅ Saved: {prefix}_public_key.txt")
    print(f"✅ Saved: {prefix}_address.txt")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate Octra wallets dari mnemonic BIP39 24 kata."
    )
    parser.add_argument("--count", type=int, default=None,
                        help="Jumlah wallet yang dibuat (contoh: 5)")
    parser.add_argument("--prefix", type=str, default=None,
                        help="Prefix alamat (contoh: oct)")
    args = parser.parse_args()

    try:
        count = args.count
        if count is None:
            count = int(input("Number of wallets to generate: ").strip())
        prefix = args.prefix
        if prefix is None:
            prefix = input("Address prefix (e.g. oct, etc.) ").strip()
        if not prefix:
            raise ValueError("Prefix tidak boleh kosong")
        if count < 1:
            raise ValueError("Jumlah wallet harus lebih dari 0")
        wallets = [generate_wallet(prefix) for _ in range(count)]
        save_wallets_json(wallets, prefix)
        save_wallets_txt_components(wallets, prefix)
        print(f"\n✅ Berhasil membuat {count} wallet dengan prefix '{prefix}'!")
        print("\n🔎 Contoh alamat wallet pertama:")
        print(f"Address : {wallets[0]['address']}")
        print(f"Mnemonic: {wallets[0]['mnemonic']}")
    except Exception as e:
        print(f"⚠️ Terjadi kesalahan: {e}")
