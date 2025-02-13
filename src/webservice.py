import websocket
import json
import threading

from logger import logger

class WebSocketClient:
    def __init__(self, url, storageClient):
        self.url = url
        self.storageClient = storageClient
        self.ws = websocket.WebSocketApp(self.url,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.on_open = self.on_open

    def on_message(self, ws, message):
        try:
            data = json.loads(message.replace(r"\\", ""))
            if data.get("message") and data.get("type") != "ping":
                ramales_data = data.get("message").get("ramales").replace(r"\\", "")
                ramales_data = json.loads(ramales_data)
                self.storageClient.upload_data(json.dumps(ramales_data, indent=4))

        except Exception as e:
            logger.error(f"Error: {e}")

    def on_error(self, ws, error):
        logger.error(f"Error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        logger.info(f"Connection closed: {close_status_code} - {close_msg}")

    def on_open(self, ws):
        def run(*args):
            logger.info("Connection opened")
            subscription_message = {
                "identifier": "{\"channel\":\"PosicionesChannel\"}",
                "command": "subscribe"
            }
            ws.send(json.dumps(subscription_message))
            while True:
                pass 

        threading.Thread(target=run).start()

    def run(self):
        self.ws.run_forever()

