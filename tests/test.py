import asyncio

from tracardi_redshift_connector.plugin import RedshiftConnectorAction

init = dict(
    dbname='dev',
    user='awsuser',
    password='Kaloryfer1',
    host='3.123.191.145',
    port='5439',
    query="SELECT * FROM sales LIMIT 10;"
)

payload = {}


async def main():
    plugin = await RedshiftConnectorAction.build(**init)
    result = await plugin.run(payload)
    print(result)


asyncio.run(main())
