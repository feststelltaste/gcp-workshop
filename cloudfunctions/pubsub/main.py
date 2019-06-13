from google.cloud import storage
import base64
import json
import os


def todo_pubsub(event, context):
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    pubsub_message_json = json.loads(pubsub_message)
    print(pubsub_message_json)
    bucket=os.environ['TODO_BUCKET']
    filename = pubsub_message_json.get('id','???') + '.json'
    blob = storage.Client().get_bucket(bucket).blob(filename)
    blob.upload_from_string(pubsub_message, content_type='application/json')

