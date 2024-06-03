import unittest
from simulation import simulate_coding_framework

class TestBankingOperations(unittest.TestCase):

    def setUp(self):
        self.test_data_1 = [
            ["CREATE_ACCOUNT", "123", 100],
            ["DEPOSIT", "123", 200],
            ["TRANSFER", "123", "456", 150],
            ["VIEW_BALANCE", "123"]
        ]
        self.test_data_2 = [
            ["CREATE_ACCOUNT", "abc", 500],
            ["CREATE_ACCOUNT", "def", 500],
            ["TRANSFER", "abc", "def", 300],
            ["TOP_OUTGOING", 1]
        ]
        self.test_data_3 = [
            ["CREATE_ACCOUNT", "xyz", 100],
            ["SCHEDULE_TRANSACTION", "deposit", "xyz", 50, '2025-01-01'],
            ["EXECUTE_SCHEDULED", '2025-01-01'],  # Assuming the scheduled date arrives
            ["CANCEL_TRANSACTION", "xyz", '2025-01-02'],  # Cancel a non-existent transaction
            ["TRANSACTION_HISTORY", "xyz"]
        ]
        self.test_data_4 = [
            ["CREATE_ACCOUNT", "001", 200],
            ["CREATE_ACCOUNT", "002", 300],
            ["TRANSFER", "001", "002", 100],
            ["MERGE_ACCOUNTS", "001", "002"],
            ["VIEW_TRANSACTION_HISTORY", "001"]
        ]

    def test_level1_basic_operations(self):
        output = simulate_coding_framework(self.test_data_1)
        self.assertEqual(output, ["Account 123 created", "123 deposited 200", "150 transferred from 123 to 456", "Balance for 123 is 250"])

    def test_level2_transaction_metrics(self):
        output = simulate_coding_framework(self.test_data_2)
        self.assertEqual(output, ["Account abc created", "Account def created", "300 transferred from abc to def", "Top outgoing account is abc"])

    def test_level3_scheduled_transactions(self):
        output = simulate_coding_framework(self.test_data_3)
        self.assertEqual(output, ["Account xyz created", "Transaction scheduled for 2025-01-01", "Transaction executed", "No transaction to cancel", "Transaction history for xyz"])

    def test_level4_account_merging(self):
        output = simulate_coding_framework(self.test_data_4)
        self.assertEqual(output, ["Account 001 created", "Account 002 created", "100 transferred from 001 to 002", "Accounts 001 and 002 merged", "Transaction history for 001 includes transfers and merge details"])

if __name__ == '__main__':
    unittest.main()