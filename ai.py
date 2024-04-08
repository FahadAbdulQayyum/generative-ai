from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion
from dotenv import load_dotenv, find_dotenv

_ : bool = load_dotenv(find_dotenv())

print(_)

client : OpenAI = OpenAI();

# # # # # # # # # # # # # # # # # # # # # # # # # # 

# stream: ChatCompletion = client.chat.completions.create(
#     model="gpt-3.5-turbo-1106",
#     message=[{"role": "user", "content": "Say this is test"}],
#     stream=True,
# )

# for part in stream:
#     print(part.choices[0].delta.content or "")

# # # # # # # # # # # # # # # # # # # # # # # # # # 

def chat_completion(prompt: str) -> str:
    response: ChatCompletion = client.chat.completions.create(
        messages=[
         {
             "role": "user",
             "content": prompt,
         }   
        ],
        model="gpt-3.5-turbo-1106",
    )

    return response.choices[0].message.content

answer: str = chat_completion("What is 1+1?")

print(answer)

# 