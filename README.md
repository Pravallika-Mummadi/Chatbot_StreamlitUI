# Projects
Generative AI Chatbot with Streamlit

1. Developed a chatbot application using Python that integrates with a generative AI model for interactive conversations.
2. Utilized langchain library for managing the language model interface, specifically employing the CTransformers class to handle the Mistral-7B model for generating AI responses.
3. Configured the model with a temperature of 0.00 and a context length of 8000 to ensure accurate and contextually relevant responses.
4. Created a PromptTemplate to format user queries for the AI model and set up an LLMChain to streamline the process of generating responses.
5. Implemented a Streamlit-based user interface in UI.py, which includes features such as:
  Persistent chat history using st.session_state to maintain continuity across interactions.
  Real-time display of user and assistant messages in a chat-like format.
  Input handling that allows users to submit queries and receive responses from the AI model.
6. Enabled a seamless user experience by incorporating interactive elements and maintaining a clear and organized chat flow.
