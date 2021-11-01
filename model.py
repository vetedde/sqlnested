from sqlalchemy import Table, Index, Integer, String, Column, Text, \
    DateTime, Boolean, PrimaryKeyConstraint, \
    UniqueConstraint, ForeignKeyConstraint, \
    SmallInteger, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    books = relationship("Book", back_populates="author")
    films = relationship("Film", back_populates="author")


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="books")

class Film(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="films")