import websocket
import json
import threading
import logging

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
                ramales_data = data["message"]["ramales"].replace(r"\\", "")
                ramales_data = json.loads(ramales_data)
                self.storageClient.upload_data(json.dumps(ramales_data, indent=4))

        except Exception as e:
            logging.error(f"Error: {e}")

    def on_error(self, ws, error):
        logging.error(f"Error: {error}")


    def on_close(self, ws, close_status_code, close_msg):
        pass

    def on_open(self, ws):
        def run(*args):
            pass
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

