from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion
from dotenv import load_dotenv, find_dotenv

_ : bool = load_dotenv(find_dotenv())

client : OpenAI = OpenAI()

def chat_completion(prompt: str) -> str :
    print('prompt:', prompt)
    response : ChatCompletion = client.chat.completions.create(
        messages=[
            {
                "role" : "user",
                "content" : prompt,
            }
        ],
        model="gpt-3.5-turbo-1106",
    )

    print('response', response)

    return response.choices[0].message.content

question : str = input("Enter your prompt?\t")

answer : str = chat_completion(question)
# answer : str = chat_completion("Where is Balochistan?")

print("answer:", answer)