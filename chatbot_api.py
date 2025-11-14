import requests

API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"   

headers = {
    "Authorization": "Bearer -HuggingFace Access Tocken-"   
}

def query(question):
    prompt = f"Answer the following question: {question}"
    payload = {
        "inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)   

    if response.status_code == 200:   
        result = response.json()      
        return result[0]["generated_text"]  
    else:
        print("Error:", response.status_code, response.text)
        return "Sorry, I couldn't generate a response."

print("Ready to chat or Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Bye!")
        break
    response = query(user_input)
    print("Bot:", response)
