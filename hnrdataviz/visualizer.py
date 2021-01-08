import pandas as pd
import matplotlib.pyplot as plt
import json
import plotly.express as px

def visualizer(ppl_dct):
    '''
    {
        p1: [{es1}, {es2}, {es3}],
        p2: [{es2}, {es2}, {es3}],
        ...
    }
    '''
    persons = []
    persons_dfs = []
    for person, emos_list in ppl_dct.items():
        # assuming the above format, can easily convert to df
        # each person has a dataframe
        # cols - each emotion
        # rows - time period
        persons.append(person)
        person_df = pd.DataFrame(emos_list)
        persons_dfs.append(person_df)
    
    emotions = ['anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise']
    columns_id = ['time', 'anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise']


    list_htmls = []
    for person, df in zip(persons, persons_dfs):
        df.rename_axis('time')
        barchart = px.bar(
            df,
            x = 'time',
            y = emotions,
            title= person + 's emotions over time',
        )
        # barchart.write_image('test.png')
        bar_html = barchart.to_html(full_html = False)
        list_htmls.append(bar_html)
        # barchart.write_json(f'{person}_emotions.json')
    return list_htmls
    
    # for person in persons:
    #     filename = f'{person}_emotions.json'
    #     with open(filename, 'r') as fo:
    #         j = json.load(fo)
    #         list_of_jsons.append(j)
    

    




    