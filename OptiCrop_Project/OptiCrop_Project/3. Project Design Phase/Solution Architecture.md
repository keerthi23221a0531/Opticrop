# Solution Architecture Diagram

**Project Name:** OptiCrop — Smart Agricultural Production Optimization Engine
**Team ID:** _xxxxxx_
**Date:** _add date_

## Architecture Layers

```
┌───────────────────────────────────────────────────┐
│                 PRESENTATION LAYER                 │
│  HTML/CSS Templates: home.html, about.html,        │
│  findyourcrop.html  (rendered via Jinja2 by Flask)  │
└───────────────────────┬─────────────────────────────┘
                         │ HTTP request (form data)
┌───────────────────────▼─────────────────────────────┐
│                 APPLICATION LAYER                   │
│  Flask app (app.py)                                 │
│   - Routes: /, /about, /findyourcrop, /predict       │
│   - Loads model.pkl and runs prediction              │
└───────────────────────┬─────────────────────────────┘
                         │ feature vector / prediction
┌───────────────────────▼─────────────────────────────┐
│                    DATA LAYER                        │
│  Crop_recommendation.csv (raw dataset)                │
│  x_train.csv / x_test.csv / y_train.csv / y_test.csv  │
│  model.pkl (trained Logistic Regression model)         │
└───────────────────────────────────────────────────────┘
```

## Components
- **Presentation Layer:** Three HTML pages served by Flask (Home, About, Find Your Crop).
- **Application Layer:** `app.py` — Flask routes, request handling, and calling `model.predict()`.
- **Data Layer:** CSV dataset + pickled trained model.

## Data Flow
Farmer input → Flask form → feature array → `model.pkl.predict()` → predicted crop → rendered back on `findyourcrop.html`.
