import unittest
from simulation import simulate_event_operations

class TestEventManagement(unittest.TestCase):

    def setUp(self):
        self.test_data_1 = [
            ["CREATE_EVENT", "Conference 2024", "2024-05-20", "New York"],
            ["EDIT_EVENT", "Conference 2024", "2024-05-21", "New York"],
            ["CANCEL_EVENT", "Conference 2024"]
        ]
        self.test_data_2 = [
            ["CREATE_EVENT", "Workshop", "2024-06-15", "Chicago"],
            ["REGISTER_PARTICIPANT", "Workshop", "John Doe"],
            ["REMOVE_PARTICIPANT", "Workshop", "John Doe"],
            ["LIST_PARTICIPANTS", "Workshop"]
        ]
        self.test_data_3 = [
            ["CREATE_EVENT", "Seminar", "2024-07-01", "Los Angeles"],
            ["RESCHEDULE_EVENT", "Seminar", "2024-07-02"],
            ["SET_REMINDER", "Seminar", "2024-06-30"],
            ["VIEW_SCHEDULE", "2024-07-02"]
        ]
        self.test_data_4 = [
            ["CREATE_EVENT", "Gala", "2024-08-20", "Miami"],
            ["SET_TICKET_PRICE", "Gala", 150],
            ["PROCESS_PAYMENT", "Gala", "Alice Smith", 150],
            ["FINANCIAL_REPORT", "Gala"]
        ]

    def test_level1_basic_event_setup(self):
        output = simulate_event_operations(self.test_data_1)
        self.assertEqual(output, ["Event Conference 2024 created", "Event Conference 2024 rescheduled", "Event Conference 2024 cancelled"])

    def test_level2_participant_management(self):
        output = simulate_event_operations(self.test_data_2)
        self.assertEqual(output, ["Event Workshop created", "John Doe registered for Workshop", "John Doe removed from Workshop", "Participants in Workshop: []"])

    def test_level3_advanced_scheduling(self):
        output = simulate_event_operations(self.test_data_3)
        self.assertEqual(output, ["Event Seminar created", "Seminar rescheduled to 2024-07-02", "Reminder set for Seminar on 2024-06-30", "Events on 2024-07-02: [Seminar]"])

    def test_level4_financial_operations(self):
        output = simulate_event_operations(self.test_data_4)
        self.assertEqual(output, ["Event Gala created", "Ticket price for Gala set at $150", "Payment processed for Alice Smith: $150", "Financial report for Gala: Total income $150"])

if __name__ == '__main__':
    unittest.main()