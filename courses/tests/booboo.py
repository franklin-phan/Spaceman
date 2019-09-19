compliments = ['coolio', 'smashing', 'neato', 'fantabulous']

def get_compliment():
    compliment = compliments[0]
    return f'Hello there, user! You are so {compliment}!'

class ComplimentTests(unittest.TestCase):
    def test_get_compiment(self):
        self.assertEqual(get_compliment(),'Hello there, user! You are so neato')