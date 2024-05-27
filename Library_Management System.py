
books_list = [] # For implimenting a set we will need to use the square bracket.
author = set() # To use the set we use parenthesis ()
Books_dict = {} # For Dictionary we use Curly braces

books_list.append("Python Programming")
author.add("John Smith")
Books_dict["Python Programming"] = "John Smith"

books_list.append("Harry Potter and the Cursed Child")
author.add("J.K Rowling")
Books_dict["Harry Potter and the Cursed Child"] = "J.K Rowling"

books_list.append("Chhota Bheem")
author.add("Shankar Kailash")
Books_dict["Chhota Bheem"] = "Shankar Kailash"

# dislpay all the books. 
for  book in books_list:
    print(book)

# remove a book 
remove_title = input("Enter the Title of th book you want to remove")
if remove_title in books_list:
    remove_author = Books_dict[remove_title]
    books_list.remove(remove_title)
    author.remove(remove_author)
    del Books_dict[remove_title]
    print("Book Removed Successfully")
    print("Book available: " ,books_list)
else:
    print("Book not found!")