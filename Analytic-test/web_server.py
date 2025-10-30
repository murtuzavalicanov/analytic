from fastapi import FastAPI
from consumer import message_queue

app = FastAPI()

@app.get("/")
def read_messages():
    messages = list(message_queue.queue)
    return {"messages": messages}
