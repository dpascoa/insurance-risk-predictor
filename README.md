# Insurance Risk Predictor API

A Flask-based API with an XGBoost model to predict driver insurance risk scores, featuring a modern web interface for user interaction. Built to demonstrate Python, microservices, machine learning, and Docker skills for backend engineering roles.

<div align="center">
  <img width="600" alt="image" src="https://github.com/user-attachments/assets/c5e1a3d6-8a26-44a6-b2bf-29e9126274df" />
</div>

## Features
- **API Endpoints**:
  - `/health` (GET): Checks API status.
  - `/predict_risk` (POST): Predicts risk score based on driver data (age, driving experience, vehicle type, past accidents).
- **Web Interface**: A responsive form at `/` for inputting driver data, displaying results, and showing a history table with a dynamic risk meter.
- **Tech Stack**: Flask, XGBoost, scikit-learn, pandas, pytest, Docker, HTML/CSS/JavaScript.
- **CI**: GitHub Actions for automated testing.
- **Logging**: Built-in logging for debugging.

## Prerequisites
- **Python**: 3.12 (download from [python.org](https://www.python.org/downloads/))
- **Docker**: Install from [docker.com](https://www.docker.com/get-started/)
- **Git**: For cloning and CI (install via [git-scm.com](https://git-scm.com/downloads))
- **Terminal**: Git Bash (Windows) or any terminal (macOS/Linux)

## Setup and Run Locally
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dpascoa/insurance-risk-predictor.git
   cd insurance-risk-predictor
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Installs Flask, XGBoost, scikit-learn, pandas, pytest.

3. **Run the Flask App**:
   ```bash
   python app.py
   ```
   The app runs on `http://localhost:5000`.

4. **Access the Web Interface**:
   - Open `http://localhost:5000/` in a browser.
   - Fill out the form (e.g., Age: 30, Years Driving: 5, Vehicle Type: van, Past Accidents: 1).
   - Submit to see the risk score and a dynamic risk meter; previous predictions appear in a table below.

5. **Test API Endpoints**:
   - **PowerShell**:
     ```powershell
     # Health check
     Invoke-WebRequest -Uri "http://localhost:5000/health" -Method Get | Select-Object -ExpandProperty Content
     # Predict risk
     Invoke-WebRequest -Method POST -Uri http://localhost:5000/predict_risk -Headers @{"Content-Type" = "application/json"} -Body '{"age": 30, "driving_experience_years": 5, "vehicle_type": "van", "past_accidents": 1}' | Select-Object -ExpandProperty Content
     ```
   - **Git Bash**:
     ```bash
     # Health check
     curl http://localhost:5000/health
     # Predict risk
     curl -X POST http://localhost:5000/predict_risk -H "Content-Type: application/json" -d '{"age": 30, "driving_experience_years": 5, "vehicle_type": "van", "past_accidents": 1}'
     ```
   - **Expected Outputs**:
     - `/health`: `{"status":"healthy"}`
     - `/predict_risk`: `{"risk_score":<float>}` (e.g., `0.65`, varies due to XGBoost).

## Setup and Run with Docker
1. **Build the Docker Image**:
   ```bash
   docker build -t insurance-risk-predictor .
   ```

2. **Run the Container**:
   ```bash
   docker run -p 5000:5000 insurance-risk-predictor
   ```

3. **Access**:
   - Web interface: `http://localhost:5000/`
   - API tests: Same as above (PowerShell or Git Bash).

4. **Stop the Container**:
   ```bash
   docker ps  # Get container ID
   docker stop <container_id>
   ```

## Running Tests
1. **Locally**:
   ```bash
   pytest
   ```
   Expected: 3 tests pass (`test_health`, `test_predict_risk_valid`, `test_predict_risk_invalid`).

2. **In Docker**:
   ```bash
   docker exec -it <container_id> bash
   pytest
   exit
   ```

## Continuous Integration
- **GitHub Actions**: The `.github/workflows/ci.yml` file runs tests on every push.
- To use:
  1. Push to GitHub:
     ```bash
     git remote add origin https://github.com/dpascoa/insurance-risk-predictor.git
     git push -u origin main
     ```
  2. Check the Actions tab in your GitHub repo for test results.

## Project Structure
```
insurance-risk-predictor/
├── .github/workflows/ci.yml  # GitHub Actions config
├── templates/index.html     # Web interface
├── app.py                   # Flask API with XGBoost
├── test_app.py              # Pytest suite
├── requirements.txt         # Dependencies
├── Dockerfile               # Docker config
```

## Troubleshooting
- **Empty Response**:
  - Check logs: `docker logs <container_id>` or local Flask output.
  - Ensure `app.py` has `app.run(host='0.0.0.0', port=5000)`.
- **Port Conflict**:
  - Check: `netstat -an | findstr 5000` (Windows) or `lsof -i :5000` (macOS/Linux).
  - Use another port: `docker run -p 5001:5000 insurance-risk-predictor` and test `http://localhost:5001`.
- **Invalid Input**:
  - Ensure `vehicle_type` is `car`, `van`, or `motorcycle`.
- **Dependencies**:
  - Reinstall: `pip install -r requirements.txt`.
  - Rebuild Docker: `docker build -t insurance-risk-predictor .`.
