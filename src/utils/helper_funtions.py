import os

import uuid


# Get PATH folder from previous directorys
def get_path(prev_folders:int=0):
    for i in range(prev_folders-1): os.chdir('../')  # Change to previous folder
    PATH = os.path.dirname(os.getcwd()) + '/'
    PATH = PATH.replace('\\\\', '/')
    return PATH

# Generate a UUID random or based at id
def uuid_generator(id):
    namespace = uuid.NAMESPACE_URL
    id = str(id)
    uuid_from_name = uuid.uuid5(namespace, id)
    return uuid_from_name
