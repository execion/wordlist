from random import randint
def verifyRepeate(word, table, cursor):
    sql = "SELECT * FROM {} WHERE word=\"{}\";".format(table, word)
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) > 0:
        return True
    else:
        return False

def addWord(word, meaning, table, cursor):
    sql = "INSERT INTO {}(word,meaning) VALUES(\"{}\",\"{}\");".format(table, word, meaning)
    cursor.execute(sql)

def fetchWords(table, cursor):
    sql = "SELECT * FROM {};".format(table)
    cursor.execute(sql)
    return cursor.fetchall()

def question(connection):
    with connection.cursor() as cursor:
        selectTable = input("All or Table: ")
        if selectTable == "all":
            tables = ["adjective", "noun", "adverb", "verb"]
        else:
            tables = selectTable.split(" ")
        AllTables = []
        for table in tables:
            wordsRows = fetchWords(table, cursor)
            AllTables.append(wordsRows)
        adjective = []
        adverb = []
        verb = []
        noun = []
        corrects = 0
        cont = 1

        totalWords = 0
        
        for i in AllTables:
            totalWords += len(i)
        
        while True:
            if cont == totalWords:
                print("\tFinish: {} / {}".format(corrects, totalWords))
                break
            randomTables = randint(0,len(tables)-1) # Elige una Tabla
            randomRows = randint(0, len(AllTables[randomTables])-1) # Elige un indice de la tabla elegida
            if randomTables == 0:
                if randomRows in adjective:
                    continue
                else:
                    adjective.append(randomRows)
            elif randomTables == 1:
                if randomRows in adverb:
                    continue
                else:
                    adverb.append(randomRows)
            elif randomTables == 2:
                if randomRows in verb:
                    continue
                else:
                    verb.append(randomRows)
            elif randomTables == 3:
                if randomRows in noun:
                    continue
                else:
                    noun.append(randomRows)
            
            listMeaning = AllTables[randomTables][randomRows]["meaning"].split(", ")
            print("\n\tTable: {}".format(tables[randomTables].capitalize()))
            question = input("{} - What does {} mean?: ".format(cont, AllTables[randomTables][randomRows]["word"].upper()))
            if question == "-quit":
                print("\tTotal: {} / {}".format(corrects, totalWords))
                break
            elif question in listMeaning:
                print("\tCorrect")
                corrects += 1
            else:
                print("Incorrect")
                print(AllTables[randomTables][randomRows]["meaning"])
            
            cont += 1

def addWordsInTable(connection):
    continueLoop = True
    table = input("Table: ")
    while continueLoop:
        print("\nTable: {}".format(table.capitalize()))
        with connection.cursor() as cursor:
            word = input("Insert your word: ")
            if verifyRepeate(word, table, cursor) == True:
                print("The word is repeat")
                continue
            elif (word == ""):
                continue
            elif (word == "-quit"):
                break
            meaning = input("Insert your meaning: ")
            if meaning == "-quit":
                break
            if meaning == "":
                continue
            addWord(word, meaning, table, cursor)      
        connection.commit()