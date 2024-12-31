# from django.db import models

# # Create your models here.


from django.db import models

class MQTTMessage(models.Model):
    topic = models.CharField(max_length=255)
    payload = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Topic: {self.topic}, Payload: {self.payload[:50]}"
