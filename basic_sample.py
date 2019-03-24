import psycopg2

# Connect to the database.
conn = psycopg2.connect(
    user='root', # show USERS; will show the users of cockorachDB
    password='',
    host='10.142.0.2',
    port=26257,
    database='postgres', # show DATABASE; will show the databases of cockorachDB
    sslmode='disable',
    sslrootcert='/etc/ssl/cert/ca-certificates.crt'
)

# Make each statement commit immediately.
conn.set_session(autocommit=True)

# Open a cursor to perform database operations.
cur = conn.cursor()

# Create an "accounts" table.
cur.execute("CREATE TABLE IF NOT EXISTS newaccounts (id INT PRIMARY KEY, balance INT)")

# Insert two rows into the "accounts" table.
cur.execute("INSERT INTO newaccounts (id, balance) VALUES (1, 1000), (2, 250)")

# Print out the balances.
cur.execute("SELECT id, balance FROM newaccounts")
rows = cur.fetchall()
print('Initial balances:')
for row in rows:
    print([str(cell) for cell in row])

# Close the database connection.
cur.close()
conn.close()