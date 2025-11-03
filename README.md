# EPQW
Post-quantum Ethereum wallet with Rust FFI &amp; Sepolia testnet
# EPQW: Ethereum Post-Quantum Wallet

A hybrid quantum-resistant wallet for Ethereum

Python 3.10+ | Rust 1.70+ | Ethereum Sepolia | MIT License

---

## Overview

EPQW (Ethereum Post-Quantum Wallet) is a hybrid cryptographic wallet that combines:

- Classical ECDSA (secp256k1) for Ethereum compatibility
- Post-quantum Dilithium (NIST FIPS 204) via Rust FFI for quantum resistance
- Real Sepolia testnet transactions using web3.py
- ZK-style Merkle proofs for privacy-preserving verification
- Performance benchmarking (ECDSA vs. Dilithium)

This project demonstrates a practical path toward Ethereum's post-quantum migration, aligning with EF's research in quantum resistance and Verkle trees.

---

## Features

- Hybrid Signing: ECDSA + Dilithium (Rust-accelerated)
- Real Testnet Tx: Broadcasts signed transactions to Sepolia
- Rust FFI: 3–5× faster Dilithium via pyo3 + pqcrypto-dilithium
- ZK Proof: Merkle tree-based proof of knowledge without revealing keys
- Benchmarking: Compares signing speed (ECDSA vs. PQ)
- EVM Compatible: Uses Keccak-256, checksum addresses

---

## Tech Stack

- Python: cryptography, web3.py, eth-keys
- Rust: pqcrypto-dilithium, pyo3 (FFI)
- Ethereum: Sepolia testnet (chain ID: 11155111)
- Standards: NIST PQC, Ethereum Yellow Paper

---

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/epqw.git
cd epqw

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Build Rust FFI module
cd rust_pq
maturin develop
cd ..

# 4. Run demo
python main.py
