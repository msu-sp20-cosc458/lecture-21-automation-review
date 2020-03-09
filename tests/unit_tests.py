import unittest
import functions


class ChatBotResponseTest(unittest.TestCase):
    def test_not_command(self):
        response = functions.get_chatbot_response("Purple")
        self.assertEqual(response, "")
        self.assertEqual(response, "")
        
    def test_add_command(self):
        response = functions.get_chatbot_response("!! add 2 4")
        self.assertEqual(response, 6)

if __name__ == '__main__':
    unittest.main()
