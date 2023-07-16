import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

@st.cache
def load_data(data):
    df = pd.read_csv(data)
    return df

def count_plot(dataframe, column_name, title=None, hue=None):
    '''
    Function to plot seaborn count plot
    Input: Dataframe name that has to be plotted, column_name that has to be plotted, title for the graph
    Output: Plot the data as a count plot
    '''
    base_color = sns.color_palette()[0]
    sns.countplot(data=dataframe, x=column_name, hue=hue)
    plt.title(title)


def run_eda():
    st.subheader("EDA")
    submenu = st.sidebar.selectbox("Submenu", ["EDA", "Plots"])
    df = load_data("data/BlackFriday.csv")

    if submenu == "EDA":
        st.subheader("Exploratory Data")
        st.dataframe(df.head())

        c1, c2 = st.columns(2)

        with st.expander("Descriptive Summary"):
            st.dataframe(df.describe())

        with c1:
            with st.expander("Gender Distribution"):
                st.dataframe(df['Gender'].value_counts())

        with c2:
            with st.expander("Age Distribution"):
                st.dataframe(df['Age'].value_counts())

    elif submenu == "Plots":
        st.subheader("Plotting")
        col1, col2 = st.columns(2)

        with col1:
            with st.expander("Pie Chart (Gender)"):
                gen_df = df['Gender'].value_counts().to_frame()
                gen_df = gen_df.reset_index()
                gen_df.columns = ['Gender Type', 'Counts']
                p01 = px.pie(gen_df, names='Gender Type', values='Counts')
                st.plotly_chart(p01, use_container_width=True)

            with st.expander("City"):
                city_df = df['City_Category'].value_counts().to_frame()
                city_df = city_df.reset_index()
                city_df.columns = ['Category', 'Counts']
                p01 = px.pie(city_df, names='Category', values='Counts')
                st.plotly_chart(p01, use_container_width=True)

        with col2:
            with st.expander("Bar Chart (Gender)"):
                fig = plt.figure()
                count_plot(df, 'Gender', title="Gender Distribution")
                st.pyplot(fig)

            with st.expander("Plot of Occupation"):
                fig = plt.figure()
                count_plot(df, 'Occupation', title="Occupation Distribution")
                st.pyplot(fig)

        with st.expander("Age"):
            age_df = df['Age'].value_counts().to_frame()
            age_df = age_df.reset_index()
            age_df.columns = ['Age Range', 'Counts']
            p01 = px.bar(age_df, x='Age Range', y='Counts')
            st.plotly_chart(p01, use_container_width=True)

        with st.expander("Gender vs Marital Status"):
            marital_df = df.groupby(['Gender', 'Marital_Status']).size().reset_index(name='Counts')
            po2 = px.bar(marital_df, x='Marital_Status', y='Counts', color='Gender')
            st.plotly_chart(po2)

