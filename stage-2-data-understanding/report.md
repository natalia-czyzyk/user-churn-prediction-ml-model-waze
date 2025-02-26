# A machine learning model to predict user churn in Waze company
## Data understanding report

## Overview
This report summarizes the initial data analysis performed to understand the structure, quality, and key insights of the dataset. The goal of this task was to inspect, clean, and analyze the data to identify patterns in user behavior, particularly in relation to churn. Key areas of focus included data types, missing values, and early trends in churned versus retained users.
## Data Understanding
### Data Inspection & Preparation
- The dataset was loaded and analyzed, ensuring correctness and consistency.
- Key aspects examined include:
  - **Column data types**
  - **Key metrics**
  - **Outliers**
  - **Missing values**

### Key Findings
#### Missing Values
- The dataset contained **700 null values** in the ‘label’ column.
- No discernible pattern or non-random cause was identified in the missing data.

#### Churned vs. Retained Users
- **Churned users drove approximately 200 km more and 2.5 more hours** in the last month than retained users.
- Churned users took **more drives in fewer days**, with longer trip durations and distances.
- They used the app **half as many times** as retained users during the same period.
- These insights suggest that users who drive significantly more than the median might find Waze lacking in features that meet their needs.

### Recommendations for Further Analysis
To enhance understanding, additional data should be incorporated, including:
- **Subscription type** (Free vs. Premium)
- **Revenue per user**
- **Support interactions** (Number of times the user contacted support)
- **App issues** (Bugs encountered, crash reports)

## Conclusion
Initial findings suggest that high-usage drivers may not be fully satisfied with the app’s functionality, leading to churn. Further analysis with additional data points will help refine the model and provide actionable recommendations to improve retention.
