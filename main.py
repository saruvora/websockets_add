import asyncio
import json
import aiofiles
from typing import Dict
from datetime import datetime

from logger import LoggerWebSocket
from server import MathWebSocketServer
from client import MathWebSocketClient

from utils import load_yaml

async def main(config: Dict):
    start_time = datetime.now()

    logger = LoggerWebSocket(config["logging_name"]).get_logger()

    # configure the server and start it
    server = MathWebSocketServer(host=config["server"]["host"], port=config["server"]["port"], logger=logger)
    server_task = asyncio.create_task(server.start()) # starts the server
    await asyncio.sleep(0.5) # added to wait till server starts just to be safe
    
    try:
        # establish client connection
        uri = f"ws://{config["server"]["host"]}:{config["server"]["port"]}"
        client = MathWebSocketClient(uri=uri, logger=logger)

        # load json data asynchronously
        async with aiofiles.open(config["client"]["json_data"], "r") as file:
            content = await file.read()
            number_data = json.loads(content)
        
        # will go through all the list of dictionaries of numbers and operations and call client multiple times   
        for numbers in number_data:
            await client.call_add_function(numbers)
        
    except Exception as e:
        logger.error(f"Exception {e} was raised, client failed !")
    
    await server.destroy() # stops the server
    server_task.cancel()
    end_time = datetime.now()
    print(f"Total time taken: {end_time-start_time}")

if __name__ == "__main__":
    config = load_yaml(file_path="config.yaml")

    if config is None:
        raise TypeError("Config file is not valid")
    
    asyncio.run(main(config))