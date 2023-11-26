import os
import sys

from flask import Flask, request, jsonify
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader, CSVLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.vectorstores import Chroma

import constants

from langdetect import detect

chatgpt = Flask(__name__)
os.environ["OPENAI_API_KEY"] = constants.APIKEY

# Enable to save to disk & reuse the model (for repeated queries on the same data)
PERSIST = False
#
query = None
if len(sys.argv) > 1:
    query = sys.argv[1]

if PERSIST and os.path.exists("persist"):
    print("Reusing index...\n")
    vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
    index = VectorStoreIndexWrapper(vectorstore=vectorstore)
else:
    loader = CSVLoader("data/films.csv")
    if PERSIST:
        index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory": "persist"}).from_loaders([loader])
    else:
        index = VectorstoreIndexCreator().from_loaders([loader])

chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model="gpt-4-1106-preview"),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)

history = []
chat_history=[{}]

@chatgpt.route('/find', methods=['GET'])
def find():
    return "Good"


@chatgpt.route('/find_data', methods=['POST'])
def find_data():
    data = request.json  # Парсим JSON из запроса
    query = data.get('query')  # Получаем значение 'query' из JSON
    print(query)
    detect_language = detect(query)
    result = index.query(query)
    if result!="I don't know":
        try:
            lang_result=detect(result)
            if(lang_result!=detect_language):
                result_end= chain({"question": f"write this text:{result} in this language only:{detect_language}", "chat_history": history})
                print(result_end['answer'])
            else:
                print(result)
        except:
            print(result)
    try:
        history.append((query, result['answer']))
    except:
        history.append((query, result))
    return jsonify({'chat_history': history})
    return None

# for item in history:
#     print(item)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    chatgpt.run(debug=True, host='127.0.0.1', port=port)