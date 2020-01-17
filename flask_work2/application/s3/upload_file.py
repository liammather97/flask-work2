def upload_file(file_name, bucket):

    object_name = file_name
    s3_client = boto3.client('s3')
    repsonse = s3_client.upload_file(file_name, bukcet, object_name)

    return response
