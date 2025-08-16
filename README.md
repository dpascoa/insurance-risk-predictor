# Insurance Risk Predictor API

A simple Python Flask microservice that uses XGBoost to predict driver risk scores for insurtech applications. Demonstrates backend API design, ML integration, testing, and Docker deployment.

## Why This Project?
Inspired by Zego's focus on data-driven insurance. It showcases my skills in Python, microservices, ML (XGBoost), and cloud-ready architectures.

## Setup
1. Clone repo: `git clone ...`

## Run with Docker
1. Build: `docker build -t risk-predictor .`
2. Run: `docker run -p 5000:5000 risk-predictor`
3. Test: POST to `http://localhost:5000/predict_risk` with JSON.

## Decisions
- Used Flask for lightweight API; could scale to Django.
- XGBoost for efficient ML predictions.
- Added tests for reliability.
- Docker for easy deployment (e.g., to AWS Lambda/ECS).

## Improvements
- Integrate real AWS (S3 for data, Lambda for serverless).
- Add event-driven webhook for telemetry inputs.
- Expand ML with TensorFlow for deeper models.

Deployed demo: [Link if you deploy]