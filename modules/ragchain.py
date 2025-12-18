from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from modules.prompt import prompt
from langchain_core.output_parsers import StrOutputParser

#Util functions
def expand_query(input_value):
    if isinstance(input_value, dict):
        q = input_value.get("question", "")
    else:
        q = input_value

    extra = " nutrition healthy diet guidelines fruits vegetables sugar salt fat who usda recommendations"
    return q + extra

def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])


def build_chain(retriever,llm):
    rag_chain = (
        {
            "context": RunnableLambda(expand_query) | retriever | RunnableLambda(format_docs),
            "question": RunnablePassthrough()
        }
        | prompt
        | llm 
        | StrOutputParser()
    )
    return rag_chain