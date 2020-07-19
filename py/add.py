from database import *
from functionality import *

try:
    addWordsInTable(connection)
finally:
    connection.close()