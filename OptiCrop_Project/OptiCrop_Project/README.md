# OptiCrop — Smart Agricultural Production Optimization Engine

## Repository Structure
1. Brainstorming & Ideation
2. Requirement Analysis
3. Project Design Phase
4. Project Planning Phase
5. Project Development Phase
6. Project Testing
7. Project Documentation
8. Project Demonstration

*(Folder structure mirrors the [AI-ML-and-GEN-AI-Track-Project-Template](https://github.com/Ravi-teja-777/AI-ML-and-GEN-AI-Track-Project-Template).)*

## Conclusion
OptiCrop is a Machine Learning-powered smart agricultural recommendation system that supports data-driven farming by predicting the most suitable crop from key soil and environmental parameters — nitrogen, phosphorus, potassium (NPK), temperature, humidity, pH, and rainfall. By combining agricultural science with artificial intelligence, OptiCrop aims to reduce uncertainty in farming decisions and promote efficient, sustainable agricultural production.

The project uses K-Means Clustering to discover patterns in soil/climate data and Logistic Regression to classify the most appropriate crop, giving both exploratory insight and a reliable final recommendation.

## Tech Stack
- **Language:** Python
- **Libraries:** NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn, SciPy
- **Web Framework:** Flask
- **Model Storage:** Pickle (`model.pkl`)
- **Frontend:** HTML/CSS (Home, About, FindYourCrop pages)

## Dataset
- **Name:** Crop_recommendation.csv
- **Source:** [Kaggle - Smart Agricultural Production Optimizing Engine](https://www.kaggle.com/datasets/chitrakumari25/smart-agricultural-production-optimizing-engine)
- **Features:** N, P, K, temperature, humidity, ph, rainfall
- **Target:** label (recommended crop)

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Place `Crop_recommendation.csv` in the working directory.
3. Run `1_data_preprocessing.py` to clean and split the data.
4. Run `2_model_building.py` to train and save `model.pkl`.
5. Run `app.py` to launch the Flask web application.
6. Open the local server URL in your browser and use the "FindYourCrop" page to get recommendations.

## Team
_Add team member names and roles here._

---
Replace/expand any placeholder ("_xxxxxx_" / "_add date_") fields inside each phase folder's documents with your actual team details before final submission.
