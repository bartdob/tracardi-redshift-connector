from typing import Optional

from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.result import Result

from tracardi_redshift_connector.plugin.redshift_connector import redshift_conn


class RedshiftConnectorAction(ActionRunner):

    def __init__(self, **kwargs):
        self.database = kwargs['dbname'] if 'dbname' in kwargs else None
        self.database = kwargs['user'] if 'database' in kwargs else None
        self.database = kwargs['password'] if 'database' in kwargs else None
        self.database = kwargs['port'] if 'port' in kwargs else '5439'

    async def run(self, query):
        result = await (redshift_conn(), query)
        return Result(port="payload", value=result)


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_redshift_connector',
            className='RedshiftConnectorAction',
            inputs=["query"],
            outputs=['payload'],
            version='0.1.4',
            license="MIT",
            author="Bartosz Dobrosielski",
            init={
                "source": {
                    "id": None,
                },
                "redshift": {
                    "database": None,
                    "host": None,
                    "user": None,
                    "password": None,
                    "collection": None
                }
            }

        ),
        metadata=MetaData(
            name='Redshift connector',
            desc='Connects to redshift and reads data.',
            type='flowNode',
            width=200,
            height=100,
            icon='redshift',
            group=["Connectors"]
        )
    )