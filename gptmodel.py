import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-4o"
        messages = [{"role": "user", "content": prompt}]
        )
    

    return response.choices[0].message.content.scrip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
