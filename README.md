# Week 5: Python Script interacting with SQL Database

This is a Python GitHub Template Repository that includes the following contents:
- A .devcontainer configuration for a Python environment
- A Makefile with commands for setup, testing, and linting
- GitHub Actions for CI/CD
- A requirements.txt for project dependencies
- A README.md with setup and usage instructions and an explanation for what the query is doing and the expected results
- A Python script includes the following operations:
  1. Connect to a SQL database
  2. Perform CRUD operations
  3. Write at least two different SQL queries

  
## Prerequisites

- mysql-connector-python

## Report

For this project, I first created my local MySQL Database with the users tables, connected to the database, performed CRUD operations with at least two different SQL queries.    

mysql> SHOW TABLES;  
+--------------------+  
| Tables_in_interact |  
+--------------------+  
| users              |  
+--------------------+  
1 row in set (0.00 sec)  
  
mysql> DESCRIBE users;  
+-------+--------------+------+-----+---------+----------------+  
| Field | Type         | Null | Key | Default | Extra          |  
+-------+--------------+------+-----+---------+----------------+  
| id    | int          | NO   | PRI | NULL    | auto_increment |  
| name  | varchar(255) | NO   |     | NULL    |                |  
| age   | int          | YES  |     | NULL    |                |  
+-------+--------------+------+-----+---------+----------------+  
3 rows in set (0.01 sec)  
  
mysql> TABLE users;  
+----+----------+------+  
| id | name     | age  |  
+----+----------+------+  
|  2 | John Doe |   26 |  
|  4 | Alice    |   20 |  
+----+----------+------+  
2 rows in set (0.00 sec)  
  
With the following operations:   
  
create_table_query = """  
    CREATE TABLE IF NOT EXISTS users (  
        id INT AUTO_INCREMENT PRIMARY KEY,  
        name VARCHAR(255) NOT NULL,  
        age INT  
    );  
    """  
      
create_query1 = """  
    INSERT INTO users (name, age)  
    VALUES ('John Doe', 25);  
    """  
      
create_query2 = """  
    INSERT INTO users (name, age)  
    VALUES ('Milker', 10);  
    """
      
create_query3 = """  
    INSERT INTO users (name, age)  
    VALUES ('Alice', 20);  
    """  
      
query = f"SELECT * FROM {table_name}" 
  
update_query = """  
    UPDATE users  
    SET age = 26  
    WHERE name = 'John Doe';  
    """  
      
delete_query = """  
    DELETE FROM users WHERE name = 'Milker';  
    """  

With the following results:  
  
Successfully connected to the database!  
Query executed successfully!  
Query executed successfully!  
Data in users table: [(1, 'John Doe', 25)]  
Query executed successfully!  
Query executed successfully!  
Connection closed.  
  
Successfully connected to the database!  
Query executed successfully!  
Query executed successfully!  
Query executed successfully!  
Query executed successfully!  
Data in users table: [(2, 'John Doe', 25), (3, 'Milker', 10), (4, 'Alice', 20)]  
Query executed successfully!  
Query executed successfully!  
Connection closed.  

Other different SQL queries:  
SELECT * FROM users WHERE age > 21;  
SELECT age, COUNT(*) as user_count FROM users GROUP BY age;  

With the following result:  
Successfully connected to the database!  
Users older than 21: [(2, 'John Doe', 26)]  
Count of users by age: [(26, 1), (20, 1)]  
Connection closed.  