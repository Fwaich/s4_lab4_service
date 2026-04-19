from prometheus_client import Counter, Histogram, generate_latest
from fastapi import Request
from starlette.responses import Response
import time

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total HTTP requests",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "app_request_duration_seconds",
    "Request latency"
)


def setup_metrics(app):
    @app.middleware("http")
    async def metrics_middleware(request: Request, call_next):
        start_time = time.time()

        response = await call_next(request)

        latency = time.time() - start_time

        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path
        ).inc()

        REQUEST_LATENCY.observe(latency)

        return response

    @app.get("/metrics")
    def metrics():
        return Response(generate_latest(), media_type="text/plain")
