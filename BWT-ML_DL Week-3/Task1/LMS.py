class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author
    
    def set_author(self, author):
        self.author = author

    def get_pages(self):
        return self.pages
    
    def set_pages(self, pages):
        self.pages = pages

    @classmethod
    def calculate_reading_time(cls, pages, words_per_minute=250):
        words = pages * 250  # Assuming an average of 250 words per page
        reading_time_minutes = words / words_per_minute
        return reading_time_minutes

class Ebook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.format = format
    
    def __str__(self):
        return f"Ebook - Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Format: {self.format}"

# For Example :
if __name__ == "__main__":
    book1 = Book("Right Thing Right Now", "Ryan Holidat ", 260)
    
    print(f"Initial Title: {book1.get_title()}")
    book1.set_title("Learning Python Programming")
    print(f"Updated Title: {book1.get_title()}")
    
    reading_time = Book.calculate_reading_time(book1.get_pages())
    print(f"Approx. reading time: {reading_time:.2f} minutes")
    
    ebook1 = Ebook("Power of Now", "Clare", 229, "PDF")
    print(ebook1)  # This will call the __str__() method of Ebook
