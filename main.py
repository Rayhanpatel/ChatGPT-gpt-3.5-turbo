import os
import openai
import streamlit as st

from langchain.memory import ConversationBufferWindowMemory
from langchain import LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv, find_dotenv


_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']



template = """
Assistant is a large language model trained by OpenAI.

Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.

Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.

Overall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.

{history}
Human: {human_input}
Assistant:
"""

prompt = PromptTemplate(input_variables=["history", "human_input"], template=template)


llm_chain = LLMChain(
    llm=ChatOpenAI(temperature=0.6, model_name="gpt-3.5-turbo"),
    prompt=prompt,
    verbose=True,
    memory=ConversationBufferWindowMemory(k=2),
)



def main():
    st.set_page_config(page_title="ChatGPT")
    st.header("ChatGpt")

    user_question = st.text_input("Enter the question")

    if user_question is not None and user_question != "":
        st.write(llm_chain.predict(human_input=user_question))
        st.write(llm_chain.memory.buffer)
if __name__ == "__main__":
    main()
