# FastAPI Monitoring Stack

A comprehensive monitoring solution for FastAPI applications using Prometheus, Grafana, Loki, and Tempo for metrics, logs, and distributed tracing.

![FastAPI Monitoring Stack](Screenshot%202025-08-25%20222055.png)

## 🚀 Features

- **FastAPI Application** with built-in monitoring endpoints
- **Prometheus** for metrics collection and storage
- **Grafana** for visualization and dashboards
- **Loki** for log aggregation
- **Promtail** for log collection
- **Tempo** for distributed tracing
- **OpenTelemetry** integration for automatic instrumentation

## 📋 Prerequisites

- Docker and Docker Compose
- Python 3.8+
- Git

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd fastapi-monitoring
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Quick Start

1. Start the monitoring stack:
```bash
docker-compose up -d
```

2. Start the FastAPI application:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

3. Generate some traffic (optional):
```bash
python generate_traffic.py
```

## 🌐 Access Points

- **FastAPI Application**: http://localhost:8000
  - `/hello` - Main endpoint
  - `/metrics` - Prometheus metrics
  - `/docs` - API documentation

- **Grafana**: http://localhost:3000
  - Username: `admin`
  - Password: `admin`

- **Prometheus**: http://localhost:9090

- **Loki**: http://localhost:3100

- **Tempo**: http://localhost:3200

## 📊 Monitoring Components

### Metrics (Prometheus)
- Request count
- Request latency
- Custom business metrics

### Logs (Loki)
- Application logs
- Access logs
- Error logs

### Traces (Tempo)
- Distributed tracing
- Request flow visualization
- Performance analysis

## 🔧 Configuration

### Prometheus
Configuration file: `prometheus.yml`
- Scrapes metrics from FastAPI application
- Stores time-series data

### Grafana
- Pre-configured dashboards
- Data source connections
- Alerting rules

### Loki
- Log aggregation
- Query interface
- Retention policies

### Tempo
- Distributed tracing backend
- OTLP receiver
- Trace storage

## 📁 Project Structure

```
fastapi-monitoring/
├── app.py                 # FastAPI application
├── generate_traffic.py    # Traffic generator script
├── docker-compose.yml     # Docker services configuration
├── prometheus.yml         # Prometheus configuration
├── promtail-config.yml    # Promtail configuration
├── tempo.yaml            # Tempo configuration
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── .gitignore           # Git ignore rules
```

## 🧪 Testing

The project includes a traffic generator script that sends requests to the FastAPI application:

```bash
python generate_traffic.py
```

This will generate 1000 requests with 200ms intervals to populate metrics, logs, and traces.

## 🔍 Troubleshooting

1. **Port conflicts**: Ensure ports 8000, 3000, 9090, 3100, 3200, 4317, and 4318 are available
2. **Docker issues**: Make sure Docker is running and you have sufficient permissions
3. **Python dependencies**: Verify all packages are installed correctly

## 📈 Next Steps

- Add custom dashboards in Grafana
- Configure alerting rules
- Set up log retention policies
- Add more application endpoints
- Implement custom metrics

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- FastAPI for the web framework
- Prometheus for metrics
- Grafana for visualization
- OpenTelemetry for observability standards
