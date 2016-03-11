from database.mysql import MySQLDatabase

my_db_connection = MySQLDatabase('employees',
                                 'root',
                                 'saga6beer')

my_tables = my_db_connection.get_available_tables()


print my_tables

kwrgs = {'where': 'emp_no-2'}

results = my_db_connection.select('employees', columns=['first_name', 'emp_no'], named_tuples=True, **kwrgs)

print results




# cursor.execute("SELECT * FROM employees")

# db.commit()
#
# results = cursor.fetchone()
#
# cursor.close()
#
# db.close
#
# print results





