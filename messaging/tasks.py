from django.utils import timezone
from firebase_admin import messaging

from messaging.celery import app


@app.task
def deliver_notification(table_name, value, change_type="SAVE"):
    topic = 'highScores'
    data = {
        'table_name': table_name,
        'value': value,
        'change_type': change_type,
        'time': str(timezone.now()),
    }
    # See documentation on defining a message payload.
    message = messaging.Message(
        data=data,
        topic=topic,
    )

    # Send a message to the devices subscribed to the provided topic.
    response = messaging.send(message)
    return response
