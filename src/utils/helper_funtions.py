import os

import uuid
import plotly.graph_objects as go
from plotly.subplots import make_subplots


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


def dataviz_structure_categorical(column, fig, dataframe, row, col):
    dataframe_new = dataframe[column].value_counts()
    dataframe_new = dataframe_new.rename_axis(column)
    dataframe_new = dataframe_new.reset_index(name='Count')

    fig.append_trace(go.Bar(
        x=dataframe_new[column],
        y=dataframe_new['Count']
    ), row=row, col=col)

def dataviz_structure_numerical_hist(column, fig, dataframe, row, col):
    trace_n = go.Histogram(x=dataframe[column])
    fig.append_trace(trace_n, row, col)
