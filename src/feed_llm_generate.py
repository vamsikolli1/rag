from transformers import GPT2LMHeadModel, GPT2Tokenizer 

# load GPT-2 model and tokenizer from hugging face 
tokenizer=GPT2Tokenizer.from_pretrained('gpt2')
model=GPT2LMHeadModel.from_pretrained('gpt2')


def generate_answer(query, retrieved_docs):
    # Combine the query with the retrieved documents
    context = " ".join(retrieved_docs)
    input_text = query + " " + context

    # Tokenize the input text
    inputs = tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True)
    
    # Generate the response using GPT-2
    outputs = model.generate(inputs['input_ids'], max_length=150, num_return_sequences=1)

    # Decode the generated response
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer