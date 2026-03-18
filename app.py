import sys
import os

# ✅ Fix import issues
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.text_preprocessor import preprocess_text
from ner.entity_extractor import extract_entities
from query.query_generator import generate_mongo_query
from database.mock_query_executor import MockMongoExecutor


def main():

    executor = MockMongoExecutor()

    while True:

        user_input = input("\nEnter query (or 'exit'): ")

        if user_input.lower() == "exit":
            break

        text = preprocess_text(user_input)

        entities = extract_entities(text)
        print("\nExtracted Entities:", entities)

        query = generate_mongo_query(entities)
        print("Generated Query:", query)

        results = executor.run_query(query)

        print("\nResults:")

        if results:
            for r in results:
                print(r)
        else:
            print("No matching records found")


if __name__ == "__main__":
    main()