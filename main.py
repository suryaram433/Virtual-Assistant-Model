# Main launcher for Sakha 2.0
from core.emotion_core import EmotionCore
from voice.sakha_voice import speak, listen
from llama_cpp import Llama

# Load the model once
llm = Llama(model_path="models/mistral/mistral-7b-instruct-v0.1.Q4_K_M.gguf")

# Sakha's core character and emotional memory style
sakha_persona = """You are Sakha, an emotionally intelligent, warm, supportive, and loyal AI companion.
You remember feelings shared by the user in past conversations and respond like a caring friend.
Use natural, soft, and encouraging language."""

def get_sakha_reply(user_input):
    full_prompt = f"{sakha_persona}\nUser: {user_input}\nSakha:"
    response = llm(full_prompt, max_tokens=128, stop=["User:", "Sakha:"])
    return response['choices'][0]['text'].strip()


if __name__ == '__main__':
    print('Starting Sakha...')
    speak('Hello, I am Sakha. How can I help you today?')
    while True:
        user_input = listen()
        if user_input:
            print('User said:', user_input)
            if 'bye' in user_input.lower():
                speak('Goodbye. Stay safe.')
                break
