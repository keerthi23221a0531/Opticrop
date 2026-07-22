# Scalability & Future Plan

**Project Name:** OptiCrop — Smart Agricultural Production Optimization Engine
**Team ID:** _xxxxxx_
**Date:** _add date_

## Current System
OptiCrop runs as a single Flask app with a pre-trained Logistic Regression model (`model.pkl`) serving one prediction request at a time on the development server — suitable for demo/small-scale use.

## Scaling the Current Solution
- Deploy behind a production WSGI server (Gunicorn/uWSGI) with a reverse proxy (Nginx) to handle more concurrent users.
- Containerize with Docker for consistent deployment across environments.
- Move the dataset/model to cloud storage and add a simple database (e.g., PostgreSQL) to log predictions for future retraining.

## Future Feature Roadmap
1. **Model retraining pipeline:** Scheduled retraining as new agricultural data becomes available.
2. **Confidence scores:** Show prediction probability alongside the recommended crop.
3. **Multi-region support:** Extend the dataset to cover more geographies/crop varieties.
4. **Mobile-friendly / regional-language UI:** Improve accessibility for farmers.
5. **API access:** Expose `/predict` as a documented REST API for integration with other agri-tech tools.

## Long-Term Vision
Evolve OptiCrop from a single-crop recommendation tool into a broader agricultural decision-support platform covering yield prediction, pest/disease risk, and irrigation planning.
