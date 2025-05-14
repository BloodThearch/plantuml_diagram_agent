from openai import OpenAI

class Llama3Instance:
  def __init__(self,key: str):

    client = OpenAI(
      base_url = "https://integrate.api.nvidia.com/v1",
      api_key = key
    )
    self.client = client

  def sendSingleMessage(self,msg: str):
    completion = self.client.chat.completions.create(
      model="meta/llama-3.1-8b-instruct",
      messages=[{"role":"user","content":msg}],
      temperature=0.2,
      top_p=0.7,
      max_tokens=1024,
      stream=True
    )

    result = ""
    for chunk in completion:
      if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
        result = result + chunk.choices[0].delta.content
    return result

