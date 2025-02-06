import unittest
from quick_replies.quick_replies import generate_quick_replies

class TestQuickReplies(unittest.TestCase):
    def test_generate_quick_replies(self):
        chat_history = [
            {"role": "assistant", "content": "您好！有什麼可以幫您？"},
            {"role": "user", "content": "我想知道怎麼退貨。"}
        ]

        replies = generate_quick_replies(chat_history)
        self.assertEqual(len(replies), 5)
        for reply in replies:
            self.assertIsInstance(reply, str)

if __name__ == "__main__":
    unittest.main()
