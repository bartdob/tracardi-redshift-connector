import psycopg2
from pydantic.main import BaseModel


class Connection(BaseModel):
    dbname: str
    user: str
    password: str
    host: str
    port: int

    def connect(self):
        return psycopg2.connect(dbname=self.dbname,
                                user=self.user,
                                password=self.password,
                                host=self.host,
                                port=self.port)


class RedShift:
    def __init__(self, connection: Connection):
        self.connection = connection.connect()

    def query(self):
        cur = self.connection.cursor()
        cur.execute(query=self.query)
        rows = cur.fetchall()
        result = [row for row in rows]
        cur.close()
        return result

    def close(self):
        if self.connection:
            self.connection.close()
