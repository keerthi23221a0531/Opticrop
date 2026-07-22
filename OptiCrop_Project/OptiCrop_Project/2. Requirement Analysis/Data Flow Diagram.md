# Data Flow Diagram (DFD)

**Project Name:** OptiCrop — Smart Agricultural Production Optimization Engine
**Team ID:** _xxxxxx_
**Date:** _add date_

## DFD Symbol Legend
| Symbol | Name | Description |
|---|---|---|
| Oval / Rounded | External Entity | A person, organization, or system outside the system boundary |
| Rectangle | Process | An activity that transforms data |
| Open rectangle | Data Store | Where data is held (files, database) |
| Arrow | Data Flow | Movement of data between entities, processes and stores |

## Level 0 (Context Diagram)
```
[Farmer] --(soil & environment inputs)--> [OptiCrop Web App] --(recommended crop)--> [Farmer]
```

## Level 1 (Detailed Flow)
```
[Farmer]
   |  (N, P, K, temperature, humidity, pH, rainfall)
   v
[1. Flask Web Form - FindYourCrop] 
   |  (feature vector)
   v
[2. Prediction Process] --(loads)--> [model.pkl - Data Store]
   |  (predicted crop label)
   v
[3. Render Result on FindYourCrop page]
   |
   v
[Farmer] (sees recommended crop)
```

## External Entities
- Farmer / User

## Processes
1. Collect soil & environmental inputs (web form)
2. Run prediction using the trained ML model
3. Display recommended crop to the user

## Data Stores
- `Crop_recommendation.csv` — training dataset
- `model.pkl` — serialized trained model
- `x_train.csv` / `x_test.csv` / `y_train.csv` / `y_test.csv` — processed train/test splits
