from typing import List
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
import config


class CustomerMemory:
    """Per-user FAISS vector store of facts/preferences."""

    def __init__(self):
        self.embeddings = OpenAIEmbeddings(openai_api_key=config.OPENAI_API_KEY)
        self.stores: dict[str, FAISS] = {}

    def _get_store(self, user_id: str) -> FAISS:
        if user_id not in self.stores:
            # empty store → will be populated on first add
            self.stores[user_id] = FAISS.from_texts([""], self.embeddings)
        return self.stores[user_id]

    def add_fact(self, user_id: str, fact: str) -> None:
        """Embed and store a fact."""
        store = self._get_store(user_id)
        doc = Document(page_content=fact, metadata={"user_id": user_id})
        store.add_documents([doc])

    def retrieve_relevant_facts(self, user_id: str, query: str, k: int = 2) -> List[str]:
        """Return top-k fact strings relevant to the query."""
        store = self._get_store(user_id)
        if store.index.ntotal == 0:
            return []

        # embed query exactly like the reference script
        query_vec = self.embeddings.embed_query(query)
        docs = store.similarity_search_by_vector(query_vec, k=k)
        return [doc.page_content for doc in docs]
