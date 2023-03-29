# GPT-Script-Automation
This repository contains code for integrating with the OpenAI ChatGPT API. This API allows you to generate text based on a prompt or question. In this case we are utilizing ChatGPT to automate writing simple Python and Terraform scripts.
## Getting Started
To use this code, you'll need to have an OpenAI API key. If you don't already have one, you can create an account and generate a key on the [OpenAI platform](https://beta.openai.com/signup/).
Once you have your API key, you'll need to set it as an environment variable in the working directory of the applications. To do this, run the following command, replacing "put_api_key_here" with your actual API key:
export OPENAI_API_KEY=put_api_key_here
## Usage
This repository contains two examples of how to use the OpenAI ChatGPT API with Python and Terraform.
### Python Automation
To use the Python automation script, run the following command in your terminal, replacing "print hello world" with your own prompt and "hello-world.py" with the desired output file:
```bash
python3 python-chatgpt.py "print hello world" "hello-world.py"
This will generate text based on your prompt and write the output to the specified file.
### Terraform Automation
To use the Terraform automation script, run the following command in your terminal, replacing "provision s3 bucket" with your own prompt and "s3.tf" with the desired output file:
python3 terraform-chatgpt.py "provision s3 bucket" "s3.tf"
This will generate text based on your prompt and write the output to the specified file.
## Conclusion
That's it! You should now be able to use the OpenAI ChatGPT API with Python and Terraform. If you have any questions or issues, please feel free to create an issue on this repository.
