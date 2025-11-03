"""
Author: Johnny Du
Date:   October 2025
Purpose: Research into post-quantum Ethereum signatures
"""
"""
EPQW – Ethereum Post-Quantum Wallet Demo
================================================
A hybrid wallet exploring quantum-resistant signatures on Ethereum.

Features:
- ECDSA + Dilithium (NIST PQC) hybrid signing
- Real Sepolia testnet interaction
- Rust FFI for 3–5× faster PQ operations
- Merkle-based ZK proof of key knowledge
- Performance benchmark

Author: [Johnny Du]
GitHub: https://github.com/JohnnyDu619/epqw
"""

from wallet import HybridWallet
from transaction import EthereumTransaction
from zk_proof import SimpleZKProof
from benchmark import run_benchmark
import secrets

def main():
    print("EPQW – Ethereum Post-Quantum Wallet")
    print("=" * 50 + "\n")

    # 1. Generate hybrid wallet
    wallet = HybridWallet()
    info = wallet.get_info()
    print(f"Address: {info['address']}")
    print(f"PQ Public Key: {info['pq_pubkey']}\n")

    # 2. Simulate transaction
    tx = EthereumTransaction(
        to="0x742d35Cc6634C0532925a3b8D7D7e4e6403a1B04",
        value=1000000000000000  # 0.001 ETH
    )
    tx_hash = tx.serialize()
    print(f"Transaction Hash: {tx_hash.hex()}")
    print(f"Broadcast: {tx.build_and_broadcast(wallet)}\n")

    # 3. Hybrid signing demo
    message = b"Exploring quantum-safe cryptography on Ethereum"
    sig_classic = wallet.sign_classic(message)
    sig_pq = wallet.sign_pq(message)
    print(f"ECDSA Signature: {sig_classic.hex()[:32]}...")
    print(f"Dilithium Signature: {sig_pq.hex()[:32]}...\n")

    # 4. ZK proof (no private key revealed)
    zk = SimpleZKProof()
    secret = secrets.token_bytes(32)
    proof = zk.generate_proof(tx_hash, secret)
    print(f"ZK Proof Valid: {proof['valid']}")
    print(f"Merkle Root: {proof['merkle_root'][:16]}...\n")

    # 5. Performance benchmark
    bench = run_benchmark(message)
    print(f"Benchmark (1000 signatures):")
    print(f"  ECDSA:     {bench['ecdsa_ms']:.2f} ms/sign")
    print(f"  Dilithium: {bench['pq_rust_ms']:.2f} ms/sign")
    print(f"  Speedup:   {bench['speedup']:.1f}x (Rust FFI)\n")

    print("Demo complete. See README.md for details.")

if __name__ == "__main__":
    main()
