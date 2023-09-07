# import all reletive libraries
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
from utils.configs import ConfigManager


# load configManager
config_manager = ConfigManager()



def generate_text(message):
  
  api_key = config_manager.get_api_key()

# Here use chatOpenAI model
  chat = ChatOpenAI(
    openai_api_key=api_key, 
    model="gpt-3.5-turbo"
    )


# Here use prompt
  messages = [
    SystemMessage(content="You are a user assistant to Translate the user input into Hinglish, identifying any complex words or phrases in English and rendering them in Hinglish so that they are natural and comprehensible even to someone who is not a native Hindi speaker. ### Hinglish means a mixture of the languages Hindi and English, especially the type of English used by speakers of Hindi."),
    HumanMessage(content=message)
]

  result = chat(messages)
  return result.content