from django.db import models


class Message(models.Model):
    """Telegram group message"""
    message_id = models.PositiveIntegerField()
    date = models.DateField()
    post_author = models.CharField(max_length=255)
    from_id = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.message_id
