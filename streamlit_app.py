import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# Create header of page
st.markdown("<h1><center> Niche Coding Communities Call GitHub for Help</center></h1>", unsafe_allow_html=True)
st.markdown("<h5><center>More Popular Languages Use it for Fun and Creativity</center></h5>", unsafe_allow_html=True)

# Datapath
csv_file_path = 'github_dataset2.csv'

# Drop Null Languages
df = pd.read_csv(csv_file_path)
df = df.drop(df[df['Language'] == ""].index)

# Get data for top left chart
average_stars_by_language = df.groupby('Language').agg({'Stars Count': 'mean', 'Language Frequency': 'mean'}).reset_index()
top_10_languages = average_stars_by_language.sort_values(by='Stars Count', ascending=False).head(10)

# Get data for bottom left chart
stars_by_freq = df.groupby('Language Frequency')['Stars Count'].mean()
stars_by_freq = stars_by_freq.reset_index()

# Get data for top right chart --> Language frequency by contributors and pull requests
result = df.groupby('Language Frequency').agg({'Contributors': 'mean', 'Pull Requests': 'mean', 'Forks Count': 'mean'}).reset_index()

# Additional dataframe for bottom right chart
df2 = pd.read_csv('github_dataset3.csv')

# Bottom right chart
chart = alt.Chart(df2).mark_circle().encode(
    x='Forks Count',
    y='Pull Requests',
    color='Frequency Category',
).interactive()

# Two columns for layout
col1, col2 = st.columns(2)

# First column about less popular languages' repositories being used by other more for community help
with col1:
    # Title
    st.markdown("<h2><center>Less Popular, More for Help</center></h2>", unsafe_allow_html=True)
    # Top left chart layout
    st.bar_chart(data=top_10_languages, x='Language', y='Stars Count', color="#FFA500", width=0, height=0, use_container_width=True)
    # Caption
    st.markdown("<p><center>Less frequently used languages like Assembly, Vim Script and Vue receive most repository stars -- a proxy for repository helpfulness</center></p>", unsafe_allow_html=True)
    # Bottom left chart layout
    st.bar_chart(data=stars_by_freq, x='Language Frequency', y='Stars Count', color="#7F00FF", width=0, height=0, use_container_width=True)

# Second column about more popular languages' repositories being used by others more for others for inspitation
with col2:
    # Title
    st.markdown("<h2><center>More Popular, More for Inspiration</center></h2>", unsafe_allow_html=True)
    # Top right chart layout
    st.vega_lite_chart(
        result,
        {
            "mark": {"type": "circle", "tooltip": True},
            "encoding": {
                "x": {"field": "Language Frequency", "type": "quantitative"},
                "y": {"field": "Contributors", "type": "quantitative"},
                "color": {"field": "Pull Requests", "type": "quantitative"},
            },
        }, 
        use_container_width=True
    )
    # Caption
    st.markdown("<p><center>Repositories of more popular programming language have more forks, contributors and pull requests, indicating high engagement</center></p>", unsafe_allow_html=True)
    # Bottom right chart layout
    st.altair_chart(chart, theme="streamlit", use_container_width=True)

# Data table
st.markdown("<p><center>Data Used for Tables</center></p>", unsafe_allow_html=True)
st.dataframe(df)

# Acknowledgements
st.markdown("<p>Data source:</p>", unsafe_allow_html=True)
st.markdown("<a>https://www.kaggle.com/datasets/nikhil25803/github-dataset/data</a>", unsafe_allow_html=True)
st.markdown("<p>Dashboard By: Mark Rubin</p>", unsafe_allow_html=True)