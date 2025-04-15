import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'transactions.json')


def load_transactions():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_transactions(transactions):
    with open(DATA_FILE, 'w') as f:
        json.dump(transactions, f, indent=4)


def add_transaction(transaction):
    transaction['date'] = transaction['date'].isoformat()
    transactions = load_transactions()
    transactions.append(transaction)
    save_transactions(transactions)
