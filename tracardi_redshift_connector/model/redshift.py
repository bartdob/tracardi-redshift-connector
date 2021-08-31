import asyncpg
from pydantic.main import BaseModel


class Connection(BaseModel):
    dbname: str
    user: str
    password: str
    host: str
    port: int

    async def connect(self) -> asyncpg.connection.Connection:
        return await asyncpg.connect(database=self.dbname,
                                     user=self.user,
                                     password=self.password,
                                     host=self.host,
                                     port=self.port)
