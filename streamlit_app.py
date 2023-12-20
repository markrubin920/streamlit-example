import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.markdown("<h1><center> Niche Coding Communities Call GitHub for Help</center></h1>", unsafe_allow_html=True)
st.markdown("<h5><center>More Popular Languages Use it for Fun and Creativity</center></h5>", unsafe_allow_html=True)
# """

csv_file_path = 'github_dataset2.csv'

df = pd.read_csv(csv_file_path)
df = df.drop(df[df['language'] == ""].index)

df2 = pd.read_csv('github_dataset4.csv')

chart = alt.Chart(df2).mark_circle().encode(
    x='forks_count',
    y='pull_requests',
    color='Frequency Category',
).interactive()

average_watchers_by_language = df.groupby('language')['stars_count'].mean()

# Reset the index to make 'primary_language' a column again
average_watchers_by_language = average_watchers_by_language.reset_index()

# Sort the DataFrame by the average watchers in descending order
top_5_languages = average_watchers_by_language.sort_values(by='stars_count', ascending=False).head(10)

# forks_by_language = df.groupby('language').agg({'Language Frequency': 'mean', 'forks_count': 'mean'}).reset_index()

# Reset the index to make 'primary_language' a column again
# forks_by_language = forks_by_language.reset_index()

# Sort the DataFrame by the average watchers in descending order
# top_5forks_languages = forks_by_language.sort_values(by='forks_count', ascending=False).head(7)


stars_by_freq = df.groupby('Language Frequency')['stars_count'].mean()
stars_by_freq = stars_by_freq.reset_index()

# engagement_by_freq = df.groupby('Language Frequency')['pull_requests'].mean()['stars_count']

# engagement_by_freq = engagement_by_freq.reset_index()


result = df.groupby('Language Frequency').agg({'contributors': 'mean', 'pull_requests': 'mean', 'forks_count': 'mean'}).reset_index()
# st.dataframe(result)

# Create two columns
col1, col2 = st.columns(2)

# Place graphs or elements in each column
with col1:
    st.markdown("<h2><center>Less Popular, More Useful</center></h2>", unsafe_allow_html=True)
    st.bar_chart(data=top_5_languages, x='language', y='stars_count', color=None, width=0, height=0, use_container_width=False)
    # Add your first graph here
    st.markdown("<p><center>Less frequently used languages like Assembly, Vim Script and Vue receive most repository stars -- a proxy for repository usefulness</center></p>", unsafe_allow_html=True)
    st.bar_chart(data=stars_by_freq, x='Language Frequency', y='stars_count', color=None, width=0, height=0, use_container_width=False)


with col2:
    st.markdown("<h2><center>More Popular, More Community Action</center></h2>", unsafe_allow_html=True)
    # Add your second graph here
    st.vega_lite_chart(
        result,
        {
            "mark": {"type": "circle", "tooltip": True},
            "encoding": {
                "x": {"field": "Language Frequency", "type": "quantitative"},
                "y": {"field": "contributors", "type": "quantitative"},
                # "size": {"field": "forks_count", "type": "quantitative"},
                "color": {"field": "pull_requests", "type": "quantitative"},
            },
        }
    )
    st.markdown("<p><center>Repositories of more frequently used programming language have more forks, contributors and pull requests, indicating high engagement with the repository</center></p>", unsafe_allow_html=True)
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
    # st.scatter_chart(data=df, x='Language Frequency', y='forks_count', color=None, width=0, height=0, use_container_width=False)
    # st.scatter_chart(data=df, x='stars_count', y='pull_requests', color=None, size=None, width=0, height=0, use_container_width=True)



# Use the `read_csv` function to read the CSV file into a DataFrame
st.markdown("<p><center>Data Used for Tables</center></p>", unsafe_allow_html=True)
st.dataframe(df)

st.markdown("<p>Data source:</p>", unsafe_allow_html=True)
st.markdown("<a>https://www.kaggle.com/datasets/nikhil25803/github-dataset/data</a>", unsafe_allow_html=True)





# st.vega_lite_chart(
#    df,
#    {
#        "mark": {"type": "circle", "tooltip": True},
#        "encoding": {
#            "x": {"field": "contributors", "type": "quantitative"},
#            "y": {"field": "pull_requests", "type": "quantitative"},
#         #    "size": {"field": "c", "type": "quantitative"},
#            "color": {"field": "language", "type": "nominal"},
#        },
#    }, 
# )

# num_points = st.slider("Number of points in spiral", 1, 60000, 1100)
# num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

# indices = np.linspace(0, 1, num_points)
# theta = 2 * np.pi * num_turns * indices
# radius = indices

# x = radius * np.cos(theta)
# y = radius * np.sin(theta)

# df = pd.DataFrame({
#     "x": y,
#     "y": y,
#     "idx": indices,
#     "rand": np.random.randn(num_points),
# })

# st.altair_chart(alt.Chart(df, height=700, width=700)
#     .mark_point(filled=True)
#     .encode(
#         x=alt.X("x", axis=None),
#         y=alt.Y("y", axis=None),
#         color=alt.Color("idx", legend=None, scale=alt.Scale()),
#         size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
#     ))
