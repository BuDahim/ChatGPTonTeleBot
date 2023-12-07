import os
import openai

openai.api_key = '----' # OpenAI key


def get_rep(conversation_dict):

  conversation = [
      {'role': 'system', 'content': 'You are Aseel'},

      {'role': 'user', 'content': conversation_dict}]

  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages = conversation,
      max_tokens=1000,
  )
  generated_response = response.choices[0].message['content']
  return generated_response

