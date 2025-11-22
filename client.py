import websockets
import json
from typing import Dict

from logging import Logger

class InvalidServerResponse(Exception):
    """Raised when server sends a response without a result field."""
    pass

class MathWebSocketClient:

    def __init__(self, uri: str, logger: Logger):
        self.uri = uri
        self.logger = logger
        

    async def call_add_function(self, json_data: Dict) -> None:
        """ establish connection to server and send the numbers for addition """
        async with websockets.connect(self.uri) as websocket:

            self.logger.info("Client Connected !!")
            request = json.dumps(json_data)
            await websocket.send(request)
            self.logger.info("Sent data to Server !!")
            try:
                response = await websocket.recv()
                if "Result" in response:
                    self.logger.info(f"Response from Server: {response}")
                else:
                    self.logger.error(f"Error response from server: {response}")
                    raise InvalidServerResponse(f"Error raise from Server: {response}")
                
            except InvalidServerResponse as e:
                self.logger.error(e)

