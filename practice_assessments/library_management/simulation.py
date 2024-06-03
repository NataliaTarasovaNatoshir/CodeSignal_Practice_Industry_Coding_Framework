class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.borrowed_by = None
        self.borrow_time = None
        self.borrow_history = []


class Library:
    def __init__(self):
        self.books = {}
        self.users_history = {}
        self.paid_fines = {}

    def add_book(self, *vals):
        title, author, isbn = vals[0], vals[1], vals[2]
        if isbn not in self.books:
            self.books[isbn] = Book(isbn, title, author)
            return f"Book {title} added"
        else:
            return ""

    def remove_book(self, *vals):
        isbn = vals[0]
        if isbn in self.books:
            title = self.books[isbn].title
            del self.books[isbn]
            return f"Book {title} removed"
        else:
            return ""

    def find_book(self, *vals):
        isbn = vals[0]
        if isbn in self.books:
            return f"Book {self.books[isbn].title}"
        else:
            return "Book not found"

    def borrow_book(self, *vals):
        isbn, user_id, days = vals[0], vals[1], vals[2]
        if isbn in self.books:
            if self.books[isbn].borrowed_by is None:
                self.books[isbn].borrowed_by = user_id
                self.books[isbn].borrow_time = days
                self.books[isbn].borrow_history.append(user_id)
                if user_id not in self.users_history:
                    self.users_history[user_id] = []
                self.users_history[user_id].append(isbn)
                return f"{self.books[isbn].title} borrowed by {user_id}"
            else:
                return f"{self.books[isbn].title} is already borrowed by {self.books[isbn].borrowed_by}"
        else:
            "Book not found"
    def return_book(self, *vals):
        isbn = vals[0]
        if isbn in self.books:
            self.books[isbn].borrowed_by = None
            return f"{self.books[isbn].title} returned"
        else:
            "Book not found"

    def check_availability(self, *vals):
        isbn = vals[0]
        if isbn in self.books:
            if self.books[isbn].borrowed_by == None:
                return f"{self.books[isbn].title} is available"
            else:
                return f"{self.books[isbn].title} is already borrowed by {self.books[isbn].borrowed_by}"
        else:
            "Book not found"

    def borrowing_history(self, *vals):
        isbn = vals[0]
        if isbn in self.books:
            h = ", ".join(self.books[isbn].borrow_history)
            return f"Borrowing history: [{h}]"
        else:
            "Book not found"

    def user_history(self, *vals):
        user_id = vals[0]
        if user_id in self.users_history:
            h = ", ".join([self.books[isbn].title for isbn in self.users_history[user_id]])
            return f"User history for {user_id}: [{h}]"
        else:
            "User not found"

    def calculate_fine(self, *vals):
        isbn, total_days = vals[0], vals[1]
        fine_size = max(0, total_days - self.books[isbn].borrow_time)
        return f"Fine for {self.books[isbn].title} is ${fine_size}"

    def pay_fine(self, *vals):
        user_id, fine_sum = vals[0], vals[1]
        if user_id in self.paid_fines:
            self.paid_fines[user_id].append(fine_sum)
        else:
            self.paid_fines[user_id] = [fine_sum]
        return f"Fine paid by {user_id}: ${fine_sum}"

def simulate_library_operations(list_of_lists):
    """
    Simulates a coding framework operation on a list of lists of strings.

    Parameters:
    list_of_lists (List[List[str]]): A list of lists containing strings.
    """
    res = []
    library = Library()
    for query in list_of_lists:
        command_name = query[0].lower()
        args = query[1:]
        res.append(getattr(library, command_name)(*args))
    return res
