# Performance Testing

**Project Name:** OptiCrop — Smart Agricultural Production Optimization Engine
**Team ID:** _xxxxxx_
**Date:** _add date_

## Step 1: Testing Overview
| Field | Details |
|---|---|
| Testing Tool Used | Manual testing via browser + `time` measurement; optionally Postman/JMeter for load testing |
| Environment | Local Flask development server |
| Scope | Prediction endpoint (`/predict`) response time and page load times |

## Step 2: Test Scenarios & Results
| Scenario | Load | Expected Result | Observed Result |
|---|---|---|---|
| Single prediction request | 1 user | Response within a few seconds | Pass — near-instant response (model already loaded in memory) |
| Repeated sequential requests | 10 requests | Consistent response time | Pass — no noticeable degradation |
| Concurrent requests (future load test) | Multiple simultaneous users | App remains responsive | Not yet tested — recommended before production deployment |

## Step 3: Model Inference Performance
- Model type: Logistic Regression (lightweight, fast inference).
- `model.pkl` is loaded once at Flask app startup, avoiding repeated disk reads per request.

## Recommendations
- Before production deployment, run a load test (e.g., with Locust or JMeter) to validate behavior under concurrent traffic.
- Consider a production WSGI server (e.g., Gunicorn) instead of the Flask development server.

*(Cross-reference: functional test cases available in `6.Project Testing/Model_Evaluation_and_Testing.md`.)*
