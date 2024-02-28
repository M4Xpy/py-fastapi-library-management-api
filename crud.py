from sqlalchemy.orm import Session

import models
import schemas


# Create Author
def create_author(db: Session, author_create: schemas.AuthorCreate):
    db_author = models.DBAuthor(**author_create.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


# Get Author by ID
def get_author(db: Session, author_id: int):
    return db.query(models.DBAuthor).filter(models.DBAuthor.id == author_id).first()


# Get all Authors
def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.DBAuthor).offset(skip).limit(limit).all()


# Update Author
def update_author(db: Session, author_id: int, author_update: schemas.AuthorCreate):
    db_author = get_author(db, author_id)
    for key, value in author_update.dict().items():
        setattr(db_author, key, value)
    db.commit()
    db.refresh(db_author)
    return db_author


# Delete Author
def delete_author(db: Session, author_id: int):
    db_author = get_author(db, author_id)
    db.delete(db_author)
    db.commit()
    return db_author


# Create Book
def create_book(db: Session, book_create: schemas.BookCreate):
    db_book = models.DBBook(**book_create.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# Get Book by ID
def get_book(db: Session, book_id: int):
    return db.query(models.DBBook).filter(models.DBBook.id == book_id).first()


# Get all Books
def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.DBBook).offset(skip).limit(limit).all()


# Update Book
def update_book(db: Session, book_id: int, book_update: schemas.BookCreate):
    db_book = get_book(db, book_id)
    for key, value in book_update.dict().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book


# Delete Book
def delete_book(db: Session, book_id: int):
    db_book = get_book(db, book_id)
    db.delete(db_book)
    db.commit()
    return db_book
