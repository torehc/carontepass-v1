 The structure of a relational schema is represented in Python    |
| using MetaData, Table, and other objects.                        |
+------------------------------------------------------ (1 / 20) --+

>>> from sqlalchemy import MetaData
>>> from sqlalchemy import Table, Column
>>> from sqlalchemy import Integer, String

>>> metadata = MetaData()
>>> user_table = Table('user', metadata,
...                Column('id', Integer, primary_key=True),
...                Column('name', String),
...                Column('fullname', String)


+------------------------------------------------------------------+
| Table and MetaData objects can be used to generate a schema      |
| in a database.                                                   |
+------------------------------------------------------ (8 / 20) --+

>>> from sqlalchemy import create_engine
>>> engine = create_engine("sqlite://")
>>> metadata.create_all(engine)

------------------------------------------------------------------+
| The Table object is at the core of the SQL expression            |
| system - this is a quick preview of that.     


>>> print(user_table.select())
SELECT "user".id, "user".name, "user".fullname 
FROM "user"

+------------------------------------------------------------------+
| Types are represented using objects such as String, Integer,     |
| DateTime.  These objects can be specified as "class keywords",   |
| or can be instantiated with arguments.                           |
+------------------------------------------------------ (9 / 20) --+

>>> from sqlalchemy import String, Numeric, DateTime, Enum
>>> fancy_table = Table('fancy', metadata,
...                     Column('key', String(50), primary_key=True),
...                     Column('timestamp', DateTime),
...                     Column('amount', Numeric(10, 2)),
...                     Column('type', Enum('a', 'b', 'c'))
...                 )
>>> fancy_table.create(engine)

+------------------------------------------------------------------+
| table metadata also allows for constraints and indexes.          |
| ForeignKey is used to link one column to a remote primary        |
| key.                                                             |
+----------------------------------------------------- (10 / 20) --+

>>> from sqlalchemy import ForeignKey
>>> addresses_table = Table('address', metadata,
...                     Column('id', Integer, primary_key=True),
...                     Column('email_address', String(100), nullable=False),
...                     Column('user_id', Integer, ForeignKey('user.id'))
...                   
>>> addresses_table.create(engine)

+------------------------------------------------------------------+
| *** Reflection ***                                               |
+------------------------------------------------------------------+
| 'reflection' refers to loading Table objects based on            |
| reading from an existing database.                               |
+----------------------------------------------------- (14 / 20) --+

>>> metadata2 = MetaData()
>>> user_reflected = Table('user', metadata2, autoload=True, autoload_with=engine)

)+---------------------------------------------------------------------+
| Information about a database at a more specific level is available  |
| using the Inspector object.                                         |
+-------------------------------------------------------- (16 / 20) --+

>>> from sqlalchemy import inspect

>>> inspector = inspect(engine)
>>> inspector.get_table_names()
>>> inspector.get_columns('address')
>>> inspector.get_foreign_keys('address')




+------------------------------------------------------------------+
| we can insert data using the insert() construct                  |
+----------------------------------------------------- (19 / 46) --+

>>> insert_stmt = user_table.insert().values(username='ed', fullname='Ed Jones')
>>> conn = engine.connect()
>>> result = conn.execute(insert_stmt)

+------------------------------------------------------------------+
| executing an insert() gives us the "last inserted id"            |
+----------------------------------------------------- (20 / 46) --+

>>> result.inserted_primary_key
[1]

+------------------------------------------------------------------+
| insert() and other DML can run multiple parameters at once.      |
+----------------------------------------------------- (21 / 46) --+

>>> conn.execute(user_table.insert(), [
...     {'username': 'jack', 'fullname': 'Jack Burger'},
...     {'username': 'wendy', 'fullname': 'Wendy Weathersmith'}
>>> ])

+------------------------------------------------------------------+
| select() is used to produce any SELECT statement.                |
+----------------------------------------------------- (22 / 46) --+

>>> from sqlalchemy import select
>>> select_stmt = select([user_table.c.username, user_table.c.fullname]).\
...             where(user_table.c.username == 'ed')
>>> result = conn.execute(select_stmt)
>>> for row in result:
...     print(row)
