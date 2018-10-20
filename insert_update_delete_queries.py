from create_table import engine
from sqlalchemy.orm import sessionmaker
from create_table import Student, Book


Session = sessionmaker(bind=engine)
session = Session()


#insert data to Student Table
insert_to_student = Student(
    name = "John Week",
    class_name = "TY Bech",
)
session.add(insert_to_student)


#insert data to Book Table
insert_to_book = Book(
    title = "7 habits of highly effective people",
    desciption = "in 1989, is a business and self-help book written by Stephen Covey.",
    author_name = "Stephen Covey",
    pages = 381

)

session.add(insert_to_book)


#Delete from Student where id=1
session.query(Student).filter(Student.id==1).delete()

#Delete from Book where id=1
session.query(Book).filter(Book.id==1).delete()

session.commit()


#Update Student
session.query(Student).filter(Student.id==2).update({"name": "Tom Jerry"})
session.commit()


#select Student
result = session.query(Student).filter_by(id=2).first()
print result.name


#select Book
book_result = session.query(Book).filter_by(id=2).all()
print book_result[0].title