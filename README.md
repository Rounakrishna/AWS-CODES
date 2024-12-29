import pymysql
# RDS Credentials
host = "#"
port = 3306
user = "admin"
password = "#"
database = "#"

try:
    # Establish connection
    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    print("Connection to RDS successful!")

    # Test query
    with connection.cursor() as cursor:
        cursor.execute("""
        INSERT INTO Employee (emp_id, emp_name, emp_salary) 
        VALUES 
        (1, 'John Doe', 50000.00), 
        (2, 'Jane Smith', 60000.00),
        (3, 'Michael Johnson', 55000.00), 
        (4, 'Emily Davis', 70000.00),
        (5, 'David Brown', 75000.00), 
        (6, 'Sarah Wilson', 68000.00), 
        (7, 'James Taylor', 72000.00),
        (8, 'Patricia Moore', 67000.00), 
        (9, 'Robert Lee', 63000.00), 
        (10, 'Linda Harris', 59000.00);
        """)
        connection.commit()  # Commit the transaction
        print("Data inserted successfully!")

except Exception as e:
    import traceback
    print(f"Error: {e}")
    traceback.print_exc()

finally:
    if 'connection' in locals() and connection.open:
        connection.close()
        print("Connection closed.")
sudo apt update
sudo apt install mysql-client -y

 mysql -h database-1.cvwkgkmiczsf.us-east-1.rds.amazonaws.com -P 3306 -u admin -p
