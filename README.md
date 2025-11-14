# Console_Chat_AI_HuggingFace

- We are importing the requests library to send HTTP requests to Hugging Face's API.
- It helps us communicate with the cloud model just like a browser or app does.
- Falcon-7B-Instruct mode
- The headers variable is a dictionary in Python. (key-value pairs)
- Bearer is a keyword that tells the server you're using token-based authentication.
- It sends the prompt as a JSON payload to the API using POST.
- 200 is the HTTP status code that means "OK" or "Success"
- This takes the raw JSON reply from the API and converts it into a Python object (usually a list or dictionary).
- We’re accessing the first item in the list
