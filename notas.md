# Notas

## Crear una base de datos con Postgresql

Suponiendo que el servidor de PostgreSQL esté activo, nos conectamos
con psql:

    $ psql -U postgres --host localhost

Creamos el usuario (Rol) con el que nos conectaremos:

    CREATE ROLE carontepass WITH CREATEDB LOGIN PASSWORD 'carontepass';

Creamos la base de datos con dueño el usuario anterior y le damos
  al mismo los accesos `CREATE`, `CONNECT`, y `TEMPORARY` (`SELECT`, `INSERT`,
  `UPDATE` y otros privilegios ya los tiene por ser el dueño de la base
  de datos):

    CREATE DATABASE carontepass
       WITH ENCODING='UTF8'
       OWNER=carontepass
       CONNECTION LIMIT=-1;
    GRANT ALL PRIVILEGES ON DATABASE carontepass TO carontepass;

Salimos de `psql` con `\q` o `\quit`.

## Uso de SqlAlchemy

Para usar un ORM, se suele empezar describiendo las tablas de la base
de datos que vamos a usar, y luego definiendo nuestras propias clases, una
para cada tabla, y mapearemos las clases con las tablas. En SQLAlchemy podemos
realizar estas dos tareas a la vez, usando un sistema llamado (Declarative)
[http://docs.sqlalchemy.org/en/rel_0_9/orm/extensions/declarative/index.html].
Usando este sistema, creamos las clases incluyendo ciertas directivas que 
describen la tabla del a la que está vincula la clase.

Estas clases se definen en base a una clase que mantiene un catálogo 
de las clases y tablas implicadas. Esta clase base se denomina
**derivate base class**. Lo normal es que nuestra aplicación tenga solo
una instancia de esta clase base, en un módulo de uso común. Para crear
la clase base se llama a la función `declarative_base()`, como en este
ejemplo:

    >>> from sqlalchemy.ext.declarative import declarative_base
    >>> Base = declarative_base()

Ahora que ya tenemos nuestra "base", podemos definir cuantas clases 
derivadas necesitemos, una para cada tabla.

### Crear y usar tablas de una base de datos

La estructura del esquema de una base de datos relacional se representa
internamente en Python usando objetos como `MetaData`, `Table`, y otros:

    >>> from sqlalchemy import MetaData
    >>> from sqlalchemy import Table, Column
    >>> from sqlalchemy import Integer, String

    >>> metadata = MetaData()
    >>> user_table = Table('user', metadata,
    ...                Column('id', Integer, primary_key=True),
    ...                Column('name', String),
    ...                Column('fullname', String)

Los objetos `MetaData` y `Table` se pueden usar para crear una tabla en un
esquema:

    >>> from sqlalchemy import create_engine
    >>> engine = create_engine("sqlite://")
    >>> metadata.create_all(engine)

El método `create_all` tiene la virtud de que antes de intentar crar una tabla,
mira a ver si ya está creada, y en ese caso no hace nada.

El objeto `Table` es el nucleo del sistema de expresiones SQL; este es una
muestra rápida de su uso: 

    >>> print(user_table.select())
    SELECT "user".id, "user".name, "user".fullname 
    FROM "user"

Los tipos de datos de la base de datos se representan con objetos como
`String`, `Integer`, `DateTime`, etc... Estos objetos se pueden especificar
como "class keywords" (es decir, psasndo la clase como argumento) o como
objetos ya instanciados con sus propios argumentos:

    >>> from sqlalchemy import String, Numeric, DateTime, Enum
    >>> fancy_table = Table('fancy', metadata,
    ...                     Column('key', String(50), primary_key=True),
    ...                     Column('timestamp', DateTime),
    ...                     Column('amount', Numeric(10, 2)),
    ...                     Column('type', Enum('a', 'b', 'c'))
    ...                 )
    >>> fancy_table.create(engine)

También podemos especificar índices y *constraints*. La clase `ForeingKey` se
usa para enlazar un campo de clave foranea con la tabla y clave primaria
correspondiente:

    >>> from sqlalchemy import ForeignKey
    >>> addresses_table = Table('address', metadata,
    ...                     Column('id', Integer, primary_key=True),
    ...                     Column('email_address', String(100), nullable=False),
    ...                     Column('user_id', Integer, ForeignKey('user.id'))
    ...                   
    >>> addresses_table.create(engine)


### Reflection

Podemos cargar la definición de una tabla directamente desde la base de datos,
si la tabla ya existe, usando el parámetro `autoload`:

    >>> metadata2 = MetaData()
    >>> user_reflected = Table('user', metadata2, autoload=True, autoload_with=engine)

Si necesitamos más información, tanto de las tablas como de la base de datos en
general, podemos usar el objeto `Inspector`:

    >>> from sqlalchemy import inspect

    >>> inspector = inspect(engine)
    >>> inspector.get_table_names()
    >>> inspector.get_columns('address')
    >>> inspector.get_foreign_keys('address')

Podemos insertar datos en la tabla usando el método `insert`, que genera
automáticamente la sentencia SQL, adaptada al engine que estemos usando::

    >>> insert_stmt = user_table.insert().values(username='ed', fullname='Ed Jones')
    >>> conn = engine.connect()
    >>> result = conn.execute(insert_stmt)

El resultado de ejecutar un insert incluye la clave primaria del último
registro insertado. Si hemos insertado varios registros no es demasiado útil,
pero sí cuando insertamos un único registro:

    >>> result.inserted_primary_key
    [1]

Los métodos `insert` y otros que reflejan comandos de manipulación de datos
(DML) pueden ejecutarse con múltiples parámetros, pasando una lista de
diccionarios con los datos:

    >>> conn.execute(user_table.insert(), [
    ...     {'username': 'jack', 'fullname': 'Jack Burger'},
    ...     {'username': 'wendy', 'fullname': 'Wendy Weathersmith'}
    >>> ])

El método `select` se puede usar para producir cualquier tipo de sentencia
`SELECT`:

    >>> from sqlalchemy import select
    >>> select_stmt = select([user_table.c.username, user_table.c.fullname]).\
    ...             where(user_table.c.username == 'ed')
    >>> result = conn.execute(select_stmt)
    >>> for row in result:
    ...     print(row)

## Uso de Flask-SqlAlchemy

Flask-SqlAlchemy es una extension de Flask que simplifica trabajar con
SqlAlchemy. No es estrictamente necesaria, pero proporciona ciertos
valores por defecto y funciones comunes útiles.

Para usarlo, configuramos la aplicacion Flask con la
variable `SQLALCHEMY_DATABASE_URI` apuntando a la base de datos
que queremos usar (en el formato de *connection string* usado por
SqlAlchemy), y luego instanciamos un objeto de la clase 
`flask.ext.sqlalchemy.SQLAlchemy`, pasándole como parámetro 
la aplicación Flask:

    from flask import Flask
    from flask.ext.sqlalchemy import SQLAlchemy

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db = SQLAlchemy(app)

Una vez creado, el objeto contiene todas las funciones y utilidades de
los módulos `sqlalchemy` y `sqlalchemy.orm`. Además, incluye una clase
Model que es la clase derivada (*declarative base*) que usaremos
para crear nuestros modelos.

