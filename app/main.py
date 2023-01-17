from fastapi import FastAPI
from .utils.send_email import send_email_async


app = FastAPI()


@app.get("/")
def root():
	return "Hello World"


@app.get("/send_email")
async def send_email():
	await send_email_async('Hello World','fnla955@gmail.com',
	{'title': 'Hello World', 'name': 'John Doe'})
	return 'Success'
