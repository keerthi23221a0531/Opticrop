# Project Testing — Model Evaluation & Application Testing

## 1. Model Evaluation Metrics
All models are evaluated and compared using important classification metrics such as **Accuracy, Precision, Recall, F1-Score, Confusion Matrix, and ROC-AUC Score**. These metrics help identify the model that provides the most accurate and reliable predictions for the dataset.

### Sample Classification Report (Logistic Regression)

| Crop | Precision | Recall | F1-score | Support |
|---|---|---|---|---|
| apple | 1.00 | 1.00 | 1.00 | 4 |
| banana | 1.00 | 1.00 | 1.00 | 22 |
| blackgram | 0.83 | 0.90 | 0.86 | 21 |
| chickpea | 1.00 | 1.00 | 1.00 | 24 |
| coconut | 1.00 | 1.00 | 1.00 | 19 |
| coffee | 1.00 | 0.95 | 0.97 | 20 |
| cotton | 0.91 | 0.91 | 0.91 | 22 |
| grapes | 1.00 | 1.00 | 1.00 | 6 |
| jute | 0.88 | 0.82 | 0.85 | 17 |
| kidneybeans | 0.83 | 1.00 | 0.91 | 20 |
| lentil | 0.94 | 0.94 | 0.94 | 17 |

*(Full report generated via `sklearn.metrics.classification_report`.)*

After evaluating the performance of all trained models, the best-performing model is selected based on its overall classification results and generalization capability. The finalized model is then serialized using `pickle.dump()` and stored as `model.pkl` so that it can be reused without retraining during deployment in the Flask web application.

## 2. Test Cases

| Test ID | Test Case | Input | Expected Output | Status |
|---|---|---|---|---|
| TC01 | Valid input prediction | N=105, P=35, K=40, Temp=25, Humidity=64, pH=7, Rainfall=100 | Suggested crop returned (e.g., "coffee") | Pass |
| TC02 | Missing input field | One field left empty | Form validation error (required field) | Pass |
| TC03 | Non-numeric input | Text entered instead of number | Prediction fails / input rejected | Pass |
| TC04 | Home page navigation | Click "Home" | Home page loads | Pass |
| TC05 | About page navigation | Click "About" | About page loads with project description | Pass |
| TC06 | Find Your Crop navigation | Click "FindYourCrop" | Prediction form loads | Pass |
| TC07 | Model loading | Start Flask app | model.pkl loads without error | Pass |

## 3. Application Testing (End-to-End)
1. Open the project in VS Code and ensure all project folders/dependencies are set up.
2. Run `app.py` and open the server URL shown in the terminal.
3. **Home Page:** Verify the OptiCrop landing page displays correctly.
4. **About Page:** Verify navigation to the About page and correct project description.
5. **FindYourCrop Page:** Enter environmental conditions and click "Predict" to verify a valid crop recommendation is returned.
