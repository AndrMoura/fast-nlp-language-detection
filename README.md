# Fast text language detection 

This open-source project delivers an efficient language detection system built on FastAPI 🚀. It uses a Google's CLD2. It is an ideal solution for applications requiring blazing fast and reliable language detection without the need for GPU hardware.

This project functions as the backend supporting the  [lang detect plugin](https://github.com/AndrMoura/ph-langdetect-plugin) designed for use with [PostHog-LLM](https://github.com/postlang/posthog-llm).


# Install from source
```bash
git clone https://github.com/AndrMoura/ph-langdetect-plugin.git
cd ph-langdetect-plugin
pip install -r requirements.txt
```


# Run locally

Run the following command to start the server (from the root directory):

```bash
chmod +x ./run.sh
./run.sh
```

Check `config.py` for more configuration options.


# Run with Docker

Run the following command to start the server (the root directory):

```bash
docker build --tag langdetect .
docker run --network=postlang --network-alias=langdetect -p 9612:9612 -it langdetect
```

The network and the network alias are used to allow PostHog-LLM to communicate with the language detection service.
Since PostHog-LLM is running in a docker container, we connect the two services by adding them to the same network for *fast* and *reliable* communication.

# Example call
```bash
curl -X 'POST' \
  'http://localhost:9612/conversation_language_detect_plugin' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "llm_input": "I like you very very much so",
  "llm_output": "Qui veut aller au ciné ? Qui veut aller au ciné ?. Oui Oui"
}'
```