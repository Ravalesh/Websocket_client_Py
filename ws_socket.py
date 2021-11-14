from websocket import create_connection
import json
import random, time


ws = create_connection('ws://localhost:8000/ws/polData/')

for i in range(1000):
    time.sleep(3)
    ws.send(json.dumps({'value': random.randint(1,100)}))