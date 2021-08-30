from tracardi_redshift_connector.plugin.redshift_connector import redshift_conn
from tracardi_redshift_connector.redshift_connector_action import RedshiftConnectorAction
from tracardi_redshift_connector.redshift_connector_action import register


print(RedshiftConnectorAction(dbname='dev', user='awsuser', password='*****', host='3.123.191.145', port='5439',
                    query="SELECT * FROM sales;"))
