from datetime import datetime, timedelta

# Base class
class LibraryItem:
    def __init__(self, title: str, author: str, item_id: str):
        self.title = title
        self.author = author
        self.item_id = item_id
        self._checkout_status = False
        self._checkout_date = None

    def checkout(self):
        if not self._checkout_status:
            self._checkout_status = True
            self._checkout_date = datetime.now()
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        self._checkout_status = False
        self._checkout_date = None

    def get_info(self):
        status = "Checked out" if self._checkout_status else "Available"
        date_str = self._checkout_date.strftime("%Y-%m-%d %H:%M:%S") if self._checkout_date else "N/A"
        return f"{self.title} by {self.author} (ID: {self.item_id})\nStatus: {status} on {date_str}"

    def calculate_late_fee(self, return_date: datetime):
        """To be overridden in subclasses"""
        return 0.0

    def is_overdue(self, current_date: datetime):
        if self._checkout_status and self._checkout_date:
            return (current_date - self._checkout_date).days > 14
        return False


# Derived class: Book
class Book(LibraryItem):
    def __init__(self, title, author, item_id, pages, genre):
        super().__init__(title, author, item_id)
        self.pages = pages
        self.genre = genre

    def get_info(self):
        base_info = super().get_info()
        return f"Book: {self.title} by {self.author} (ID: {self.item_id})\nPages: {self.pages}, Genre: {self.genre}\nStatus: {'Checked out on ' + self._checkout_date.strftime('%Y-%m-%d %H:%M:%S') if self._checkout_status else 'Available'}"

    def calculate_late_fee(self, return_date: datetime):
        if not self._checkout_status or not self._checkout_date:
            return 0.0
        overdue_days = max((return_date - self._checkout_date).days - 14, 0)
        return overdue_days * 0.50


# Derived class: Magazine
class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number, publication_date):
        super().__init__(title, author, item_id)
        self.issue_number = issue_number
        self.publication_date = publication_date

    def get_info(self):
        return f"Magazine: {self.title} by {self.author} (ID: {self.item_id})\nIssue: {self.issue_number}, Published: {self.publication_date}\nStatus: {'Checked out on ' + self._checkout_date.strftime('%Y-%m-%d %H:%M:%S') if self._checkout_status else 'Available'}"

    def calculate_late_fee(self, return_date: datetime):
        if not self._checkout_status or not self._checkout_date:
            return 0.0
        overdue_days = max((return_date - self._checkout_date).days - 14, 0)
        return overdue_days * 0.25


# Derived class: DVD
class DVD(LibraryItem):
    def __init__(self, title, author, item_id, duration, rating):
        super().__init__(title, author, item_id)
        self.duration = duration
        self.rating = rating

    def get_info(self):
        return f"DVD: {self.title} by {self.author} (ID: {self.item_id})\nDuration: {self.duration} minutes, Rating: {self.rating}\nStatus: {'Checked out on ' + self._checkout_date.strftime('%Y-%m-%d %H:%M:%S') if self._checkout_status else 'Available'}"

    def calculate_late_fee(self, return_date: datetime):
        if not self._checkout_status or not self._checkout_date:
            return 0.0
        overdue_days = max((return_date - self._checkout_date).days - 14, 0)
        return overdue_days * 1.00


# Example Usage
if __name__ == "__main__":
    book = Book("The Python Guide", "John Doe", "B001", 350, "Programming")
    magazine = Magazine("Tech Today", "Jane Smith", "M001", 42, "2024-01-15")
    dvd = DVD("Python Tutorial", "Tech Corp", "D001", 120, "G")

    # Checkout items
    book.checkout()
    magazine.checkout()
    dvd.checkout()

    # Display information
    print(book.get_info())
    print(magazine.get_info())
    print(dvd.get_info())

    # Calculate late fees (assume return 20 days later)
    return_date = datetime.now() + timedelta(days=20)
    print(f"Book late fee: ${book.calculate_late_fee(return_date):.2f}")
    print(f"Magazine late fee: ${magazine.calculate_late_fee(return_date):.2f}")
    print(f"DVD late fee: ${dvd.calculate_late_fee(return_date):.2f}")