from django.db import models


class Message(models.Model):
    """Telegram group message"""
    sender_id = models.PositiveIntegerField()
    text = models.CharField(max_length=255)
    date = models.DateField()
    message_id = models.PositiveIntegerField()
    post_author = models.CharField(max_length=255)
    views = models.PositiveIntegerField()
    peer_id_channel_id = models.PositiveIntegerField()

    def __str__(self):
        return self.message_id
