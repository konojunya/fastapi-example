from app.schemas.hello import HelloResponse

class HelloService:
    def get_message(self) -> HelloResponse:
        return HelloResponse(message="Hello, World!")