from fastapi import FastAPI
import requests
import boto3

app = FastAPI()

AWS_SECRET_KEY_ID = "AKIAFAKEKEY1234567890"
AWS_SECRET_KEY = "fakeSuperSecretKeyForDemoOnly123!"

def get_external_data():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    return response.json()

def connect_to_aws():
    print(f"Conectando à AWS com key_id={AWS_SECRET_KEY_ID} e secret={AWS_SECRET_KEY}")
    return True

def list_s3_objects():
    s3 = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name="us-east-1"
    )
    bucket_name = "my-demo-bucket"    
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        objects = [obj["Key"] for obj in response.get("Contents", [])]
    except Exception as e:
        objects = [f"Erro simulando bucket: {str(e)}"]
    
    return objects

@app.get("/data")
def read_data():
    connect_to_aws() 
    data = get_external_data()
    print(list_s3_objects())
    unused_var = 123
    return {"message": data}
