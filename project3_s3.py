import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='33_heath_bhav_y_buc',  # Modify the bucket name to something unique
)
