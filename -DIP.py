# class Dictionary:
#     def verify_word(self, word):
#         #logic to verify words
#         pass

# class OrtographicCorrector:
#     def __init__(self):
#         self.dictionary = Dictionary()

#     def correct_text(self, text)
#         #use the dictionary to correct the text
#         pass
        
from abc import ABC, abstractmethod

class OrtographicVerifier(ABC)
    @abstractmethod
    def verify_word(self, word):
        pass

class Dictionary(OrtographicVerifier):
    def verify_word(self, word):
        # logic to verify words if it is in the dictionary
        pass

class OnlineService(OrtographicVerifier):
    def verify_word(self, word):
        return super().verify_word(word)

class OrtographicCorrector:
    def __init__(self,verifier):
        self.verifier = verifier
    
    def correct_text(self, text):
        # we use the verifier to correct text