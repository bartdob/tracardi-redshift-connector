from tracardi_redshift_connector.plugin.redshift_connector import redshift_conn


print(redshift_conn(dbname='dev', user='awsuser', password='******', host='3.123.191.145', port='5439',
                    query="SELECT * FROM sales;"))

