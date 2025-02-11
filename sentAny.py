# #setiment anyliser
# from langchain_groq import ChatGroq


# llm = ChatGroq(
#     model="mixtral-8x7b-32768",
#     temperature=0.2,
#     groq_api_key="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" 
# )


# def analyze_sentiment_and_suggest(text):
#     prompt = f"""
#     You are an assistant that 
#     analyzes the sentiment of a 
#     given text and provides useful suggestions
#     based on the tone of the text:
#     ---
#     {text}
#     ---
#     Based on the sentiment of the text,
#     please provide one of the following:
#     1. The sentiment of the text: 'Positive', 'Negative', or 'Neutral'.
#     2. A helpful suggestion or advice based on the sentiment:
#         - If the sentiment is positive, suggest ways to maintain or enhance it.
#         - If the sentiment is negative, suggest ways to improve or overcome the negativity.
#         - If the sentiment is neutral, suggest ways to add more emotion or perspective to the text.
#     """
    
    
#     response = llm.invoke(prompt, max_tokens=150)
#     return response.content.strip()


# def main():
#     print("Enter a sentence to analyze the sentiment and receive suggestions (type 'exit' to quit):")
#     while True:
#         user_input = input("Your input: ")
        
        
#         if user_input.lower() == 'exit':
#             print("Exiting the sentiment analysis tool.")
#             break
        
       
#         result = analyze_sentiment_and_suggest(user_input)
        
        
#         print(f"Result:\n{result}\n")



# main()

import streamlit as st
from langchain_groq import ChatGroq

# Configure the language model
llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0.2,
    api_key="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"  # Replace with your actual API key
)

def analyze_sentiment_and_suggest(text):
    prompt = f"""
    You are an assistant that 
    analyzes the sentiment of a 
    given text and provides useful suggestions
    based on the tone of the text:
    Analyze the sentiment of the following text: {text}
    Provide a helpful suggestion or advice based on the sentiment.
    
    ---
    {text}
    ---
    Based on the sentiment of the text,
    please provide one of the following:
    1. The sentiment of the text: 'Positive', 'Negative', or 'Neutral'.
    2. A helpful suggestion or advice based on the sentiment:
        - If the sentiment is positive, suggest ways to maintain or enhance it.
        - If the sentiment is negative, suggest ways to improve or overcome the negativity.
        - If the sentiment is neutral, suggest ways to add more emotion or perspective to the text.
    """
    
    response = llm.invoke(prompt, max_tokens=150)
    return response.content.strip()

# Streamlit app
st.title("Sentiment Analyzer and Suggestion Tool 📊")
st.subheader("Analyze the sentiment of your text and receive useful suggestions!")
st.sidebar.title("Instructions")
st.sidebar.write("Enter a sentence and click the button to analyze its sentiment. "
                 "The app will provide sentiment analysis and suggestions based on the tone.")

input_text = st.text_input("Enter a sentence:", placeholder="Type your sentence here...")

if st.button("Analyze Sentiment"):
    if input_text:
        result = analyze_sentiment_and_suggest(input_text)
        st.write("### Result:")
        st.success(result)
    else:
        st.warning("Please enter a sentence to analyze.")

# Add some style
st.markdown(
    """
    <style>
    .css-1d391kg {background-color: #f0f0f0; padding: 20px; border-radius: 10px;}
    .css-164nlkn {font-size: 1.2em; font-weight: bold; color: #0000ff;}
    .css-2trqyj {font-size: 1em; color: #ff0000;}
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 12px;
        border: none;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    body {background-color: #e8f4f8;}
    </style>
    """, unsafe_allow_html=True
)

# Adding a footer
st.markdown(
    """
    <div style="position: fixed; left: 0; bottom: 0; width: 100%; background-color: #333; color: white; text-align: center; padding: 10px;">
        Created with 💖 by saurabh
    </div>
    """, unsafe_allow_html=True
)
