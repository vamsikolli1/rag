from flask import Flask, request, jsonify # type: ignore
import retrieve_generate 
import feed_llm_generate

app=Flask(__name__)

@app.route('/answer', methods=['POST'])
def main():
    # Define the query
    #query = "What is the Eiffel Tower?"
    query=request.get_json()['query']
    # Step 1: Search for relevant documents from the sample dataset
    retrieved_docs = retrieve_generate.search_documents(query, documents, top_k=3)
    
    if not retrieved_docs:
        print("No relevant documents found.")
        return

    # Step 2: Generate an answer using GPT-2 or GPT-3
    print("\nRetrieving relevant documents:\n")
    for doc in retrieved_docs:
        print(f"- {doc}")

    print("\nGenerating answer using GPT-2:\n")
    # Using GPT-2 (choose this if you want to run locally)
    answer_gpt2 = feed_llm_generate.generate_answer(query, retrieved_docs)
    print(answer_gpt2)
    return answer_gpt2 

    # Alternatively, you can use GPT-3 (uncomment the following line to use GPT-3)
    # print("\nGenerating answer using GPT-3:\n")
    # answer_gpt3 = generate_answer_with_gpt3(query, retrieved_docs)
    # print(answer_gpt3)

# run the flask app with this file 

if __name__ == "__main__":
    app.run()