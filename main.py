import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = "postgresql://postgres:Ntktajif@localhost:5432/HW6"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

# сессия
Session = sessionmaker(bind=engine)
session = Session()

# создание объектов
P1 = Publisher(name = 'Александр Пушкин')
P2 = Publisher(name = 'Лев Толстой')
P3 = Publisher(name = 'Джейн Остен')
P4 = Publisher(name = 'Виктор Гюго')

session.add_all([P1, P2, P3, P4])
session.commit()

b1_1 = Book(title = 'Капитансткая дочка', publishers = P1)
b1_2 = Book(title = 'Евгений Онегин', publishers = P1)
b1_3 = Book(title = 'Руслан и Людмила', publishers = P1)

b2_1 = Book(title = 'Война и Мир', publishers = P2)
b2_2 = Book(title = 'Анна Каренина', publishers = P2)
b2_3 = Book(title = 'Кавказский пленник', publishers = P2)

b3_1 = Book(title = 'Гордость и Предубеждение', publishers = P3)
b3_2 = Book(title = 'Чувство и чувствительность', publishers = P3)
b3_3 = Book(title = 'Нортенгерское аббатство', publishers = P3)

b4_1 = Book(title = 'Отверженные', publishers = P4)
b4_2 = Book(title = 'Человек, который смеется', publishers = P4)
b4_3 = Book(title = 'Собор Парижской Богоматери', publishers = P4)

session.add_all([b1_1, b1_2, b1_3, b2_1, b2_2, b2_3, b3_1, b3_2, b3_3, b4_1, b4_2, b4_3])
session.commit()

sh1 = Shop(name = 'Читай-город')
sh2 = Shop(name = 'Читайна')
sh3 = Shop(name = 'Лабиринт')
sh4 = Shop(name = 'Book24')
sh5 = Shop(name = 'Дирижабль')
sh6 = Shop(name = 'Дом книги')

session.add_all([sh1, sh2, sh3, sh4, sh5, sh6])
session.commit()

st1 = Stock(books = b1_1, shops = sh1, count = 5)
st2 = Stock(books = b1_2, shops = sh2, count = 6)
st3 = Stock(books = b1_3, shops = sh3, count = 7)
st4 = Stock(books = b2_1, shops = sh4, count = 8)
st5 = Stock(books = b2_2, shops = sh5, count = 9)
st6 = Stock(books = b2_3, shops = sh6, count = 10)
st7 = Stock(books = b3_1, shops = sh1, count = 9)
st8 = Stock(books = b3_2, shops = sh2, count = 8)
st9 = Stock(books = b3_3, shops = sh3, count = 7)
st10 = Stock(books = b4_1, shops = sh4, count = 6)
st11 = Stock(books = b4_2, shops = sh5, count = 5)
st12 = Stock(books = b4_3, shops = sh6, count = 4)

session.add_all([st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11, st12])
session.commit()

sl1 = Sale(price = 250, date_sale = '09/12/2022', stocks = st1, count = 2)
sl2 = Sale(price = 350, date_sale = '01/12/2022', stocks = st2, count = 3)
sl3 = Sale(price = 450, date_sale = '02/12/2022', stocks = st3, count = 4)
sl4 = Sale(price = 550, date_sale = '03/12/2022', stocks = st4, count = 5)
sl5 = Sale(price = 650, date_sale = '04/12/2022', stocks = st5, count = 6)
sl6 = Sale(price = 200, date_sale = '05/12/2022', stocks = st6, count = 5)
sl7 = Sale(price = 300, date_sale = '06/12/2022', stocks = st7, count = 4)
sl8 = Sale(price = 400, date_sale = '07/12/2022', stocks = st8, count = 3)
sl9 = Sale(price = 500, date_sale = '08/12/2022', stocks = st9, count = 2)
sl10 = Sale(price = 600, date_sale = '10/12/2022', stocks = st10, count = 1)
sl11 = Sale(price = 250, date_sale = '11/12/2022', stocks = st11, count = 2)
sl12 = Sale(price = 270, date_sale = '12/12/2022', stocks = st12, count = 3)

session.add_all([sl1, sl2, sl3, sl4, sl5, sl6, sl7, sl8, sl9, sl10, sl11, sl12])
session.commit()


author_name = input("Введите автора книги: ")
n = session.query(Publisher).filter(Publisher.name == author_name)
for author in n.all():
    for book in session.query(Book).filter(Book.id_publisher == author.id):
        for stock in session.query(Stock).filter(Stock.id_book == book.id):
            for sale in session.query(Sale).filter(Sale.id_stock == stock.id):
                print(sale)
            

session.close()