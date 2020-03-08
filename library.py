import sys
from datetime import date, timedelta

class Library:
      def __init__(self,listofbooks):
            self.availablebooks=listofbooks
            self.listofborrowedbooks = []
            

      def displayAvailablebooks(self):
                   print("The books we have in our library are as follows:")
                   print("================================")
                   for book in self.availablebooks:
                         print(book)
                  
      def lendBook(self,requestedBook):
            today = date.today()
            N = 30
            date_in_thirty_days = date.today() + timedelta(days=N)
            if requestedBook in self.availablebooks:
                  print("The book you requested has now been borrowed")
                  print("You borrowed a book on",today)
                  print("Your book should be returned by",date_in_thirty_days,"or a fine of GHS30 shall be demanded")
                  self.availablebooks.remove(requestedBook)
                  self.listofborrowedbooks.append(requestedBook)
            else:
                  print("Sorry the book you have requested is currently not in the library")
                  
      def addBook(self,returnedBook):
            today = date.today()
            if returnedBook in self.listofborrowedbooks:
                  self.availablebooks.append(returnedBook)
                  print("Thanks for returning your borrowed book")
                  print ("You returned the book on",today)
            elif returnedBook not in self.availablebooks:
                  print ("Sorry the book you are returning does not belong to the library")
            else:
                  print ("Sorry the book you are returning has not yet been borrowed")
           

class Student:
      def requestBook(self):
            print("Enter the name of the book you'd like to borrow>>")
            self.book=input()  
            return self.book
          

      def returnBook(self):
            print("Enter the name of the book you'd like to return>>")
            self.book=input()
            return self.book

def main():            
      library=Library(["The Firm",
                       "The Catcher in the Rye",
                       "The Odyssey",
                       "Adventures of Huckleberry Finn",
                       "In Search of Lost Time",
                       "Wings of Eagle",
                       "Endgame",
                       "Lincoln Lawyer",
                       "Dangerous Fortune",
                       "The Great Gatsby"])
      today = date.today()
      print ( today)
      student=Student()
      done=False
      while done==False:
            print(""" ======LIBRARY MENU=======
                  1. Display all available books
                  2. Borrow a book
                  3. Return a book
                  4. Exit
                  """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                        library.displayAvailablebooks()
            elif choice==2:
                        library.lendBook(student.requestBook())
            elif choice==3:
                        library.addBook(student.returnBook())
            elif choice==4:
                  sys.exit()
                  
main()
