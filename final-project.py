# Feelings Analyzer Chatbot

# In this project, you must develop a chatbot in Python, which will allow us to tell him something,
# the chatbot should take this input and understand it, it must analize the feeling and 
# it should reply to us leeting us know more about the feeling.

# This project will grant you the opportunity to work with multiple aspects of the OOP, modules, API and data analis

#from textblob import TextBlob

# class FeelingsAnalizer:
#     def analyze_feeling(self, text):
#         analysis = TextBlob(text)
#         if analysis.sentiment.polarity > 0:
#             return "positive"
#         elif analysis.sentiment.polarity == 0:
#             return "neutral"
#         else:
#             return "negative"

# analyzer = FeelingsAnalizer()
# result = analyzer.analyze_feeling("I am very cheerful")
# print(result)

import openai

openai.api_key = "apikey"
system_rol = '''Behave as you are a feeling analyzer, 
                I'll pass you feelings and you will analyze the feeling of each message, 
                and will give me an swer with at least 1 character and as maximum 4 characters, 
                ONLY NUMERIC ANSWERS, in which -1 is maximum negativity, 0 is neutral and 1 is the maximum positivity. 
                You can do among those values, meaning 0.3, -0.5 etc are also valid.
                You can only answer with ints or floats'''

messages = [{"role": "system", "content":system_rol}]

class FeelingsAnalyzer:
    def analyze_feeling(self, polarity):
        if polarity > -0.8 and polarity <= -0.3:
            return "\x1b[1;31m" + "Negativity" + "\x1b[0;37m"
        elif polarity > -0.3 and polarity < -0.1:
            return "\x1b[1;31m" + "Some Negativity" + "\x1b[0;37m"
        elif polarity > -0.1 and polarity <= 0.1:
            return "\x1b[1;33m" + "Neutral" + "\x1b[0;37m"
        elif polarity >= 0.1 and polarity <= 0.4:
            return "\x1b[1;32m" + "Some Positivity" + "\x1b[0;37m"
        elif polarity >= 0.4 and polarity <= 0.9:
            return "\x1b[1;32m" + "Positivity" + "\x1b[0;37m"
        elif polarity > 0.9:
            return "\x1b[1;32m" + "Very Positive" + "\x1b[0;37m"
        else:
            return "\x1b[1;31m" + "Very Negative" + "\x1b[0;37m"
        
analyzer = FeelingsAnalyzer()

while True:
    user_prompt = input("\x1b[1;33m" + "\n Tell me something: " + "\x1b[0;37m")
    messages.append({"role": "user", "content":user_prompt})

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        max_tokens = 8
    )

    answer = completion.choices[0].message["content"]
    messages.append({"role": "assistant", "content": answer})

    feeling = analyzer.analyze_feeling(float(answer))
    print(feeling)
