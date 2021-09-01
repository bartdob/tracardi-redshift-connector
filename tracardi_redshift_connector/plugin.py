import json
from datetime import datetime, date
from typing import Optional

import asyncpg
from decimal import Decimal
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.result import Result
from tracardi_redshift_connector.model.redshift import Connection


class RedshiftConnectorAction(ActionRunner):

    @staticmethod
    async def build(**kwargs) -> 'RedshiftConnectorAction':
        plugin = RedshiftConnectorAction(**kwargs)
        connection = Connection(**kwargs)
        plugin.db = await connection.connect()

        return plugin

    def __init__(self, **kwargs):
        self.db = None  # type: Optional[asyncpg.connection.Connection]
        if 'query' not in kwargs:
            raise ValueError("Please define query.")

        self.query = kwargs['query']
        self.timeout = kwargs['timeout'] if 'timeout' in kwargs else None

    async def run(self, payload):
        result = await self.db.fetch(self.query, timeout=self.timeout)
        result = [self.to_dict(record) for record in result]
        return Result(port="payload", value={"result": result})

    async def close(self):
        if self.db:
            await self.db.close()

    @staticmethod
    def to_dict(record):

        def json_default(obj):
            """JSON serializer for objects not serializable by default json code"""

            if isinstance(obj, (datetime, date)):
                return obj.isoformat()

            if isinstance(obj, Decimal):
                return float(obj)

            return str(obj)

        j = json.dumps(dict(record), default=json_default)
        return json.loads(j)


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_redshift_connector.plugin',
            className='RedshiftConnectorAction',
            inputs=["payload"],
            outputs=['payload'],
            version='0.1.2',
            license="MIT",
            author="Bartosz Dobrosielski",
            init={
                "host": 'localhost',
                "port": 5439,
                "dbname": None,
                "user": None,
                "password": None,
                "query": None
            }

        ),
        metadata=MetaData(
            name='Redshift connector',
            desc='Connects to redshift and reads data.',
            type='flowNode',
            width=200,
            height=100,
            icon='postgres',
            group=["Connectors"]
        )
    )
