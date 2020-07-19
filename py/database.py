import pymysql.cursors

connection = pymysql.connect(
    host='localhost', 
    user='execion', 
    password='mu1565', 
    db='english', 
    charset='utf8mb4', 
    cursorclass=pymysql.cursors.DictCursor
)