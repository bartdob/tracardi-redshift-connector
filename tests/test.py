from tracardi_redshift_connector.plugin.redshift_connector import redshift_conn
import pprint


print(redshift_conn(dbname='dev', user='awsuser', password='xxx', host='3.123.191.145', port='5439'))
