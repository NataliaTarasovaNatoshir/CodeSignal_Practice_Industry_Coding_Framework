import unittest
from practice_assessments.library_management.simulation import simulate_library_operations

class TestLibraryManagement(unittest.TestCase):

    def setUp(self):
        self.test_data_1 = [
            ["ADD_BOOK", "1984", "George Orwell", "978-0451524935"],
            ["REMOVE_BOOK", "978-0451524935"],
            ["FIND_BOOK", "978-0451524935"]
        ]
        self.test_data_2 = [
            ["ADD_BOOK", "Animal Farm", "George Orwell", "978-0451526342"],
            ["BORROW_BOOK", "978-0451526342", "user123"],
            ["RETURN_BOOK", "978-0451526342"],
            ["CHECK_AVAILABILITY", "978-0451526342"]
        ]
        self.test_data_3 = [
            ["ADD_BOOK", "Brave New World", "Aldous Huxley", "978-0060850524"],
            ["BORROW_BOOK", "978-0060850524", "user456"],
            ["BORROWING_HISTORY", "978-0060850524"],
            ["USER_HISTORY", "user456"]
        ]
        self.test_data_4 = [
            ["ADD_BOOK", "Catch-22", "Joseph Heller", "978-1451626650"],
            ["BORROW_BOOK", "978-1451626650", "user789", 15],  # Borrowed for 15 days
            ["CALCULATE_FINE", "978-1451626650", 20],  # 5 days overdue
            ["PAY_FINE", "user789", 5]
        ]

    def test_level1_basic_library_operations(self):
        output = simulate_library_operations(self.test_data_1)
        self.assertEqual(output, ["Book 1984 added", "Book 1984 removed", "Book not found"])

    def test_level2_borrowing_and_returning(self):
        output = simulate_library_operations(self.test_data_2)
        self.assertEqual(output, ["Book Animal Farm added", "Animal Farm borrowed by user123", "Animal Farm returned", "Animal Farm is available"])

    def test_level3_tracking_history(self):
        output = simulate_library_operations(self.test_data_3)
        self.assertEqual(output, ["Book Brave New World added", "Brave New World borrowed by user456", "Borrowing history: [user456]", "User history for user456: [Brave New World]"])

    def test_level4_fine_calculation_and_payment(self):
        output = simulate_library_operations(self.test_data_4)
        self.assertEqual(output, ["Book Catch-22 added", "Catch-22 borrowed by user789", "Fine for Catch-22 is $5", "Fine paid by user789: $5"])

if __name__ == '__main__':
    unittest.main()