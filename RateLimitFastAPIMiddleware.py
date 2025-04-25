import time
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import asyncio


class TokenBucket:
    def __init__(self, rate: int, capacity: int):
        self.rate = rate  # сколько токенов добавляется в секунду
        self.capacity = capacity  # максимальный размер ведра
        self.tokens = capacity
        self.timestamp = time.time()

    def consume(self, tokens: int = 1) -> bool:
        now = time.time()
        elapsed = now - self.timestamp # Пополнить ведро новыми токенами
        self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)
        self.timestamp = now
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False


class RateLimiterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, rate=5, capacity=10):
        super().__init__(app)
        self.rate = rate
        self.capacity = capacity
        self.buckets = {}  
        self.lock = asyncio.Lock()

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host  

        async with self.lock:
            bucket = self.buckets.get(client_ip)
            if bucket is None:
                bucket = TokenBucket(self.rate, self.capacity)
                self.buckets[client_ip] = bucket

            allowed = bucket.consume()

        if not allowed:
            return JSONResponse(
                status_code=429,
                content={"detail": "Too Many Requests. Please slow down."},
            )

        response = await call_next(request)
        return response
