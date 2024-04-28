import streamlit as st
import joblib

#load the trained model
model = joblib.load("sentiment-model.pkl")

#deifne the sentiment labels
sentiment_labels = {'1':'positive','0':'Negtive'}

#create streamlit app
st.title('sentiment analysis')

#input text area
user_input =st.text_area("enter your text here:")

#prediction button
if st.button('predict'):
    #perform sentiment prediction
    print(user_input)
    predicted_sentiment=model.predict([user_input])[0]
    print("predicted label:" +str(predicted_sentiment))
    predicted_sentiment_label = sentiment_labels[str(predicted_sentiment)]

    #display predicted sentimnet
    st.info(f'predited statement : {predicted_sentiment_label}')