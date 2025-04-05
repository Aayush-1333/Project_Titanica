import streamlit as st
import joblib
import pandas as pd


def categorize__age_transfomer(X: pd.DataFrame, y=None) -> pd.DataFrame:
    return X.apply(pd.cut, bins=[0, 30, 50, 90], labels=['young', 'middle', 'old'])


def categorize__fare_transformer(X: pd.DataFrame) -> pd.DataFrame:
    return X.apply(pd.cut, bins=[-0.5, 150, 300, 600], labels=['low', 'mid', 'high'])


def rename_cols(X: pd.DataFrame) -> pd.DataFrame:
    X.columns = [
        "Age_middle", "Age_old", "Age_young",
        "Fare_high", "Fare_low", "Fare_mid",
        "Embarked_C", "Embarked_Q", "Emabrked_S",
        "Pclass", "Sex_female", "Sex_male",
        "SibSp", "Parch"
    ]
    return X


clf_pipeline = joblib.load("./data/svc_pipeline.bz2")
def predict(data: dict) -> int:
    # st.write(data)
    test_data = pd.DataFrame(data=data)
    return clf_pipeline.predict(test_data)[0]


st.title("Classifier Model")
with st.form("passenger_details"):
    col1, col2 = st.columns([2, 2])
    with col1:
        age = st.number_input("Age", min_value=0.0, step=0.5)
        fare = st.number_input("Fare", min_value=0.0, step=0.25)
        sibsp = st.checkbox("SibSp")
        parch = st.checkbox("Parch")

    with col2:
        pclass = st.selectbox("Pclass", ["1", "2", "3"])
        sex = st.selectbox("Sex", ["Male", "Female"])
        embarked = st.selectbox("Embarked", ["Southampton", "Chersbourg", "Queenstown"])

    submitted = st.form_submit_button("Submit")
    if submitted:
        passenger_data = {
            "PassengerId": [712],
            "Pclass": [int(pclass)],
            "Name": ["Passenger"],
            "Sex": [sex.lower()],
            "Age": [float(age)],
            "SibSp": [int(sibsp)],
            "Parch": [int(parch)],
            "Ticket": ["35410"],
            "Fare": [float(fare)],
            "Cabin": ["A16"],
            "Embarked": [embarked[0]]
        }
        result = predict(passenger_data)
        st.write("The person survived" if result else "The person didn't survive in the incident")
