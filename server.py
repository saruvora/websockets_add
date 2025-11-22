import json

from websockets.asyncio.server import serve

from logging import Logger

class MathWebSocketServer():
    def __init__(self, host: str, port: int, logger: Logger):
        self.host = host
        self.port = port
        self.logger = logger
        
    async def handler(self, websocket: any) -> None:
        """ This will handle the input from client and process the data
        for the required math operation """
        
        try:
            async for message in websocket:
                self.logger.info("Mesage start: %s", message)
                json_data = json.loads(message)
                operation = json_data.get("operation").lower()
                num1 = json_data.get("num1")
                num2 = json_data.get("num2")

                if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
                    if operation == "add":
                        self.result = self._add(num1=num1, num2=num2)
                        await websocket.send(json.dumps({"Result": self.result}))
                    else:
                        await websocket.send(json.dumps({"Error": "Invalid Operation"}))
                else:
                    self.logger.error("Error: check the data type of num1 and/or num2")
                    await websocket.send(json.dumps({"Error": "Invalid datatype"}))
        except Exception as e:
            self.logger.error(f"Server handler error {e} raised")
            

    async def start(self) -> None:
        """ Start the server """
        self.server = await serve(
            self.handler, 
            self.host, 
            self.port, 
            reuse_address=True, 
            reuse_port=True
        )
        
        await self.server.serve_forever()
        self.logger.info("Server started !!")

    async def destroy(self) -> None:
        """ Kill/Close/Destroy the connection to the server """
        if self.server:
            self.server.close() 
            
            # Wait for the server to close entirely
            await self.server.wait_closed()
            
            # Clear the reference to the server
            self.server = None 
            self.logger.info("Server destroyed successfully.")
        else:
            self.logger.warning("Attempted to destroy server, but no running instance was found.")

    def _add(self, num1: int, num2: int) -> int:
        """ Math operation to add 2 numbers """
        return num1 + num2


