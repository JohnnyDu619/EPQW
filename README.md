# EPQW – Ethereum Post-Quantum Wallet

A hybrid wallet combining ECDSA and post-quantum Dilithium signatures, with Rust-accelerated PQ operations and real Sepolia testnet support.

---

## Overview

EPQW demonstrates a practical approach to quantum-resistant Ethereum transactions:

- **ECDSA (secp256k1)** for full EVM compatibility  
- **Dilithium (NIST FIPS 204)** via **Rust FFI** for quantum safety  
- **Real Sepolia transactions** using `web3.py`  
- **Merkle-based ZK proof** for keyless verification  
- **Performance benchmark** (ECDSA vs. Dilithium)

---

## Features

- Hybrid signing (ECDSA + Dilithium)  
- Real Sepolia testnet broadcasting  
- 3–5× faster Dilithium via `pyo3` + `pqcrypto-dilithium`  
- Merkle tree proof of knowledge  
- Keccak-256 and checksum address support  

---

## Tech Stack

- **Python**: `cryptography`, `web3.py`, `eth-keys`  
- **Rust**: `pqcrypto-dilithium`, `pyo3` (FFI)  
- **Network**: Sepolia testnet (`chainId: 11155111`)  
- **Standards**: NIST PQC, Ethereum Yellow Paper  

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/JohnnyDu619/epqw.git
cd epqw

# 2. Install Python deps
pip install -r requirements.txt

# 3. Build Rust module
cd rust_pq
maturin develop
cd ..

# 4. Run
python main.py
