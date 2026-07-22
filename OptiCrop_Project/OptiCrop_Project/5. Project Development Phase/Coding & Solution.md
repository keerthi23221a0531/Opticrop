# Coding & Solution

**Project Name:** OptiCrop — Smart Agricultural Production Optimization Engine
**Team ID:** _xxxxxx_
**Date:** _add date_

## Overview
This section documents the implementation of the OptiCrop solution: a data pipeline that trains a crop-recommendation model and a Flask web app that serves predictions.

## Implementation Summary
1. **Data Preprocessing (`1_data_preprocessing.py`):** Loads `Crop_recommendation.csv`, renames columns (N/P/K → nitrogen/phosphorous/potassium), performs EDA, handles nulls/outliers, and splits into train/test sets.
2. **Model Building (`2_model_building.py`):** Applies K-Means clustering (elbow method) to explore natural groupings, trains a Logistic Regression classifier on the labeled data, evaluates it, and serializes the best model to `model.pkl` via `pickle`.
3. **Web Application (`app.py`):** A Flask app with routes for `/` (Home), `/about`, `/findyourcrop`, and `/predict` (POST). The `/predict` route reads form values, converts them to a feature array, calls `model.predict()`, and renders the result back to the user.

## Working Functionality
- User submits N, P, K, temperature, humidity, pH, rainfall via the FindYourCrop form.
- The app returns a message such as: *"Best crop for given conditions is coffee"*.

## Alignment with Requirements
Matches FR-1 through FR-4 in `Solution Requirements.md` — input collection, ML-based prediction, web interface, and result display.
