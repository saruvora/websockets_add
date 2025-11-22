# Math Websocket 
This is a web socket for server and client full-duplex communication to add 2 numbers.

# Files
- Server.py: has the MathWebScoketServer class to implement the server and one can add more functions to it. Make sure to start() and destroy() the server
            to start and stop the connection to the server (See main.py for example). 

- Client.py: has the MathWebScoketClient class to implement the client.

- config.yaml: use this file to configure the server for host and Port and configure the client with an input json of numbers. 

- main.py: runs both the server and the client together can be used either for testing or refence to write your own server and client calls.

## Input file
- numbers.json: this file is used as the input to the client.py has "operation" (which suggests add), "num1" and "num2". One can either keep one of it in it or repeat it as one wills. 

# Requirements
This should be taken care by the pyproject.toml file.
''' 
requires-python = ">=3.13"
dependencies = [
    "aiofiles>=25.1.0",
    "pyyaml>=6.0.3",
    "websockets>=15.0.1",
]
'''

## 1. Create virtual environment 
'''
uv venv
'''

## 2. Activate the environment

### Linux/macOS:
'''
source .venv/bin/activate
'''

### Windows
'''
.venv\Scripts\Activate.ps1
'''

## 3. Install Dependencies 
'''
uv sync
'''