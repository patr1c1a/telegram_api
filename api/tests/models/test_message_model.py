from rest_framework.test import APITestCase
from api.models import Message


class MessageModelTests(APITestCase):
    def test_create_message(self):
        """
        Tests that a Message can be created with all its fields.
        """
        message = Message.objects.create(
			sender_id=123,
			text="this is a test",
			date="2023-06-09",
			message_id=1,
			post_author="test author",
			views=13,
			peer_id_channel_id=136
        )
        self.assertEqual(message.sender_id, 123)
        self.assertEqual(message.text, "this is a test")
        self.assertEqual(message.date, "2023-06-09")
        self.assertEqual(message.post_author, "test author")
        self.assertEqual(message.views, 13)
        self.assertEqual(message.peer_id_channel_id, 136)
