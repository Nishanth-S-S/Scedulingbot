

import openai


openai.api_key = "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"


messages = []
system_msg = """You are a scheduiling bot that helps C2 education of charlotte schedule. You must ask for the Student NAME, Tutor name, Subject: Number of hours: Hourly rate. At one time totors can only handle 3 students. If they ask you must show them all the people who have been scheduled. You have to ask your question one by one. It is not just 100 hours """
messages.append({"role": "system", "content": system_msg})


print("Hello, I'm Zen 👋, an AI scheduling bot that will help you schedule.")
print("Would you like to book someone an appointment today or would you like to see all the appointments.")
while input != "quit":
   message = input()
   messages.append({"role": "user", "content": message})
   response = openai.ChatCompletion.create(
       model="gpt-3.5-turbo",
       messages=messages)
   reply = response["choices"][0]["message"]["content"]
   messages.append({"role": "assistant", "content": reply})
   print("\n" + reply + "\n")
