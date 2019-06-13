# Google Cloud Functions ImageMagick sample

This sample shows you how to blur an image using ImageMagick in a Storage-triggered Cloud Function.

``` 

# create bucket
export TEST_BUCKET=eimer-$RANDOM
gsutil mb "gs://$TEST_BUCKET"

# enable vision api https://console.developers.google.com/apis/api/vision.googleapis.com/overview
# deploy function
gcloud functions deploy blur_offensive_images --trigger-bucket=$TEST_BUCKET --set-env-vars BLURRED_BUCKET_NAME=$TEST_BUCKET --runtime python37

# Upload an offensive image to the Storage bucket, such as this image of a flesh-eating zombie: https://cdn.pixabay.com/photo/2015/09/21/14/24/zombie-949916_1280.jpg
gsutil cp zombie-949916_1280.jpg gs://$TEST_BUCKET/

gsutil ls gs://$TEST_BUCKET/

```

https://console.cloud.google.com/storage/browser/