from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow_sqlalchemy.fields import Nested
from model import Author, Book, Film
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        include_fk = True
        load_instance = True


class FilmSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Film
        include_fk = True
        load_instance = True


class AuthorSchema(SQLAlchemyAutoSchema):
    books = Nested(BookSchema, many=True)
    films = Nested(FilmSchema, many=True)

    class Meta:
        model = Author
        include_relationships = True
        load_instance = True
