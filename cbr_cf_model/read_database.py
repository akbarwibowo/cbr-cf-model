import mysql.connector as sql
import json

connector = sql.connect(
    host="localhost",
    user="root",
    password="",
    database="tbc_database"
)

cursor = connector.cursor()


def indications_table():
    cursor.execute("SELECT indication_code FROM indications")
    indication_code = cursor.fetchall()
    cursor.execute("SELECT indication_name FROM indications")
    indication_name = cursor.fetchall()

    indications_map = {}
    for code, name in zip(indication_code, indication_name):
        indications_map[code[0]] = name[0]

    return indications_map, list(indications_map.keys())


def indications_list_table():
    cursor.execute("SELECT indication_code, knowledge_id FROM indications_list")
    query_list = cursor.fetchall()

    knowledge_id = [ids[1] for ids in query_list]
    indication_list_code = [code[0] for code in query_list]

    indications_list_map = {}
    temp_list = []
    for index in range(len(knowledge_id)-1):
        if knowledge_id[index] == knowledge_id[index+1]:
            temp_list.append(indication_list_code[index])
        else:
            temp_list.append(indication_list_code[index])
            indications_list_map[knowledge_id[index]] = temp_list
            temp_list = []

    return indications_list_map


def knowledge_table():
    cursor.execute("SELECT knowledge_id, disease, solution FROM knowledge_data")
    knowledge_list = cursor.fetchall()

    knowledge_map = {}
    for knowledge in knowledge_list:
        knowledge_map[knowledge[0]] = {"disease": knowledge[1], "solution": knowledge[2]}

    return knowledge_map


def create_dataframe():
    indication_map, indication_codes = indications_table()
    indications_list_map = indications_list_table()
    knowledge_data = knowledge_table()

    new_indications_list_map = {}
    temp_arr = []
    for key, values in indications_list_map.items():
        for item in indication_codes:
            if item in values:
                temp_arr.append(1)
            else:
                temp_arr.append(0)
        new_indications_list_map[key] = {
            "matrix": temp_arr,
            "disease": knowledge_data[key]["disease"],
            "solution": knowledge_data[key]["solution"]
        }
        temp_arr = []

    return new_indications_list_map


create_dataframe()
