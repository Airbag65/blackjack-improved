import sqlite3
con = sqlite3.connect("database/database.db")
cur = con.cursor()
sql_query = ""
exec_sql = ""


sql_file = open("database/migrate.sql", "r")
sql_data = sql_file.readlines()
sql_file.close()
for line in sql_data:
    new_line = line.replace("\n", "")
    if new_line == "":
        continue
    sql_query += new_line
    if sql_query.endswith(";"):
        exec_sql = exec_sql.replace("    ", "")
        print(exec_sql)
        cur.execute(exec_sql)
        sql_query = ""
        print("END of quary line")
        con.commit()
    else:
        continue
con.commit()
cur.close()