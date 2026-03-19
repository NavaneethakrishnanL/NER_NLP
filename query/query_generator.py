#query genearator.py
def generate_mongo_query(entities):

    if not entities:
        return None

    return {
        entities["field"]: entities["value"]
    }