# Octra Wallet Generator

Generate Octra wallets dari Python: tiap wallet dibuat dari mnemonic BIP39 24 kata, lalu diturunkan jadi Ed25519 keypair dengan prefix alamat yang bisa dipilih (misalnya `oct`).

## Install

```bash
pip install -r requirements.txt
```

Dependencies: `bip-utils`, `pynacl`, `base58`, `rich`.

## Cara pakai

```bash
python3 octra.py
```

Saat diminta address prefix, ketik prefix yang diinginkan (contoh: `oct`).

## Output

Untuk tiap batch, script menyimpan:

- `<prefix>_wallets.json` — semua wallet (mnemonic, private key, public key, address)
- `<prefix>_mnemonic.txt` — daftar mnemonic
- `<prefix>_private_key.txt` — daftar private key (base64)
- `<prefix>_public_key.txt` — daftar public key (base64)

## Peringatan keamanan

Mnemonic dan private key adalah rahasia penuh atas wallet. Jangan dibagikan ke siapa pun, jangan di-commit ke repo, dan jangan disimpan di tempat yang bisa diakses orang lain.

## Mode non-interaktif

```bash
python3 octra.py --count 5 --prefix oct
```

Tanpa flag, script tetap bertanya secara interaktif seperti biasa.

## Contoh hasil

```bash
$ python3 octra.py --count 1 --prefix oct
✅ Saved: oct_wallets.json
✅ Saved: oct_mnemonic.txt
✅ Saved: oct_private_key.txt
✅ Saved: oct_public_key.txt
✅ Saved: oct_address.txt

✅ Berhasil membuat 1 wallet dengan prefix 'oct'!
```

`oct_address.txt` berisi alamat-alamat yang dihasilkan. Mnemonic dan private key hanya ada di file `.txt`/`.json` masing-masing - simpan baik-baik dan jangan dibagikan.
