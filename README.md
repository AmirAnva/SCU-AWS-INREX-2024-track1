# VisionFlow AI

## 1. Introduction
VisionFlow AI is a traffic-monitoring demo that combines a React + Vite front end with a Flask back end. The front end loads Google Maps and shows INRIX traffic cameras within a bounding box. When a camera marker is selected, the back end fetches the latest image and invokes AWS Bedrock (Claude 3 Sonnet) to analyze congestion, car accidents, and weather, returning a structured JSON response. A simple notification service is also included to email users within a radius of an incident based on coordinates stored in MySQL.

Key files:
- Frontend: `vite-project/src/map.jsx` (map, markers, data fetching), `vite-project/src/App.jsx`
- Backend: `test/aws/server.py` (Flask API), `test/aws/bedrock.py` (image analysis with Bedrock)
- Utilities: `util/app.py` (notification service), `util/service/send_email.py` (Gmail SMTP), INRIX API samples under `test/camera_api`

Distance is computed using the Haversine formula (see `vite-project/src/map.jsx` → `calcCrow`).

## 2. Features
- Interactive map and camera markers
  - Fetch cameras in a geographic box from INRIX: `test/aws/server.py` → `/cameras`
  - Filter cameras within 1 mile of the current point and display on Google Maps, including a “Current Location” marker: `vite-project/src/map.jsx`
- Live image + AI interpretation
  - On marker click, fetch image and analysis (Congestion/Car Accident/Weather): `vite-project/src/map.jsx` → `test/aws/server.py` → `test/aws/bedrock.py`
  - Image source via INRIX camera image API: `test/aws/get_byte_image.py`
- User-radius email notifications
  - Query users within a radius from incident coordinates and send email: `test/aws/server.py` and `util/app.py`, with email via `util/service/send_email.py`
  - Database DDL and seed: `setup_database.sql`
- Environment & configuration
  - Backend env example: `.env.example`
  - Frontend env example: `vite-project/.env.example`

Sample analysis JSON (from `test/aws/bedrock.py`):
```json
{
  "Id": "62219",
  "Image": "<base64>",
  "Status": 200,
  "Content": {
    "Congestion": 1,
    "Car Accident": 0,
    "Weather": "rainy"
  }
}
```

## 3. Project Structure
- Frontend (Vite + React)
  - Entrypoints & pages
    - `vite-project/index.html`
    - `vite-project/src/main.jsx`
    - `vite-project/src/App.jsx`
  - Map and data
    - `vite-project/src/map.jsx` (Google Maps, markers, `GetData`, `calcCrow`)
  - Others
    - `vite-project/src/Navbar.jsx`
    - `vite-project/vite.config.js`
    - `vite-project/package.json`
    - `vite-project/.env.example`
- Backend (Flask API)
  - Main service
    - `test/aws/server.py` (routes: `/cameras`, `/<id>`, notification APIs)
    - INRIX helpers: `test/aws/Token.py`, `test/aws/CamerasBox.py`, `test/aws/CameraImage.py`
    - Image analysis: `test/aws/bedrock.py`, `test/aws/get_byte_image.py`
  - Alternative/simple notification service: `util/app.py`, `util/service/send_email.py`
- Database
  - Schema and seed: `setup_database.sql`
- Root config
  - Backend environment variables: `.env.example`

## 4. Dependencies
- Frontend (see `vite-project/package.json`)
  - react 18, react-dom 18
  - @react-google-maps/api
  - axios
  - react-router-dom
  - vite
- Backend (Python)
  - Flask (`flask`), CORS (`flask-cors`)
  - Requests (`requests`)
  - Pillow (`Pillow`)
  - Boto3 (`boto3`)
  - dotenv (`python-dotenv`)
  - MySQL Connector (`mysql-connector-python`)
  - Built-in: `smtplib`, `email`

Environment variable examples:
- Backend: see `.env.example` (AWS, `INRIX_TOKEN`, MySQL, Gmail SMTP)
- Frontend: see `vite-project/.env.example` (`VITE_GOOGLE_MAPS_API_KEY`, `VITE_API_BASE_URL`)
