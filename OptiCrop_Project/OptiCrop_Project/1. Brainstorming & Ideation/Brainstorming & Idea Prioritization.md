# Brainstorming & Idea Prioritization

**Project Name:** OptiCrop — Smart Agricultural Production Optimization Engine
**Team ID:** _xxxxxx_
**Date:** _add date_

## Step 1: Brainstorm and Idea Listing
Each team member listed ideas without judging them at this stage.

| S.No | Team Member | Idea / Suggestion | Category |
|---|---|---|---|
| 1 | Member 1 | Recommend a crop based on soil NPK values, temperature, humidity, pH and rainfall | Core Feature |
| 2 | Member 2 | Use K-Means clustering to discover natural groupings of similar growing conditions | ML Approach |
| 3 | Member 3 | Use Logistic Regression to classify the most suitable crop label | ML Approach |
| 4 | Member 4 | Build a Flask web app with Home, About and Find Your Crop pages | Application |
| 5 | Member 5 | Allow the model to be retrained on new agricultural datasets | Scalability |
| 6 | Member 6 | Show confidence/probability of the recommended crop to the farmer | Enhancement |

## Step 2: Idea Prioritization
Each grouped idea rated on feasibility and importance to decide what goes into the MVP.

| Idea | Feasibility (1-5) | Importance (1-5) | Priority |
|---|---|---|---|
| Crop recommendation from soil/environment inputs | 5 | 5 | High — MVP |
| Flask web interface (Home/About/FindYourCrop) | 5 | 5 | High — MVP |
| K-Means clustering for pattern discovery | 4 | 4 | High — MVP |
| Logistic Regression classification | 5 | 5 | High — MVP |
| Confidence score display | 3 | 3 | Medium — Future Scope |
| Model retraining on new datasets | 3 | 3 | Medium — Future Scope |

**Outcome:** The team prioritized building an ML pipeline (data preprocessing → clustering → classification) wrapped in a simple Flask application that takes N, P, K, temperature, humidity, pH and rainfall as inputs and returns the recommended crop.
