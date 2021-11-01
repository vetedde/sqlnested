from sqlalchemy import insert, create_engine
from sqlalchemy.orm import sessionmaker

from model import Author, Book, Base
from schema import AuthorSchema, BookSchema

engine = create_engine('sqlite:///db.db')
#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

conn = engine.connect()

full_data = {
    "first_name": "Joan",
    "last_name": "Rowling",
    "books": [{"title": "Harry Potter"}],
    "films": [{"title": "Fantastic Beasts"}],
}
data_without_book = {
    "first_name": "Tim",
    "last_name": "Burton",
    "films": [{"title": "Big Fish"}],
}

Session = sessionmaker(engine)
author_schema = AuthorSchema()
with Session() as session:

    load_data = author_schema.load(data_without_book, session=session)

    session.add(load_data)
    session.commit()