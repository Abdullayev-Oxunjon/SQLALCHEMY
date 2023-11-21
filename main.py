from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:22@localhost:5432/sqlalchemy",
                       echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    grade = Column(String(10), nullable=False)


Base.metadata.create_all(engine)

# student1 = Student(name="John", age=20, grade="A")
# student2 = Student(name="Jane", age=21, grade="B")
# session.add_all([student1, student2])
# session.commit()

"""Hamma studentlarni chiqarish"""
# students = session.query(Student)
# for student in students:
#     print(student.name, student.age, student.grade)

"""STUDENTNI chiqarish"""
# student = session.query(Student).filter(Student.id == 1).first()
# print(student.name, student.age, student.grade)


"""_or orqali filter qilish"""

# students = session.query(Student).filter(or_(Student.name == "John", Student.name == "Jane"))
# for student in students:
#     print(student.name, student.age, student.grade)


"""Studentlarning sonini chiqarish"""
# students_count = session.query(Student).count()
# print(students_count)


"""Studentni o'chirish"""
# student = session.query(Student).filter(Student.id == 3).delete()
# session.commit()
# student = session.query(Student).filter(Student.id == 2).first()
# session.delete(student)
# session.commit()
"""Studentni yangilash"""

# student = session.query(Student).filter(Student.name == "John").first()
# student.name = "Dilshod"
# session.commit()
# print("Bu dilshod", student.name)


