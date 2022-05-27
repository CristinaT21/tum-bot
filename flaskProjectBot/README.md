# Facebook Messenger Chatbot

## Components / Mechanisms 
- Web server developed using Flask
- Requests sent with the requests library
- HTTPS connection to the local instance via ngrok
- Additional packages:
  - Conversational model: The implementation of the conversational data models based on movie dialogs corpus.
  - Page scrapper: Module used for scrapping web pages for information.
  - Integrations: Package that contains python modules used for third-party integrations. 

## Running the project
- flask run --host=localhost --port=desired_port
- ngrok http desired_port
- Configure the webhooks in facebook application to use the ngrok endpoint

## Authorization
- Generate the verification token by running: openssl rand -base64 32