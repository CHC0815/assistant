# Home Voice Assistant

## What is it

This project aims to provide a voice assistant that executes your commands to control Home Assistant.

It uses the KaldiRecognizer from Vosk to perform speech recognition.

A simple text-based lookup parser then parses the voice command. If it fails to find an entity and a state (on, off) a gpt-3.5-turbo model is asked for some function_calls.

## Requirements

Have a Home Assistant server running with API and HTTP enabled.

## How to use

1. Clone this Repo
2. Run ```pip3 install -r requirements.txt```
3. Create an openai API key and set it as an environment variable
4. Create a config.ini and populate it
5. Run ```python3 main.py```
6. Say the assistant's activation word
7. Say voice command





