# Sample document dataset stored as a list of dictionaries
documents = [
    {"title": "Eiffel Tower", "content": "The Eiffel Tower was built in 1889 and is located in Paris, France."},
    {"title": "Python Programming", "content": "Python is a versatile programming language used for web development, data science, automation, and more."},
    {"title": "Albert Einstein", "content": "Albert Einstein was a German physicist best known for developing the theory of relativity."},
    {"title": "Great Wall of China", "content": "The Great Wall of China is a series of fortifications that were built along the northern borders of China to protect against invasions."}
]

def search_documents(query,documents,top_k=3):
     """
    Search for relevant documents based on a keyword match.
    :param query: The query string for searching
    :param documents: List of documents (dictionaries)
    :param top_k: Number of top documents to retrieve
    :return: List of document contents
    """
     relevant_docs = []

     for doc in documents:
         if query.lower() in doc['content'].lower():
            relevant_docs.append(doc['content'])

    # Return the top K documents (or fewer if less are found)
     return relevant_docs[:top_k]

