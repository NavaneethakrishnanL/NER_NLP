from data.sample_data import SUBSCRIBERS


class MockMongoExecutor:

    def run_query(self, query):

        if not query:
            return []

        field = list(query.keys())[0]
        value = query[field]

        results = []

        for record in SUBSCRIBERS:
            if field in record and str(record[field]).lower() == str(value).lower():
                results.append(record)

        return results