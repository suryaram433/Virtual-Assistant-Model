# Emotional logic placeholder
class EmotionCore:
    def __init__(self):
        self.emotion = 'neutral'

    def analyze(self, text):
        # Dummy emotion switch
        if 'sad' in text:
            self.emotion = 'empathetic'
        elif 'happy' in text:
            self.emotion = 'cheerful'
        else:
            self.emotion = 'neutral'
        return self.emotion
