import os

import uuid
import plotly.express as px
import plotly.graph_objects as go

import matplotlib.pyplot as plt
import seaborn as sns


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
    
def dataviz_structure_numerical(column, fig, dataframe, row, col):
    fig.append_trace(go.Box(
        y=dataframe[column],
        name=column
    ), row=row, col=col)

def conversion_rate_chart(predictor_var, var_to_predict, dataframe, type='line', order=None):
    # Generate group data, calculate conversion rate (mean) and multiply by 100
    df_group = dataframe.groupby(predictor_var)[var_to_predict].mean().mul(100).rename('conversion_rate').reset_index()

    # Generate charts
    if type=='line': # Useful for continuous ranges
        fig = px.line(df_group, x=predictor_var, y='conversion_rate',
                      title=f'Tasa de conversión para la variable "{predictor_var}"'
                      )
        fig.show()
    elif type=='bar': # Useful if data are divided into ranges or are categorical data
        fig = px.bar(df_group, x=predictor_var, y='conversion_rate',
                     title=f'Tasa de conversión para la variable "{predictor_var}"'
                     )
        fig.show()
    elif type=='scatter':
        fig = px.scatter(df_group, x=predictor_var, y='conversion_rate',
                         title=f'Tasa de conversión para la variable "{predictor_var}"'
                         )
        fig.show()

# Tasa de conversión para dos columnas
def graficar_tc_bivariada(col_list, dataframe, orden=None):
    tc = dataframe.groupby(col_list)['Sales'].mean().to_frame().reset_index()

    # Gráfica
    plt.figure(figsize=(13,7))
    ax = sns.pointplot(x=tc['Sales'], y=tc[col_list[0]], hue=tc[col_list[1]], join=False, order=orden)
    ax.yaxis.grid(True)
    ax.xaxis.grid(True)
    plt.title(f'Tasa de conversión para "{col_list[0]}" y "{col_list[1]}"')
    plt.xlabel('Tasa de conversión (%)')
    plt.xlim((0,1))
  
    # fig = px.scatter(dataframe, x=tc['Sales'], y=tc[col_list[0]], color=tc[col_list[0]],
    #                     title=f'Tasa de conversión para {col_list[0]} y {col_list[1]}',
    #                     # labels={"salary":"Annual Salary (in thousands)"} # customize axis label
    #                     )
    # fig.show()