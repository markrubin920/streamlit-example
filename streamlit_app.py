import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# """
# # Welcome to Streamlit!

# Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
# If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
# forums](https://discuss.streamlit.io).

# In the meantime, below is an example of what you can do with just a few lines of code:
# """

csv_file_path = 'github_dataset.csv'

# Use the `read_csv` function to read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
df = df.drop(df[df['language'] == ""].index)

average_watchers_by_language = df.groupby('language')['stars_count'].mean()

# Reset the index to make 'primary_language' a column again
average_watchers_by_language = average_watchers_by_language.reset_index()

# Sort the DataFrame by the average watchers in descending order
top_5_languages = average_watchers_by_language.sort_values(by='stars_count', ascending=False).head(10)


st.dataframe(df)

st.bar_chart(data=top_5_languages, x='language', y='stars_count', color=None, width=0, height=0, use_container_width=False)

st.scatter_chart(data=df, x='stars_count', y='pull_requests', color=None, size=None, width=0, height=0, use_container_width=True)

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
