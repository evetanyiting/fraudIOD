import streamlit as st
import pandas as pd
import joblib
from utils import preprocessor

def run():
    model = joblib.load('sentiment_model.pkl')

    st.title("Sentiment Analysis")
    st.text("Basic app to detect the sentiment of text.")
    st.text("")
    userinput = st.text_input('Enter text below, then click the Predict button.', placeholder='Input text HERE')
    st.text("")
    
    if st.button("Predict") and userinput:
        predicted_sentiment = model.predict(pd.Series([userinput]))[0]
        output = 'positive 👍' if predicted_sentiment == 1 else 'negative'
        sentiment=f'Predicted sentiment of "{userinput}" is {output}.'
        st.success(sentiment)

if __name__ == "__main__":
    run()