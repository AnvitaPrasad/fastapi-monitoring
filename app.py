from fastapi import FastAPI
from prometheus_client import Counter, Histogram, generate_latest
from fastapi.responses import PlainTextResponse
import time
import random
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.resources import Resource
app=FastAPI()


REQUEST_COUNT=Counter("request_count","Total number of requests")
REQUEST_LATENCY=Histogram("request_latency","Request latency in seconds")

#Naming the service
resource = Resource(attributes={
    "service.name": "fastapi"
})



#Tracing Setup
trace.set_tracer_provider(TracerProvider(resource=resource))
tracer_provider = trace.get_tracer_provider()
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4318/v1/traces")
tracer_provider.add_span_processor(BatchSpanProcessor(otlp_exporter))

# Instrument FastAPI + requests
FastAPIInstrumentor.instrument_app(app)
RequestsInstrumentor().instrument()

@app.get("/hello")
def read_root():
    start_time=time.time()

    REQUEST_COUNT.inc()
    message={"message":"Hello,World!"}

    # Simulate work (random 10–100 ms)
    time.sleep(random.uniform(0.01, 0.1))

    latency=time.time()-start_time
    REQUEST_LATENCY.observe(latency)

    return message
@app.get("/metrics",response_class=PlainTextResponse)
def metrics():
    return generate_latest().decode('utf-8')