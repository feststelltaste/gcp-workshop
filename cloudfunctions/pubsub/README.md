# Google Cloud Functions PubSub sample

This sample shows how to write pubsub messages into a cloud storage buckets.

``` 
# create bucket
export TEST_BUCKET=eimer-$RANDOM
gsutil mb -l europe-west2 "gs://$TEST_BUCKET" 

# create topic
gcloud pubsub topics create todo

# deploy function
gcloud functions deploy todo_pubsub --runtime python37 --trigger-topic todo --set-env-vars TODO_BUCKET=$TEST_BUCKET --region europe-west2

# send a test message 
gcloud pubsub topics publish todo --message '{"id": "0a92b9d8-f258-11e8-9aa4-afea51c69f05", "todo": "pubsub test todo", "created_at": "2019-01-01"}'

# check if the file was created
gsutil ls gs://$TEST_BUCKET/
gsutil cp gs://$TEST_BUCKET/0a92b9d8-f258-11e8-9aa4-afea51c69f05.json -

```

https://console.cloud.google.com/storage/browser/



