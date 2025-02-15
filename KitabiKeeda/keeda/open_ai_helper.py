import os
from openai import OpenAI

class OpenAIHelper:
    def __init__(self, model='gpt-4o-mini'):
        self.client = OpenAI(
            api_key=OAI_API_KEY,
            # project=OAI_PRJ_KEY,
            organization=OAI_ORG_ID,
        )
        self.model = model

    def stream(self, content='Say this is a test'):
        return self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": content}],
            stream=True,
        )
    
    def create_assistant(self, instructions, name, tools):
        return self.client.beta.assistants.create(
            instructions="You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
            name="Math Tutor",
            tools=[{"type": "code_interpreter"}],
            model=self.model,
            )
    
    def create_vector_store(self, name):
        return self.client.beta.vector_stores.create(name=name)


if __name__ == '__main__':
    oai = OpenAIHelper()
    for chunk in oai.stream():
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
