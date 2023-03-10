import  json



##########  movie ##############
# temp_movie.json file handaling functions 
def dump_movie(data):
    with open("temp_movie.json", "w") as file:
        json.dump(data, file, indent=4)
    return True


def get_movie_json():
    with open("temp_movie.json", 'r') as file:
        store = json.loads(file.read())
    return store


def append_cast_to_movie(movie_name):
    movie_data = get_movie_json()
    cast_data = get_cast_json()
    movie_data[movie_name]["casts"] = { **movie_data[movie_name]["casts"], **cast_data }
    with open("temp_movie.json", 'w') as file:
        json.dump(movie_data, file, indent=4)
    return True





########## cast  ##############
# temp_cast.json file handaling functions 
def dump_cast(data):
    with open("temp_cast.json", 'w') as file:
        json.dump(data, file, indent=4)
    return True

def get_cast_json():
    with open("temp_cast.json", 'r') as file:
        store = json.loads(file.read())
    return store

def append_dialogue_to_cast(name):
    cast_data = get_cast_json()
    dialogue_data = get_dialogue_json()
    cast_data[name]["dialogue"] = { **cast_data[name]["dialogue"], **dialogue_data }
    with open("temp_cast.json", 'w') as file:
        json.dump(cast_data, file, indent=4)
    return True





########### dialogue  ###############
# temp_dialogue.json file handaling functions

def dump_dialogue(data):
    with open("temp_dialogue.json", 'w') as file:
        json.dump(data, file, indent=4)
    return True


def get_dialogue_json():
    with open("temp_dialogue.json", 'r') as file:
        store = json.loads(file.read())
    return store











########### main storage #############
# storage.json file handaling functions

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
