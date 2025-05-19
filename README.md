# Fast Credit-Card Charge Aggregator

> Course project for **Algorithms & Complexity** (5th semester) — Department of Computer Science & Telecommunications, University of Ioannina

## Problem Statement
Generate **1 000 000** synthetic credit-card charges across **20 000** random card numbers and compute per-card aggregates (total amount & transaction count). The goal is to compare different data-structure choices and implement a custom hash table with linear probing.

## Approach
1. **Pandas DataFrame**  
   Naïve approach using row-wise appending. Very slow for large data.

2. **Python built-in dictionary**  
   Key = card number, value = [total, transactions]; fast.

3. **Custom Linear-Probing Hash Table**  
   Manual implementation using Jenkins hash, prime resizing, and linear probing.

## Complexity
| Operation | Dictionary | Custom Hash Table |
|-----------|------------|-------------------|
| `put` / `get` average | O(1) | O(1) (amortised) |
| Worst-case | O(n) | O(n) |
| Memory | Θ(n) | Θ(n) |

## Benchmarks
| Method | 1 000 000 charges | 10 000 charges |
|--------|------------------|----------------|
| Pandas DataFrame | ~0.35 s |
| Python `dict` | ~0.01–0.02 s |
| Linear-Probing Hash Table | ~same as dict for 10K; slower for 1M due to collisions |

*(Machine: Ryzen 5 5600U · Python 3.11)*

## How to Run
```bash
git clone https://github.com/<your-username>/fast-cc-aggregator.git
cd fast-cc-aggregator
python fast_cc_charge_aggregator.py
