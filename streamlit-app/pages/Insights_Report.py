import streamlit as st
import pandas as pd


st.title("Insights Report")

df = pd.read_csv("./pages/train_cleaned.csv", index_col=0)
st.dataframe(data=df)

survived = df[df["Survived"] == 1]
deceased = df[df["Survived"] == 0]

st.markdown("## Bar Charts")
tab1, tab2, tab3, tab4 = st.tabs(["Age", "Fare", "Gender", "Embarked"])
with tab1:
    survived_grouped_age = survived.groupby(survived['Age']).count().reset_index()
    deceased_grouped_age = deceased.groupby(deceased['Age']).count().reset_index()

    st.markdown("## Age groups")
    st.markdown("""
        `young` = Ages between 0 to 30\n
        `middle` = Ages between 30 to 50\n
        `old` = Ages greater than 50
    """)

    col1, col2 = st.columns([2, 2])
    with col1:
        st.markdown("#### Survived")
        st.bar_chart(data=survived_grouped_age, x='Age', y='Survived', y_label="No. of passengers", color=["#da0"])
    with col2:
        st.markdown("#### Deceased")
        st.bar_chart(data=deceased_grouped_age, x='Age', y='Survived', y_label="No. of passengers", color=["#fa0"])
        
with tab2:
    survived_grouped_fare = survived.groupby(survived['Fare']).count().reset_index()
    deceased_grouped_fare = deceased.groupby(deceased['Fare']).count().reset_index()

    st.markdown("## Fare groups")
    st.markdown("""
        `low` = Low price fares\n
        `mid` = Middle price fares\n
        `high` = expensive fares
    """)

    col1, col2 = st.columns([2, 2])
    with col1:
        st.markdown("#### Survived")
        st.bar_chart(data=survived_grouped_fare, x='Fare', y='Survived', y_label="No. of passengers", color=["#da0"])
    with col2:
        st.markdown("#### Deceased")
        st.bar_chart(data=deceased_grouped_fare, x='Fare', y='Survived', y_label="No. of passengers", color=["#fa0"])

with tab3:
    survived_grouped_sex = survived.groupby(survived['Sex']).count().reset_index()
    deceased_grouped_sex = deceased.groupby(deceased['Sex']).count().reset_index()

    st.markdown("## Gender groups")
    st.markdown("""
        `male` = Male passengers\n
        `female` = Female passengers
    """)

    col1, col2 = st.columns([2, 2])
    with col1:
        st.markdown("#### Survived")
        st.bar_chart(data=survived_grouped_sex, x='Sex', y='Survived', y_label="No. of passengers", color=["#da0"])
    with col2:
        st.markdown("#### Deceased")
        st.bar_chart(data=deceased_grouped_sex, x='Sex', y='Survived', y_label="No. of passengers", color=["#fa0"])

with tab4:
    survived_grouped_embarked = survived.groupby(survived['Embarked']).count().reset_index()
    deceased_grouped_embarked = deceased.groupby(deceased['Embarked']).count().reset_index()

    st.markdown("## Embarked groups")
    st.markdown("""
        `S` = Southampton\n
        `Q` = Queenstown\n
        `C` = Chersbourg
    """)

    col1, col2 = st.columns([2, 2])
    with col1:
        st.markdown("#### Survived")
        st.bar_chart(data=survived_grouped_embarked, x='Embarked', y='Survived', y_label="No. of passengers", color=["#da0"])
    with col2:
        st.markdown("#### Deceased")
        st.bar_chart(data=deceased_grouped_embarked, x='Embarked', y='Survived', y_label="No. of passengers", color=["#fa0"])
