import psycopg2


def redshift_conn(*args, ** kwargs):
    print("start connection")

    # config = kwargs['config']
    try:
        conn = psycopg2.connect(dbname='dev',
                                host='172.31.4.237', #ipadres
                                port=5439,
                                user='awsuser',
                                password='**********')
        # conn = psycopg2.connect(dbname=config['dbname'],
        #                         host=config['host'],
        #                         port=config['port'],
        #                         user=config['user'],
        #                         password=config['password'])
        print("SUCCESS")
    except Exception as err:
        print("Error:", err)
        conn = None
        print("end conn ")
    return conn
