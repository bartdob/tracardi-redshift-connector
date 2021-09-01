import os

import asyncio
from dotenv import load_dotenv

from tracardi_redshift_connector.plugin import RedshiftConnectorAction

load_dotenv()

init = dict(
    dbname='dev',
    user=os.environ['LOGIN'],
    password=os.environ['PASS'],
    host=os.environ['IP'],
    port='5439',
    query="SELECT * FROM sales LIMIT 10;"
)

payload = {}


async def main():
    plugin = await RedshiftConnectorAction.build(**init)
    result = await plugin.run(payload)
    print(result)


asyncio.run(main())
