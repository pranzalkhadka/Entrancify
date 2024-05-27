import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain.vectorstores import FAISS
from langchain_community.vectorstores.faiss import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

raw_text = """Amrit Campus, formally named as Public Science College (PUSCOL) and later named as Amrit
Science College (ASCOL), after late Mr. Amrit Prasad Pradhan. Mr pradhan was born in 1918 at
Thamel, Kathmandu. He served as headmaster of Jooddha High School in Birgunj for two years
and later joined at Tri-Chandra College as lecturer in Chemistry. In 1962, he became founder
Principal of Public Science College (present Amrit Campus) and began teaching as professor of
Chamistry. Late Principal Amrit Prasad Pradhan established Amrit Campus with a view to
promote the study of Science and Technology in Nepal. The campus has benefited greatly from
his spirit or enterprise, dedication and enthusiasm. While on a mission to the United States of a
cause connected with the college, he died in an air crash over Mt. Blanc on January 24, 1966.
The death of this noble soul was mourned by the nation.

Patan Multiple Campus was established on 2nd September 1954 AD under the Ministry of
Education of Nepal. This campus was established even before the establishment of Tribhuvan
University. Patan Multiple Campus was founded with the name “Patan Inter College” and was
inaugurated by the Crowned Prince His Majesty Mahendra Bir Bikram Shah. The Campus was
renamed Patan Multiple Campus after the implementation of the National Education System in
2030 BS (1973 AD). Only in 1973 AD, the Campus was added to tribhuvan University as a
constituent campus. The campus occupies about 27,296 sq. m area. Patan Multiple Campus is
well facilitated with sufficient classrooms with spacious premises that fit all the required
infrastructures of the faculties. Being one of the largest campuses in Nepal it has all its facilities
within the premises of the campus and they are equipped for every program they learn.

ST. XAVIER’S COLLEGE, Kathmandu, is an educational institution of higher
learning established and managed by the Nepal Jesuit Society. The Jesuits began their
educational work in Nepal in 1951 with the opening of St. Xavier’s School, Godavari,
followed by St. Xavier’s School, Jawalakhel, St. Xavier’s School, Deonia, Moran
Memorial School, Maheshpur,and St. Xavier’s School, Sadakbari. The Jesuits have
served people of all faiths, all over the world, as educators, scientists, explorers and
social reformers since 1540. The centuries-old tradition of service to others is the
cornerstone of Jesuit education. Every institute and organization established by the
Jesuits in Nepal, prepares each student to Live for God and Lead for Nepal. The
education programme is designed to foster criticalthinking, positive action and service
to others. It challenges students to look beyond career, and have a wider vision of being
channels of betterment. It encourages every student to be a job creator rather than a job
seeker, and to play the role of being a creative designer of the future.

Tribhuvan University, Bhaktapur Multiple Campus (BKMC), is established in 1959 in Bhaktapur, 
situated at the heart of Bhaktapur Municipality, Bhaktapur, Bagmati Province, as an educational institute 
to educate young Nepalese women and men entering the field of Information Technology, Science, Humanities and Management. 
Bhaktapur Multiple Campus is the pioneer constituent campus of Tribhuvan University (TU) 
which has become one of the pioneer educational organizations in Nepal since its establishment. 
Within Five decades, the campus gradually expanded its academic program from PCL to Master in Humanities and Management. 
Bhaktapur Multiple Campus is an academic center of excellence through the foundation of integrated subjects 
with its specialization in Information technology, Finance, Accounting, Management, Banking, Physics, Chemistry, Biology and Mathematics Sociology
 and Rural Development. 
"""


st.set_page_config(page_title="Document Genie", layout="wide")


api_key = st.secrets["GOOGLE_API_KEY"]


def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks, api_key):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")


def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3, google_api_key=api_key)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain


def user_input(user_question, api_key):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    st.write("Reply: ", response["output_text"])


def main():
    st.header("Helper Chatbot")

    user_question = st.text_input("Ask any questions about colleges", key="user_question")

    if user_question and api_key: 
        user_input(user_question, api_key)

    text_chunks = get_text_chunks(raw_text)
    get_vector_store(text_chunks, api_key)