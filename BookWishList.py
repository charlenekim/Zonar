from flask import Flask
#import View

app = Flask(__name__)

@app.route("/")
def index():
	pass
	
@app.route("/login")
def login(email, password):
	pass

@app.route("/createAccount")
def login(firstName, lastName, email, password):
	pass

@app.route("/books")
def getBooks():
	pass

@app.route("/book/{id}")
def getBookDetails(summary=''):
	pass

# list of books: UserBook entries with matching userId
# only available for logged in users
@app.route("/myBooks")
def getMyBooks(userId):
	pass

@app.route("/book/add")
def addBook(bookTitle, bookAuthor, ISBN=None, pubYear=None):
	pass
	
@app.route("/book/edit/{id}")
def editBook(bookId, bookTitle, bookAuthor, ISBN=None, pubYear=None):
	pass
	
@app.route("/book/delete/{id}")
def deleteBook(bookId):
	pass

@app.route("/logout")
def logout(userId):
	pass
