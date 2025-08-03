from llama_cpp import Llama

llm = Llama(model_path="C:/llm/models/mistral/mistral-7b-instruct-v0.1.Q4_K_M.gguf")

response = llm("Q: What is the capital of France?\nA:", max_tokens=32)
print(response['choices'][0]['text'].strip())
