# # import streamlit as st
# # from langchain_groq import ChatGroq

# # llm = ChatGroq(
# #     model="mixtral-8x7b-32768",
# #     temperature= 0,
# #     api_key="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",
# # )


# # st.title("mera tera sabka llm Chatbot")
# # st.write("Question dalo :")

# # user_input = st.text_input("mera Question :","")

# # if st.button("ye lo tumara Answer"):
# #     response = llm.invoke(user_input)
# #     st.write("### Response : ")
# #     st.write(response.content)

# import streamlit as st
# from langchain_groq import ChatGroq

# # Configure the language model
# llm = ChatGroq(
#     model="mixtral-8x7b-32768",
#     temperature=0,
#     api_key="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",
# )

# # Title of the app
# st.title("Mera Tera Sabka LLM Chatbot 🤖")

# # Subtitle for a bit of charm
# st.subheader("Aapka apna AI dost! 💬")

# # Instructional text
# st.write("Question dalo aur jawab pao:")

# # Create input box for user questions
# user_input = st.text_input("Mera Question:", placeholder="Type your question here...")

# # Button to get the response
# if st.button("Ye lo tumara Answer"):
#     if user_input:
#         response = llm.invoke(user_input)
#         st.write("### Response:")
#         st.write(response.content)
#     else:
#         st.warning("Please enter a question to get an answer.")

# # Add some style
# st.markdown(
#     """
#     <style>
#     .css-1d391kg {background-color: #f0f0f0; padding: 20px; border-radius: 10px;}
#     .css-164nlkn {font-size: 1.2em; font-weight: bold; color: #0000ff;}
#     .css-2trqyj {font-size: 1em; color: #ff0000;}
#     </style>
#     """, unsafe_allow_html=True
# )

import streamlit as st
from langchain_groq import ChatGroq

# Configure the language model
llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    api_key="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",
)

# Title of the app
st.title("Mera Tera Sabka LLM Chatbot 🤖")

# Subtitle for a bit of charm
st.subheader("Aapka apna AI dost! 💬")

# Adding a nice sidebar
st.sidebar.title("Welcome!")
st.sidebar.write("This is your friendly neighborhood chatbot. Feel free to ask me anything!")

# Adding an image for a visual touch
st.image("https://images.unsplash.com/photo-1498050108023-c5249f4df085", caption='Connecting Ideas')

# Instructional text
st.write("### Question dalo aur jawab pao:")

# Create input box for user questions
user_input = st.text_input("Mera Question:", placeholder="Type your question here...")

# Button to get the response
if st.button("Ye lo tumara Answer"):
    if user_input:
        response = llm.invoke(user_input)
        st.write("### Response:")
        st.success(response.content)
    else:
        st.warning("Please enter a question to get an answer.")

# Additional layout and style
st.markdown(
    """
    <style>
    .css-1d391kg {background-color: #f0f0f0; padding: 20px; border-radius: 10px;}
    .css-164nlkn {font-size: 1.2em; font-weight: bold; color: #0000ff;}
    .css-2trqyj {font-size: 1em; color: #ff0000;}
    body {background-color: #e8f4f8;}
    </style>
    """, unsafe_allow_html=True
)

# Adding a footer
st.markdown(
    """
    <div style="position: fixed; left: 0; bottom: 0; width: 100%; background-color: #333; color: white; text-align: center; padding: 10px;">
        Created with 💖 by Saurabh
    </div>
    """, unsafe_allow_html=True
)

