import requests

API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"   

headers = {
    "Authorization": "Bearer -HuggingFace Access Tocken-"   # add your acess Tocken
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


# We are importing the requests library to send HTTP requests to Hugging Face's API.
# It helps us communicate with the cloud model just like a browser or app does.
# Falcon-7B-Instruct mode
# The headers variable is a dictionary in Python. (key-value pairs)
# Bearer is a keyword that tells the server you're using token-based authentication.
# It sends the prompt as a JSON payload to the API using POST.
# 200 is the HTTP status code that means "OK" or "Success"
# This takes the raw JSON reply from the API and converts it into a Python object (usually a list or dictionary).
# We’re accessing the first item in the list