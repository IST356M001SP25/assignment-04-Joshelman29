'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as dp


def display_universal_data_browser():
    """
    Main application function for UniBrow - Universal Data Browser.
    Handles file upload, column selection, filtering, and data display.
    """
    # Application header
    st.title("UniBrow")
    st.caption("The Universal Data Exploration Tool")
    
    # File upload section
    uploaded_data = st.file_uploader(
        "Upload Dataset:", 
        type=["csv", "xlsx", "json"],
        help="Supported formats: CSV, Excel (xlsx), JSON"
    )
    
    if uploaded_data:
        # Process uploaded file
        file_extension = dp.get_file_extension(uploaded_data.name)
        data_frame = dp.load_file(uploaded_data, file_extension)
        available_columns = dp.get_column_names(data_frame)
        
        # Column selection
        selected_columns = st.multiselect(
            "Choose Columns to Display",
            available_columns,
            default=available_columns
        )
        
        # Filtering options
        if st.toggle("Enable Data Filtering"):
            filter_columns = st.columns(3)
            text_columns = dp.get_columns_of_type(data_frame, 'object')
            
            filter_column = filter_columns[0].selectbox(
                "Select Filter Column",
                text_columns
            )
            
            if filter_column:
                unique_values = dp.get_unique_values(data_frame, filter_column)
                selected_value = filter_columns[1].selectbox(
                    "Select Filter Value",
                    unique_values
                )
                filtered_data = data_frame[data_frame[filter_column] == selected_value][selected_columns]
        else:
            filtered_data = data_frame[selected_columns]
        
        # Data display
        st.dataframe(filtered_data)
        st.dataframe(filtered_data.describe())


display_universal_data_browser()