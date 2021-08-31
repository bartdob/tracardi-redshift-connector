from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.result import Result
from tracardi_redshift_connector.model.redshift import RedShift, Connection


class RedshiftConnectorAction(ActionRunner):

    def __init__(self, **kwargs):
        self.db = RedShift(connection=Connection(**kwargs))
        if 'query' not in kwargs:
            raise ValueError("Please define query.")

        self.query = kwargs['query']

    async def run(self, payload):
        result = self.db.query(self.query)
        return Result(port="payload", value=result)

    async def close(self):
        self.db.close()


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_redshift_connector.redshift_connector_action',
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
