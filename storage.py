import  json


def get_storage():
    with open("storage.json", 'r') as f:
        store = json.loads(f.read())
    return store

def dump_storage(data):
    with open("storage.json", 'r') as f:
        store = json.loads(f.read())
    i = 0
    for i in store:
        pass
    store[i+1] = data

    with open("storage.json", 'w') as f:
        json.dumps(store, f, indent=4)

    return 1
