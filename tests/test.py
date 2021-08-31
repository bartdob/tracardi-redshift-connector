import asyncio

from tracardi_redshift_connector.redshift_connector_action import RedshiftConnectorAction

init = dict(
    dbname='dev',
    user='awsuser',
    password='******',
    host='3.123.191.145',
    port='5439',
    query="SELECT * FROM sales;"
)

payload = {}


async def main():
    plugin = RedshiftConnectorAction(**init)
    result = await plugin.run(payload)
    print(result)


asyncio.run(main())
