from st_aggrid import AgGrid, GridUpdateMode, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd


def app():
    df = pd.read_json('../data/sample-json.json')
    gd = GridOptionsBuilder.from_dataframe(df)
    gd.configure_column("name", header_name='Suite')
    gd.configure_column("language", header_name='Run Name')
    gd.configure_column("id", header_name='Checkpoint')
    gd.configure_column("bio", header_name='Success')
    gd.configure_column("version", header_name='Failed')
    gd.configure_column("dqscrore", header_name='DQ Score')
    gd.configure_column("rundate", header_name='Rundate')
    gd.configure_pagination(enabled=True, paginationAutoPageSize=False, paginationPageSize=5)
    gd.configure_default_column(editable=True, groupable=True)

    custom_css = {
        ".ag-row-hover": {"background-color": "red !important"},
        ".ag-header": {"background-color": "#e6ecf3 !important", "font-family": "roboto,sans-serif;",
                       "font-size": ".75rem;"}
    }

    gd.configure_selection(selection_mode='single', use_checkbox=True)
    gridoptions: dict = gd.build()
    # grid_table = AgGrid(df, gridOptions= gridoptions)

    grid_table = AgGrid(df, custom_css=custom_css, gridOptions=gridoptions,
                        update_mode=GridUpdateMode.SELECTION_CHANGED,
                        # height=700,
                        width='100%',
                        allow_unsafe_jscode=False,
                        enable_enterprise_modules=True,
                        theme='balham')
    #
    sel_row = grid_table["selected_rows"]

