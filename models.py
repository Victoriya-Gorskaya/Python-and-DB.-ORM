import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "Publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=60), unique=True)
    
    def __str__(self):
        return f'{self.name}'
    
    
class Book(Base):
    __tablename__ = "Book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("Publisher.id"), nullable=False)
    
    publishers = relationship(Publisher, backref="books")
     
    def __str__(self):
        return f'{self.title}'
    

class Shop(Base):
    __tablename__ = "Shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)
    
    def __str__(self):
        return f'{self.name}'
    

class Stock(Base):
    __tablename__ = "Stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("Book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("Shop.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    
    books = relationship(Book, backref="stocks")
    shops = relationship(Shop, backref="stocks")
    
    def __str__(self):
        return f'{self.books} | {self.shops}'
    
class Sale(Base):
    __tablename__ = "Sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, nullable=False)    
    date_sale = sq.Column(sq.String(length=40), unique=True)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("Stock.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    
    stocks = relationship(Stock, backref="sales")
    
    def __str__(self):
        return f'{self.stocks} | {self.price} | {self.date_sale}'
    

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)