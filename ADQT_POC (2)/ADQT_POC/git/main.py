import streamlit as st
import pandas as pd
from frontend import st_keyup, search, titles, table, cards, suites
from theme import *
import streamlit.components.v1 as comp

# st.set_page_config(
#     page_title="ADQT",
#     page_icon="chart_with_upwards_trend",
#     layout="wide",
# )

def clicked_event():
    return 'clicked'

default_page: str = 'projects'

num = st_keyup('', key='header')

if num == '':
    num = default_page

if num == 'projects':
    col1, col2 = st.columns([2, 6])
    with col1:
        text = search('search')
        table('table')


    with col2:
        titles('title1')
        col1_1, col1_2, col1_3 = st.columns([1, 1, 1])
        with col1_1:
            cards(key='card1')
        with col1_2:
            cards(key='card2')
        with st.container():
            col11, col12 = st.columns([12, 2])
            with col11:
                st.write('Last 10 Executed Runs')
            with col12:
                bt1 = st.button('View all runs →', key=None, help="", on_click=clicked_event)

            df = pd.read_json('./data/sample-json.json').head(10)
            df1 = pd.DataFrame(df)
            df1.columns = ["Suite", "Run Name", "Checkpoint", "Success", "Failed", "DQ Score", "Run Date"]
            cell_hover = {
                "selector": "td:hover",
                "props": [("background-color", "#FFFFE0")]
            }
            index_names = {
                "selector": ".index_name",
                "props": "font-style: italic; color: darkgrey; font-weight:normal;"
            }
            headers = {
                "selector": "th:not(.index_name)",
                "props": "background-color: black; color: white;"
            }
            df1.style.set_table_styles([cell_hover, index_names, headers])

            st.dataframe(df1)
           
elif num == 'suites':
    suites('Suites Page')

