from azure.storage.blob import BlobServiceClient
from uuid import uuid4
from datetime import datetime, timedelta

class AzureBlobStorage:
    def __init__(self, account_url, credential, container_name):
        self.service = BlobServiceClient(account_url=account_url, credential=credential)
        self.container_name = container_name

    def upload_data(self, data):
        container_client = self.service.get_container_client(self.container_name)
        try:
            container_client.create_container()
        except Exception as e:
            if "ContainerAlreadyExists" not in str(e):
                raise
        now = datetime.now() - timedelta(hours=3)
        blob_name = f"posiciones/{now.year}/{now.month}/{now.day}/{uuid4()}.json"
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(data, overwrite=False)