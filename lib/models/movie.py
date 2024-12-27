import sqlite3

CONN = sqlite3.connect("filmdatabase.db")
CURSOR = CONN.cursor()


class Movie:
    all = []

    def __init__(self, title, star_id, director_id, box_office, genre, id=None):
        self.title = title
        self.star_id = star_id
        self.director_id = director_id
        self.box_office = box_office
        self.genre = genre
        self.id = id
        self.__class__.all.append(self)

    @property
    def star_id(self):
        return self._star_id

    @star_id.setter
    def star_id(self, value):
        if isinstance(value, int):
            self._star_id = value
        else:
            raise ValueError("Id must be an integer.")

    @property
    def director_id(self):
        return self._director_id

    @director_id.setter
    def director_id(self, value):
        if isinstance(value, int):
            self._director_id = value
        else:
            raise ValueError("Id must be an integer.")

    @property
    def box_office(self):
        return self._box_office

    @box_office.setter
    def box_office(self, value):
        if isinstance(value, float):
            self._box_office = value
        else:
            raise ValueError("Box office must be floating point decimal.")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS movies
            (id INTEGER PRIMARY KEY,
            title TEXT,
            star_id INTEGER,
            director_id INTEGER,
            box_office FLOAT,
            genre TEXT);

        """
        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS movies;

        """
        CURSOR.execute(sql)

    @classmethod
    def instance_from_db(cls, row):
        movie = cls(
            id=row[0],
            title=row[1],
            star_id=row[2],
            director_id=row[3],
            box_office=row[4],
            genre=row[5],
        )
        return movie

    @classmethod
    def get_all_movies(cls):
        sql = "SELECT * FROM movies;"
        return [cls.instance_from_db(row) for row in CURSOR.execute(sql).fetchall()]

    def save(self):
        sql = """
            INSERT INTO movies (title, star_id, director_id, box_office, genre)
            VALUES (?, ?, ?, ?, ?);
        """
        CURSOR.execute(
            sql,
            (self.title, self.star_id, self.director_id, self.box_office, self.genre),
        )
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, title, star_id, director_id, box_office, genre):
        movie = cls(title, star_id, director_id, box_office, genre)
        movie.save()
        return movie
