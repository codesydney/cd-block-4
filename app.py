import os.path
from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

os.environ['OPENAI_API_KEY'] = '<hidden>'

# check if storage already exists
if not os.path.exists("./storage"):
    # load the documents and create the index
    documents = SimpleDirectoryReader("/Users/engramarbollas/Projects/cd-block-4/data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist()
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)

# either way we can now query the index
query_engine = index.as_query_engine()
response = query_engine.query("How much is Customer A invoice and how many support tickets?")
print(response)