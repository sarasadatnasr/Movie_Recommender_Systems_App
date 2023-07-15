import streamlit as st
import pandas as pd
import ast
import re

# Set page configuration
st.set_page_config(
    page_title="Netflix Search",
    page_icon=":tv:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define CSS styles for the app
CSS = """
body {
    background-image: url("https://cdn.mos.cms.futurecdn.net/rDJegQJaCyGaYysj2g5XWY.jpg");
    background-size: cover;
    background-color: #141414;
    background-position: center center;
    background-repeat: no-repeat;
    color: #ffffff;
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

.container {
    padding:10px;
}

h1 {
    color: #ffffff;
    text-align: center;
    font-size: 48px;
    margin-top: 0;
    margin-bottom: 30px;
}

.search-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 30px;
}

.search-container .input-field {
    width: 200px;
}

.search-container .input-field input[type="text"] {
    width: 60%;
    padding: 28px;
    font-size: 14px;
    border-radius: 5px;
    border: none;
}

.search-container .input-field select {
    width: 60%;
    padding: 8px;
    font-size: 14px;
    border-radius: 5px;
    border: none;
}

.search-container .search-button {
    margin-top: 10px;
    background-color: red;
    color: red;
    padding: 48px 16px;
    font-size: 14px;
    border: none;
    border-radius: 5px;
}

.results-container {
    display: flex;
    flex-wrap: wrap;
}

.result-card {
    background-color: rgba(0, 0, 0, 0.7);
    color: #ffffff;
    border-radius: 5px;
    padding: 10px;
    margin: 10px;
    width: 200px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
}

.result-card img {
    width: 10%;
    height: 250px;
    object-fit: cover;
    border-radius: 5px;
    margin-bottom: 1px;
}
"""

# Set dark theme
st.markdown('<style>' + CSS + '</style>', unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .stApp {
        background-color: rgba(0, 0, 0, 0);
        color: red;
    }
    .st-ba {
        background-color: rgba(0, 0, 3, 0);
        
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load CSV data
dataMain = pd.read_csv('./Final/data.csv')
dataPoster =  pd.read_csv('./Final/MovieGenre.csv')
# App header
st.title("Netflix Search")
st.markdown("---")


def find_poster_with_title(df, s):
    mask = df['Title'].str.contains(re.escape(s))
    if mask.any():
        return df.loc[mask, 'Poster'].iloc[0]
    else:
        return "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmUo2nZHDQPSF3vGwsETiT4uMNmMr4RmCIIg&usqp=CAU"



def result(dataframe, dropdown, user_id):
    user_id = int(user_id)
    movies = dataframe.loc[(dataframe['userId'] == user_id), dropdown].values[0]
    result = ast.literal_eval(movies)
    return result

# Insert or edit Models you implemented (name of columns)
dropdown_options = ["Cluster_Based","Content_Based","Deep_Factorization_Machine","Factorization_Machine","KNN_Collaborative_Filtring","Light_GCN","Matrix_Factorization","Neural_Graph_Collaborative_Filtring"]


with st.container():
    dropdown = st.selectbox("Select an option", dropdown_options)
    search = st.text_input("Enter a search query")


box_style = """
    display: inline-block;
    vertical-align: top;
    text-align: center;
    padding: 10px;
    margin: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
"""

if st.button("Generate Recommendations"):
    movies = result(dataMain, dropdown, search)
    
    # Apply CSS style to each box
    st.markdown(f'<div style="{box_style}">', unsafe_allow_html=True)
    for movie in movies:
        # Display image and title in a box
        st.markdown(f'<div style="{box_style}"><img src="{find_poster_with_title(dataPoster, movie)}" width="150"><p>{movie}</p></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


