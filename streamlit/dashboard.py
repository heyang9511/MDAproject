
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# load dataframe of transcripts
data = pd.read_excel("data/transcripts.xlsx", index_col=0)

# define dashboard title
st.title("Modern Data Analytics Project")

# define sidebar and country selection
option = st.sidebar.selectbox("Which Country?", data["country"])

# header to make clear which country was selected
st.header(option)

# sorry Kendall
# data_usa=data.query('country=="USA"').set_index(pd.Index(range(0,len(data.query('country=="USA"')))))

# filter data based on selected country
data_filtered = data.loc[data['country'] == option]
#st.dataframe(data_filtered.head(4))

# provide option for term to be searched in the transcripts
term = st.sidebar.text_input("Term", value="climate", max_chars=30).lower()

# interactive text that specifies which term was selected for plotting
blurb = "Number of times {} was mentioned".format(term)
st.text(blurb)

# loop-de-loop that does the counting
count = np.empty(0)
for i in data_filtered.index:
    count = np.append(count, word_tokenize(data_filtered["transcript"][i].lower()).count(term))

# creating scatter plot of year and count with loess regression line
year=np.array(data_filtered["year"])
fig2, ax = plt.subplots()
sns.regplot(year, count, lowess=True, line_kws={"color": "red"})
st.pyplot(fig2)

# plot without loess line
# fig, ax = plt.subplots()
# plt.scatter(year, count)
# plt.ylabel("Word Count")
# plt.xlabel("Year")
# st.pyplot(fig)