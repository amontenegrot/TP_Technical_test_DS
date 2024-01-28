import os

# Get PATH folder from previous directorys
def get_path(prev_folders:int=0):
    for i in range(prev_folders-1): os.chdir('../')  # Change to previous folder
    PATH = os.path.dirname(os.getcwd()) + '/'
    PATH = PATH.replace('\\\\', '/')
    return PATH