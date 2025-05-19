import random
import time

# Set seed.
random.seed(0)

# List to store the generated credit card numbers.
numbers = []

# Dictionary to store charges per card.
# Position [0] stores the total charge amount, and [1] the number of transactions.
card_charges = {}

# Generate 20,000 random credit card numbers.
for _ in range(20_000):
    # Generate random 16-digit numbers.
    random_number = random.randint(0000000000000000, 9999999999999999)
    # Append to the numbers list.
    numbers.append(random_number)

# Generate 1,000,000 random charges.
for _ in range(1_000_000):
    # Select a random card number.
    random_number = random.choice(numbers)
    # Select a random amount between 10 and 1000 euros.
    random_amount = random.randint(10, 1000)
    
    # If the card is not yet in the dictionary, add it and initialize with amount and 1 transaction.
    if random_number not in card_charges:
        card_charges[random_number] = [random_amount, 1]
    else:
        # Otherwise, update the total and increment the transaction count.
        card_charges[random_number][0] += random_amount
        card_charges[random_number][1] += 1

# Start timing.
start = time.time()

# Compute results: min/max by amount and transaction count.
min_total_payment_card = min(card_charges, key=lambda card: card_charges[card][0])
max_total_payment_card = max(card_charges, key=lambda card: card_charges[card][0])
min_transaction_count_card = min(card_charges, key=lambda card: card_charges[card][1])
max_transaction_count_card = max(card_charges, key=lambda card: card_charges[card][1])

# End timing.
elapsed_time = time.time() - start

# Print results.
print("Results using dictionary:")
print(f"Card with lowest total payments: {min_total_payment_card}, amount: {card_charges[min_total_payment_card][0]} euros.")
print(f"Card with highest total payments: {max_total_payment_card}, amount: {card_charges[max_total_payment_card][0]} euros.")
print(f"Card with lowest number of transactions: {min_transaction_count_card}, count: {card_charges[min_transaction_count_card][1]}.")
print(f"Card with highest number of transactions: {max_transaction_count_card}, count: {card_charges[max_transaction_count_card][1]}.")

# Print total execution time.
print(f"Total execution time: {elapsed_time:.2f} seconds.")


# Class implementing a linear probing hash table.
class Linear_Probing_Hash_Table:
    
    # Initialization function.
    def __init__(self, size=101):
        # Default size is 101.
        self.size = size
        # Create a list with size elements, all initialized to None.
        self.table = [None] * size
        # Initial load factor = 0%.
        self.load_factor = 0

    # Hash function using Jenkins hash.
    def hash_function(self, key):
        hash_value = 0
        key_str = str(key)
        for char in key_str:
            hash_value += ord(char)
            hash_value += (hash_value << 10)
            hash_value ^= (hash_value >> 6)
        hash_value += (hash_value << 3)
        hash_value ^= (hash_value >> 11)
        hash_value += (hash_value << 15)
        return hash_value % self.size

    # Insert a (key, value) pair into the hash table.
    def put(self, key, value):
        # Compute index via the hash function.
        index = self.hash_function(key)
        # Linear probing to find an empty slot.
        while self.table[index] is not None:
            index = (index + 1) % self.size
        # Insert the pair.
        self.table[index] = (key, value)
        # Update load factor.
        self.load_factor += 1 / self.size
        # Rehash if load factor exceeds 70%.
        if self.load_factor >= 0.7:
            self.rehash()

    # Retrieve a value by key from the hash table.
    def get(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            # Check if key matches.
            if self.table[index][0] == key:
                return self.table[index][1]
            # Otherwise move to the next index via linear probing.
            index = (index + 1) % self.size
        return None

    # Check if a number is prime.
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Find the next prime number ≥ n.
    def next_prime(self, n):
        n += 1
        while not self.is_prime(n):
            n += 1
        return n

    # Rehash the table to a new size (next prime ≥ 2×current).
    def rehash(self):
        new_size = self.next_prime(self.size * 2)
        new_table = [None] * new_size
        count = 0
        for item in self.table:
            if item is not None:
                key, value = item
                index = self.hash_function(key)
                while new_table[index] is not None:
                    index = (index + 1) % new_size
                new_table[index] = (key, value)
                count += 1
        self.size = new_size
        self.table = new_table
        self.load_factor = count / new_size

# Create a hash table instance.
hash_table = Linear_Probing_Hash_Table()
# Number of transactions to simulate.
N = 10_000

# Generate 20,000 additional card numbers.
for _ in range(20_000):
    random_number = random.randint(0000000000000000, 9999999999999999)
    numbers.append(random_number)

# Perform transactions and update hash table.
for _ in range(N):
    random_number = random.choice(numbers)
    random_amount = random.randint(10, 1000)
    
    # If card is not in the table, add it.
    if hash_table.get(random_number) is None:
        hash_table.put(random_number, [random_amount, 1])
    else:
        # Otherwise, update the existing entry.
        card_info = hash_table.get(random_number)
        card_info[0] += random_amount
        card_info[1] += 1

# Compute and print results using the hash table.
start = time.time()

min_total_payment_card_table = min(hash_table.table, key=lambda item: item[1][0] if item is not None else float('inf'))
max_total_payment_card_table = max(hash_table.table, key=lambda item: item[1][0] if item is not None else float('-inf'))
min_transaction_count_card_table = min(hash_table.table, key=lambda item: item[1][1] if item is not None else float('inf'))
max_transaction_count_card_table = max(hash_table.table, key=lambda item: item[1][1] if item is not None else float('-inf'))

elapsed_time_table = time.time() - start

print(f"\nResults using hash table for {N} credit card charges:")
print(f"Card with lowest total payments: {min_total_payment_card_table[0]}, amount: {min_total_payment_card_table[1][0]} euros.")
print(f"Card with highest total payments: {max_total_payment_card_table[0]}, amount: {max_total_payment_card_table[1][0]} euros.")
print(f"Card with lowest number of transactions: {min_transaction_count_card_table[0]}, count: {min_transaction_count_card_table[1][1]}.")
print(f"Card with highest number of transactions: {max_transaction_count_card_table[0]}, count: {max_transaction_count_card_table[1][1]}.")

print(f"Total execution time: {elapsed_time_table:.2f} seconds.")
