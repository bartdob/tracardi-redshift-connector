import psycopg2
import pprint


def redshift_conn(*args, **kwargs):
    # print("start connection")
    # print(kwargs)

    try:
        conn = psycopg2.connect(dbname=kwargs['dbname'],
                                user=kwargs['user'],
                                password=kwargs['password'],
                                host=kwargs['host'],
                                port=kwargs['port'])

        print("SUCCESS")
        cur = conn.cursor()
        # cur.execute("SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';")
        cur.execute(query=kwargs['query'])
        rows = cur.fetchall()
        for row in rows:
            print (row)
        cur.close()
        conn.close()
        # print("connection close")

    except Exception as err:
        # print("Error:", err)
        conn = None
        print("end conn ")
    return conn


# def select(*args, **kwargs):
#     cur = kwargs['cur']
#
#     try:
#         cur.execute("SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';")
#     except Exception as err:
#             print (err.code,err)
#
#
#     rows = cur.fetchall()
#     for row in rows:
#         print (row)
#
#
# cursor = conn.cursor()
# print ('start select')
# select(cur=cursor)
# print ('finish')
#
# cursor.close()
# for n in conn.notices():
#     pprint(n)
# conn.close()
