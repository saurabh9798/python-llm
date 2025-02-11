import streamlit as st
from langchain_groq import ChatGroq

def correct_grammar(text):
    llm = ChatGroq(
        model="gemma2-9b-it",
        temperature=0,
        api_key="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"  # Replace with your actual API key
    )
    
    prompt = (
        f"Check the grammar of the following text. "
        f"If it's correct, return it as is. "
        f"If it has grammar mistakes, correct them without "
        f"changing the meaning or adding extra words. "
        f"Also, list the incorrect words and provide feedback "
        f"on what went wrong.\nText: {text}"
    )
    
    response = llm.invoke(prompt)
    corrected_text = response.content.strip()
    
    return corrected_text

def extract_incorrect_words(response_text):
    incorrect_words = []
    lines = response_text.splitlines()
    feedback_section = False
    for line in lines:
        if "incorrect words" in line.lower():
            feedback_section = True
        if feedback_section:
            incorrect_words.append(line.strip())
    return incorrect_words

# Streamlit app
st.title("Grammar Checker App 📚")
st.subheader("Correct your sentences and get feedback!")
st.sidebar.title("Instructions")
st.sidebar.write("Enter a sentence and click the button to check its grammar. "
                 "The app will provide corrections and feedback.")

input_text = st.text_input("Enter a sentence:", placeholder="Type your sentence here...")

if st.button("Check Grammar"):
    if input_text:
        corrected_text = correct_grammar(input_text)
        if corrected_text == input_text.strip():
            st.success("Sentence is already correct: " + input_text)
        else:
            st.write("### Corrected Text:")
            st.success(corrected_text)
            
            incorrect_words_feedback = extract_incorrect_words(corrected_text)
            if incorrect_words_feedback:
                st.write("### Incorrect Words and Feedback:")
                st.write("\n".join(incorrect_words_feedback))
    else:
        st.warning("Please enter a sentence to check.")

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
        Created with 💖 by [Your Name]
    </div>
    """, unsafe_allow_html=True
)
