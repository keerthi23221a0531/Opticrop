# Project Proposal (Proposed Solution) Report

**Project Title:** OptiCrop — Smart Agricultural Production Optimization Engine
**Team ID:** _xxxxxx_
**Date:** _add date_

## Problem Statement
Farmers lack a reliable, data-driven way to determine which crop is best suited to their soil and environmental conditions, leading to lower yields and inefficient resource use.

## Proposed Solution
OptiCrop uses machine learning to recommend the most suitable crop from soil and environmental parameters — Nitrogen (N), Phosphorous (P), Potassium (K), temperature, humidity, pH, and rainfall — delivered through a lightweight Flask web application.

| Parameter | Description |
|---|---|
| **Problem Statement** | Lack of data-driven crop selection guidance for farmers |
| **Idea / Solution Description** | ML pipeline (K-Means clustering for pattern discovery + Logistic Regression for classification) trained on `Crop_recommendation.csv`, exposed via a Flask web app |
| **Novelty / Uniqueness** | Combines unsupervised clustering with supervised classification to both explore and predict crop suitability, wrapped in a farmer-friendly interface |
| **Social Impact / Business Model** | Improves food security and farmer income; can be offered as a value-added advisory service by agri-tech companies and cooperatives |
| **Scalability of the Solution** | Modular pipeline allows new crops/datasets/regions to be added by retraining the model |

## How It Works
1. Farmer enters soil & weather values on the FindYourCrop page.
2. Flask backend loads `model.pkl` and passes the input features to it.
3. The model returns the predicted crop label.
4. The result is rendered back on the page: *"Best crop for given conditions is &lt;crop&gt;"*.
