from book import Book

books=[]
with open("books.txt") as file:
    for line in file:
        title,author,genre=line.strip().split(",")
        book=Book(title, author, genre)
        books.append(book)


print(books[0].get_title())
print(books[0].get_author())
print(books[0].get_genre())
print(books[0].is_checked_out())

books[0].check_out()
print(books[0])

books[0].return_book()
print(books[0])


print(books[2])