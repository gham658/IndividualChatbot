# Psychiatrist ChatBot
## COSC 310 Software Engineering Individual Assignment
### Graham Itcush

------

### Local Environment Setup

#### Install Dependencies

`pip install nltk`

`pip install numpy`

`pip install keras`

`pip install tensorflow`

`pip install spacy`

`pip install wikipedia`

`pip install requests`


download spacy model

`python -m spacy download en_core_web_sm`



When first running the program, it may ask you to download certain NTLK packages. The only way I found I could download them was by running the code below:

```python
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()
```

Link to source can be found here: https://stackoverflow.com/questions/38916452/nltk-download-ssl-certificate-verify-failed


#### Train ChatBot

To train the chatbot you can run the file `app/chatbot/train.py`

#### Use ChatBot

To use the chatbot you can run the file `app/chatbot/chatbot_app.py`

------

### API Updates (For Individual Assignment)

#### Wikipedia API
This Chatbot uses the Wikipedia API to provide users with extra information about the mental illness 
they get diagnosed with. After being diagnosed, the user can check the console to find an additional 
summary about their disease taken from Wikipedia.

#### Translate API
This Chatbot also uses Microsoft Azure Translate API, it can take inputs from all of the patterns and responses in the JSON file and translate them to a given language.
