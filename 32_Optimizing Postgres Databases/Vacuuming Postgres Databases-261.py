## 1. Destructive Queries ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()

cur.execute("DELETE FROM homeless_by_coc")

with open("homeless_by_coc.csv","r") as f: 
    
    cur.copy_expert("COPY homeless_by_coc FROM STDIN WITH CSV HEADER",f)
conn.commit()

cur.execute("SELECT COUNT(*) FROM homeless_by_coc")
homeless_rows = int(cur.fetchall()[0][0])




## 3. Counting Dead Rows ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()


cur.execute("""SELECT n_dead_tup FROM pg_stat_all_tables WHERE relname = 'homeless_by_coc'""")
pp.pprint(cur.fetchone()[0])

cur.execute("DELETE FROM homeless_by_coc")
with open('homeless_by_coc.csv') as f:
    cur.copy_expert('COPY homeless_by_coc FROM STDIN WITH CSV HEADER', f)
conn.commit()

cur.execute("""SELECT n_dead_tup FROM pg_stat_all_tables WHERE relname = 'homeless_by_coc'""")
homeless_dead_rows = cur.fetchone()[0]
pp.pprint(homeless_dead_rows)


## 4. Vacuuming Dead Rows ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()

cur.execute("VACUUM homeless_by_coc")
conn.commit()



## 5. Transaction Blocks ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
conn.autocommit = True
cur = conn.cursor()
cur.execute("SELECT n_dead_tup FROM pg_stat_all_tables WHERE relname='homeless_by_coc'")
pp.pprint(cur.fetchall())
pp.pprint(" ")

cur.execute("VACUUM homeless_by_coc")

cur.execute("SELECT n_dead_tup FROM pg_stat_all_tables WHERE relname='homeless_by_coc'")
homeless_dead_rows = int(cur.fetchall()[0][0])
pp.pprint(homeless_dead_rows)

## 6. Updating Statistics ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
conn.autocommit = True
cur = conn.cursor()
cur.execute("EXPLAIN SELECT * FROM homeless_by_coc")
pp.pprint(cur.fetchall())
print(1)
cur.execute("VACUUM ANALYZE homeless_by_coc")
cur.execute("EXPLAIN SELECT * FROM homeless_by_coc")
pp.pprint(cur.fetchall())

## 7. Full Vacuum ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
conn.autocommit = True
cur = conn.cursor()

cur.execute("VACUUM FULL")