memory_store = {}

def has_schema(schema_id):
    return schema_id in memory_store

def get_from_memory(schema_id):
    return memory_store.get(schema_id)

def save_to_memory(schema_id, insights):
    memory_store[schema_id] = insights
