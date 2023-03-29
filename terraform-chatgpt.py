import requests
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to the OpenAI API")
parser.add_argument("file_name", help="Name of the file to save Terraform script")
args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")

request_headers = {
    "Content-Type": "application/json",  # this line is specifying the format of the content in our header, this case being json
    "Authorization": "Bearer " + api_key # authorization when sending a request to a protected source/endpoint
}

request_data = {
    "model": "text-davinci-003", # this is the model of chatGPT we are using
    "prompt": f"Write terraform script for {args.prompt}. Provide only code, no text.", # this is the prompt you would type into chatGPT when using it
    "max_tokens": 100, # do not exceed this number of tokens in chatGPT's response
    "temperature": 0   # the closer to 0 the more precise, the closer to 1 the more creative the response is
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200: # If response OK print json content response
    response_text = (response.json())["choices"][0]["text"]
    with open(args.file_name, "w") as file: # finds a file called specified in our argument, if it doesn't exist it creates one and opens it in write mode
        file.write(response_text) # now that we are in write mode, write our json content response to the file
else: # If response not OK return response status code
    print(f"Request failed with status code: {str(response.status_code)}")