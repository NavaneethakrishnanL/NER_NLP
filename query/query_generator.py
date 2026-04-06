def generate_mongo_query(entities):
    """
    Generates a MongoDB query from structured input.

    Supported formats:
    - Single condition
    - Multiple conditions (AND)
    - OR conditions
    - Operators like $in, $gte, $lte, etc.
    """

    if not entities:
        return {}

    # If it's a single condition like {"field": "name", "value": "Vishwa"}
    if "field" in entities and "value" in entities:
        return {entities["field"]: entities["value"]}

    query = {}

    # Handle AND conditions
    if "conditions" in entities:
        and_conditions = []

        for condition in entities["conditions"]:
            field = condition.get("field")
            value = condition.get("value")
            operator = condition.get("operator", "eq")

            if not field:
                continue

            if operator == "eq":
                and_conditions.append({field: value})
            elif operator == "in":
                and_conditions.append({field: {"$in": value}})
            elif operator == "gte":
                and_conditions.append({field: {"$gte": value}})
            elif operator == "lte":
                and_conditions.append({field: {"$lte": value}})
            elif operator == "gt":
                and_conditions.append({field: {"$gt": value}})
            elif operator == "lt":
                and_conditions.append({field: {"$lt": value}})
            elif operator == "ne":
                and_conditions.append({field: {"$ne": value}})

        if and_conditions:
            query["$and"] = and_conditions

    # Handle OR conditions
    if "or_conditions" in entities:
        or_conditions = []

        for condition in entities["or_conditions"]:
            field = condition.get("field")
            value = condition.get("value")

            if field:
                or_conditions.append({field: value})

        if or_conditions:
            query["$or"] = or_conditions

    return query