import time
from fastapi import Request, Response

async def timingMiddleWare(request: Request, call_next):
    start_time = time.perf_counter
    response: Response = await call_next(request)
    response.headers["X-Process-Time"] = f"{time.perf_counter() - start_time:.4f} seconds"
    return response