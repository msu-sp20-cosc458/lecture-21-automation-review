import unittest
import functions

class ChatBotResponseTest(unittest.TestCase):
    def test_not_command(self):
        response = functions.get_chatbot_response("Purple")
        self.assertEquals(response, "")
        
    def test_add_command(self):
        response = functions.get_chatbot_response(''' put something here ''')
        self.assertEquals(''' put something here''')

if __name__ == '__main__':
    unittest.main()
