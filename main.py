import openai 

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]

    )
    return response.choices[0].message.content.strip()
if __name__ == "__main__":
    while True:
        user_input = input("you:")
        if user_input.lower() in ["quit","exit","bye"]:
            break 
        response = chat_with_gpt(user_input)
        print("chatbot:",response)
