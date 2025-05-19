# Fast Credit-Card Charge Aggregator

> Course project for **Algorithms & Complexity** (5th semester) — Department of Informatics and Telecommunications of the University of Ioannina.

## Problem Statement
Generate **1 000 000** synthetic credit-card charges across **20 000** random card numbers and compute per-card aggregates (total amount & transaction count). The goal is to compare different data-structure choices and implement a custom hash table with linear probing.

## Approach
1. **Pandas DataFrame**  
   Naïve approach using row-wise appending. Very slow for large data.

2. **Python built-in dictionary**  
   Key = card number, value = `[total_amount, transactions]`; fast.

3. **Custom Linear-Probing Hash Table**  
   Manual implementation using Jenkins hash, prime resizing, and linear probing.

## Complexity
| Operation            | Dictionary | Custom Hash Table |
|----------------------|------------|-------------------|
| `put` / `get` avg.   | O(1)       | O(1) (amortised)  |
| Worst-case           | O(n)       | O(n)              |
| Memory               | Θ(n)       | Θ(n)              |

## Benchmarks
| Method                     | 1 000 000 charges | 10 000 charges |
|----------------------------|------------------|----------------|
| Pandas DataFrame           | ~0.35 s          | —              |
| Python `dict`              | ~0.01–0.02 s     | —              |
| Linear-Probing Hash Table  | —                | ~0.01 s        |

*(Machine: Ryzen 5 5600U · Python 3.11)*

## How to Run
```bash
git clone https://github.com/konrantos/cc-hash-aggregator.git
cd cc-hash-aggregator
python cc-hash-aggregator.py
```

## Output Example
```
Results using dictionary:
Card with lowest total payments: 532437998554836, amount: 11881 euros.
Card with highest total payments: 2545452946481910, amount: 43888 euros.
Card with lowest number of transactions: 3365852352567254, count: 25.
Card with highest number of transactions: 5209439849770051, count: 80.
Total execution time: 0.01 seconds.

Results using hash table for 10000 credit card charges:
Card with lowest total payments: 9988142345057134, amount: 10 euros.
Card with highest total payments: 8870159902148392, amount: 2465 euros.
Card with lowest number of transactions: 2807632396130387, count: 1.
Card with highest number of transactions: 4449804892512562, count: 3.
Total execution time: 0.01 seconds.
```

## Project Files
```
cc-hash-aggregator/
├── cc-hash-aggregator.py          # Source code with English comments
├── README.md                      # Documentation
├── LICENSE                        # MIT license
├── .gitignore                     # Python exclusions
└── .github/
    └── workflows/
        └── python.yml             # GitHub Actions for CI
```

## License

This project is licensed under the MIT License.

## Acknowledgements

- University of Ioannina — course project for *Algorithms & Complexity*
- Inspired by Python’s built-in dictionary and hashing internals
