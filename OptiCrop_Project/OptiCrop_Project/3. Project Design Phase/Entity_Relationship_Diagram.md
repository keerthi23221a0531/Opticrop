# Entity Relationship Diagram (ERD)

The ER diagram represents the core entities involved in the OptiCrop Smart Agricultural Production Optimization System and illustrates how they interact with each other. It provides a clear structure for organizing applicant/user information, soil data, prediction results, and machine learning model outputs within the database.

## Entities Involved
The ER diagram features seven primary entities:
1. User
2. SoilData
3. Crop
4. Dataset
5. MLModel
6. Prediction
7. Report

## Primary Keys
| Entity | Primary Key |
|---|---|
| User | user_id |
| SoilData | soil_id |
| Crop | crop_id |
| Dataset | dataset_id |
| MLModel | model_id |
| Prediction | prediction_id |
| Report | report_id |

## Foreign Keys
- SoilData references User via user_id
- Prediction references SoilData via soil_id
- Prediction references Crop via crop_id
- Prediction references MLModel via model_id
- Report references Prediction via prediction_id

## Relationships
- **User → SoilData:** One user can submit multiple soil data records for crop analysis (1 to Many)
- **SoilData → Prediction:** A single soil data entry generates one crop prediction result (1 to One)
- **Crop → Prediction:** One crop can be recommended in multiple prediction results (1 to Many)
- **MLModel → Prediction:** One machine learning model can generate multiple prediction records (1 to Many)
- **Dataset → MLModel:** A single dataset can be used to train multiple machine learning models (1 to Many)
- **Prediction → Report:** One prediction can generate multiple agricultural reports and recommendations (1 to Many)

## Cardinality Summary
A single user can submit multiple soil data records for agricultural analysis. Each soil data entry is processed by the machine learning model to generate crop prediction results. A crop can appear in multiple predictions, while a single machine learning model can generate predictions for many users and soil conditions. Each prediction can further generate multiple agricultural reports containing summaries and farming recommendations.

## Normalization and Structure
The ER diagram is normalized to separate user information, soil parameters, crop details, datasets, machine learning models, prediction records, and reports into different entities. This structure reduces redundancy, improves scalability, and supports efficient querying.

## Entity Attributes

**User**
- user_id (PK), name, email, password, role

**SoilData**
- soil_id (PK), nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall, season, user_id (FK)

**Crop**
- crop_id (PK), crop_name, crop_type, season, optimal_ph, water_requirement

**Dataset**
- dataset_id (PK), dataset_name, source, total_records, last_updated

**MLModel**
- model_id (PK), dataset_id (PK/FK), dataset_name, source, total_records, last_updated

**Prediction**
- prediction_id (PK), soil_id (FK), crop_id (FK), model_id (FK), prediction_date, confidence_score

**Report**
- report_id (PK), prediction_id (FK), generated_date, summary, recommendations

## Use Case Coverage
This ER model supports the core functionalities of the OptiCrop Smart Agricultural Production Optimization System, including:
- Collecting and managing soil and environmental data from users.
- Predicting suitable crops using machine learning algorithms.
- Managing datasets and trained machine learning models.
- Generating intelligent crop recommendations and prediction reports.
- Supporting sustainable farming practices and data-driven agricultural decision-making.
