import json
from read_database import CreateMatrix
from sklearn.metrics.pairwise import cosine_similarity

matrix = CreateMatrix("sql12.freesqldatabase.com", "sql12714474", "63c4EvNXTs", "sql12714474")


def run_prediction(user_input: dict) -> json:
    """
    This function is responsible for running the prediction process.

    :param user_input: json object with key "indications" and value as a list of strings
    :return: json object with keys "knowledge_id", "disease", "solution", "indications", "indications_code"
    """

    base_matrix = matrix.create_matrix()

    indications_map, indication_list = matrix.indications_table()
    input_matrix = []
    input_indications_name = []

    for item in indication_list:
        if item in user_input["indications"]:
            input_matrix.append(1)
            input_indications_name.append(indications_map[item])
        else:
            input_matrix.append(0)

    temp_highest_score = 0
    temp_knowledge_id = 0
    for key, value in base_matrix.items():
        cosine_score = cosine_similarity([input_matrix], [value['matrix']])
        if cosine_score > temp_highest_score:
            temp_highest_score = cosine_score
            temp_knowledge_id = key

    return_json = {
        "knowledge_id": temp_knowledge_id,
        "disease": base_matrix[temp_knowledge_id]['disease'],
        "solution": base_matrix[temp_knowledge_id]['solution'],
        "indications": input_indications_name,
        "indications_code": user_input["indications"]
    }

    return return_json

