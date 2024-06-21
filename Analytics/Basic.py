# Pandas :
#       import pandas as pd
#       - df = pd.read_csv('<file>')
#       - df.head() : top 5 , df.head(20)
#       - df.columns : list of column names
#       - df.column1 : print all values of column1
#       - df : all rows and columns
#       - df1 = df[['col3', 'col4', 'col6']] : selected columns
#       - display(df.iloc[6]) : specific row of data
#       - df.rank() : rank for each row
#       - df.info : info about all columns and table
#       - df.dtypes : info about each column type
#       - df.describe() : maths related func
#       - df['column'].mean() : maths functions , can use for others as well
#       - df.shape : number of rows and columns
#       - df.size : number of values
#       - df.sample(15)

# import webbrowser : package for using website with python
#       - webbrowser.open(website) : opening website


# import matplotlib.pyplot as plt
#       - plt.bar(df1['month'], df1['sales'])
#       - plt.xlabel() , plt.ylabel() , plt.show()



# psycopg2 : for db and python connection
import psycopg2 as pg2

conn = pg2.connect(database='Airlines', user='postgres', password='secret', port=5432)
cur = conn.cursor()
cur.execute('SELECT * FROM ticket_flights')
cur.fetchall()   # fetching all
print(cur.fetchmany(20))   # fetching only few



