import os 
from dotenv import load_dotenv

from src.webservice import WebSocketClient
from src.storage import AzureBlobStorage

load_dotenv()

if __name__ == "__main__":
    STORAGE_ACCESS_KEY = os.getenv("STORAGE_ACCESS_KEY")
    STORAGE_ACESS_URL = os.getenv("STORAGE_ACESS_URL")
    STORAGE_CONTAINER_NAME = os.getenv("STORAGE_CONTAINER_NAME")

    storage_client = AzureBlobStorage(STORAGE_ACESS_URL, STORAGE_ACCESS_KEY, STORAGE_CONTAINER_NAME)

    websocket_url = "wss://tucubondismt.gob.ar/cable"
    client = WebSocketClient(websocket_url, storage_client)
    client.run()