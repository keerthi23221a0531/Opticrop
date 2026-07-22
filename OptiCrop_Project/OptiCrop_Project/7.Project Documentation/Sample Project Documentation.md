# OptiCrop: Smart Agricultural Production Optimization Engine

## Project Description
OptiCrop is a Machine Learning-powered crop recommendation system that helps farmers decide the most suitable crop to grow based on soil nutrients (Nitrogen, Phosphorous, Potassium), temperature, humidity, pH, and rainfall. The system combines K-Means clustering (to discover patterns in soil/climate data) and Logistic Regression (to classify the best-fit crop), served through a Flask web application with Home, About, and Find Your Crop pages.

## Core Modules
- **Data Preprocessing Module:** Cleans and prepares `Crop_recommendation.csv` for modeling.
- **Model Building Module:** Trains K-Means and Logistic Regression models, evaluates them, and saves the best one.
- **Prediction Module (Flask):** Accepts user input via web form and returns the recommended crop.

## Target Users
Farmers, agricultural cooperatives, and researchers looking for a fast, data-driven crop recommendation.

*(This mirrors the structure of a project documentation summary — see the full `README.md` at the project root for setup, tech stack and run instructions.)*
