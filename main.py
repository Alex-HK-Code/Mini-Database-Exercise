books = []  #this is used to store new inputs

while(True):
	user_selection = input("Enter '1' to add a new book | Enter '2' to view all books | Enter '3' to quit the program\n")

	if(user_selection == str(1)):    #str(1) == '1'
		book_name = input("Enter Book Name\n")
		books.append(book_name)

	elif(user_selection == str(2)):  #str(2) == '2'
		for book in books:   #books is a list, each iteration handles an element as book
			print(book)

	elif(user_selection == str(3)):
		break	#end of program (break while loop)