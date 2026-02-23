import sqlite3
import pandas as pd

# connect to database
conn = sqlite3.connect("C:\SQLite\internship.db")

# write join query
query = """
SELECT interns.intern_name,
       interns.track,
       mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track;
"""

# load into pandas dataframe
df = pd.read_sql_query(query, conn)

# display result
print(df)

# close connection
conn.close()