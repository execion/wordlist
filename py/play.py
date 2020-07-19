from database import *
from functionality import *

try:
    question(connection)
finally:
    connection.close()