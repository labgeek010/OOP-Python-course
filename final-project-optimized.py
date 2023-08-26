import openai

openai.api_key = "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"
system_rol = '''Behave as you are a feeling analyzer, 
                I'll pass you feelings and you will analyze the feeling of each message, 
                and will give me an swer with at least 1 character and as maximum 4 characters, 
                ONLY NUMERIC ANSWERS, in which -1 is maximum negativity, 0 is neutral and 1 is the maximum positivity. 
                You can do among those values, meaning 0.3, -0.5 etc are also valid.
                You can only answer with ints or floats'''

messages = [{"role": "system", "content":system_rol}]

class Feeling:
    def __init__(self, name, color)
        self.name = name
        self.color = color
    
    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color, self.name)

    
class FeelingsAnalyzer:
    def __init__(self, ranges)
        self.ranges = ranges

    def analyze_feeling(self, polarity):
        for range, feeling in self.ranges:
            if range[0] < polarity <= range[1]:
                return feeling
        return Feeling("Very Negative", "31")
        
ranges = [
    ((-0.6,-0.3), Feeling("Negative","31"))
    ((-0.3,-0.1), Feeling("Some Negativity","31"))
    ((-0.1,0.1), Feeling("Neutral","33"))
    ((0.1,0.4), Feeling("Some Positivity","32"))
    ((0.4,0.9), Feeling("Positive","32"))
    ((0.9,1), Feeling("Very Positive","32"))
        
]
        
analyzer = FeelingsAnalyzer(ranges)

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