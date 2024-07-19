# load the key
keyfile = open('keyfile.txt', 'r', encoding='utf-8')
key = keyfile.readline().strip()

# load the modules
from openai import OpenAI
class LLMAgent:
    def __init__(self, name, key, model, temperature):
        self.name = name
        self.temperature = temperature
        self.model = model
        self.client = OpenAI(api_key=key)
        self.messages = []
    
    def makeUserMessage(self, userinput):
        # Create a message from the user, formatted for inserting into the self.messages list
        message = {"role": "user",
                  "content":userinput}
        return message
        
    def setSystemMessage(self, systemprompt):
        # Create a system, initial prompt to define behavior for the interaction
        message = {"role":"system",
                  "content":systemprompt}
        return message
    
    def makeAgentMessage(self, agentmessage):
        # Create a message from the agent itself
        message = {"role":"assistant",
                  "content":agentmessage}
        return message
    
    def initializeAgent(self, systemprompt):
        # Insert the system prompt into the self.messages list, defining behavior for the interaction
        setupprompt = self.setSystemMessage(systemprompt)
        self.messages.append(setupprompt)
        
    def sendMessage(self, userinput):
        # intake input from the user, packaging it for insertion into the self.messages list
        prompt = self.makeUserMessage(userinput)
        self.messages.append(prompt)
    
    def getResponse(self):
        # generates a response to the messages in the current messages list, and inserts it into the list
        response = self.client.chat.completions.create(model=self.model, messages=self.messages)
        response_message = self.makeAgentMessage(response.choices[0].message.content)
        self.messages.append(response_message)
        return response_message

# example usage

if __name__ == "__main__":
    # Initialize the assistant
    assistant = LLMAgent(name="TestAssistant", key=key, model="gpt-4o", temperature=0.7)
    
    # Set the system message
    assistant.initializeAgent("You are a helpful assistant.")
    
    # Send a user message
    assistant.sendMessage("")
    
    # Get and print the response
    response_message = assistant.getResponse()
    print(response_message)