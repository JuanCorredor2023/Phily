Phily - Spanish Virtual Assistant

Description
Phily is an AI-based virtual assistant that engages in conversations in Spanish using voice. It employs natural language processing (NLP) and speech synthesis to understand and respond to user inputs, providing an interactive and user-friendly experience.

Features
- **Voice Recognition in Spanish**: Understands spoken Spanish commands and queries.
- **AI-Generated Responses**: Delivers context-aware and intelligent replies.
- **Voice Synthesis for Replies**: Converts text responses into natural-sounding speech.
- **Continuous Learning**: Improves performance and accuracy through ongoing interaction.

Requirements
- **Python 3.x**
- **Libraries**: 
  - `random`
  - `json`
  - `unicodedata`
  - `os`
  - `time`
  - `playsound`
  - `speech_recognition`
  - `gtts`
  - `torch`
  - `nltk`

Install the necessary libraries using the command:
```bash
pip install -r requirements.txt
```

Usage
1. **Setup**: Make sure all required libraries are installed.
2. **Run Phily**: Execute the `chat.py` script to start the assistant.
3. **Interact**: Speak clearly in Spanish. Phily will respond vocally. To end the conversation, say 'chao'.

```bash
python chat.py
```

File Overview
- **chat.py**: Main script to start the assistant.
- **intents.json**: Knowledge base containing conversation patterns.
- **model.py**: Neural network model for understanding and generating responses.
- **nltk_utils.py**: Utilities for NLP tasks like tokenization and stemming.
- **data.pth**: Trained model data used by the assistant.

Author
Juan Andrés Corredor