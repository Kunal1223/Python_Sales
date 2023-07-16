import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

@st.cache
def load_data(data):
    df = pd.read_csv(data)
    return df

def run_home_page():
    df = load_data("data/thanksgiving_in_multi_lang.csv")

    with st.expander("Happy Thanksgiving Day", expanded=True):
        day_text = " ".join(df['Day'].tolist())
        mywordcloud = WordCloud().generate(day_text)
        plt.imshow(mywordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot()

    lang_list = df['Language'].unique().tolist()
    lang_choice = st.sidebar.selectbox("Lang", lang_list)

    if lang_choice:
        thank_word = df[df["Language"] == lang_choice].iloc[0].Word
        thank_day = df[df["Language"] == lang_choice].iloc[0].Day
        st.info("How to Say Happy Thanksgiving in {}".format(lang_choice))
        st.write({"lang": lang_choice, "word": thank_word, "day": thank_day})

    name = st.text_input("Name", "Streamlit")
    bgcolor = st.color_picker("Background Color")
    modified_name = "From {0} {0} {0}".format(name)
    updated_text = []
    updated_text.append(modified_name)
    updated_text.extend(df['Word'].tolist())
    new_text = " ".join(updated_text)

    with st.expander("Thanksgiving From {}".format(name)):
        mywordcloud = WordCloud(background_color=bgcolor).generate(new_text)
        plt.imshow(mywordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot()

