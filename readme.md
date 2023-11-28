# Credit Card Fraudalent System

This project is a fraud detection model based on anonymized credit card transactions,that flags any kind of fraud transactions taking place in real-time.


## Tutorial
<video width="800" height="400" controls autoplay loop>
  <source src="Detection_Video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Overview
This system is designed to identify and prevent fraudulent transactions in real-time, providing a secure environment for both financial institutions and cardholders. We have developed a machine learning model using classification algorithms and techniques to accurately detect if a credit card transaction is fraudulent or not. 

### Key Features:
1.Real-time Monitoring: Transactions are analyzed as they occur, enabling swift identification and response to suspicious activities.

2.Machine Learning Algorithms: Our system utilizes state-of-the-art machine learning algorithms for predictive modeling and pattern recognition. It continuously learns and adapts to new fraud patterns.

3.We have used SMOTE(Synthetic Minority Oversampling Technique) since the the target class in the dataset was highly imbalanced.

### Technology Stack:
Programming Language: Python

Machine Learning Frameworks: Scikit-Learn, Matplotlib,Seaborn

Web Interface: Streamlit Application

### Implementation Steps
1.Data Collection: Gather historical transaction data for training machine learning models.

2.Preprocessing: Cleaning and preprocessing of data to remove outliers,duplicacies,and irrelevant information. Implement feature engineering for enhanced model performance.

3.Model Training: Developed and trained machine learning models using a labeled dataset. 

4.User Interface Development: Design a user-friendly interface for monitoring, reporting, and managing potential fraud cases.

## Data
This credit card dataset contains transactions made by credit cards in September 2013 by European cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced; the positive class (frauds) account for 0.172% of all transactions.
[Credit Card Dataset](creditcard.csv)

## Installation 
Version of the packages:<p>
1.numpy==1.23.5<p>
2.pandas==1.5.3<p>
3.requests==2.31.0<p>
4.scikit-learn==1.3.2<p>
5.validators==0.22.0<p>
6.zipp==3.17.0<p>
7.streamlit==1.28.2<p>
8.pickle==4.0<p>

## Training and Evaluation:
We have used the following classification models to learn from the given data:<p>
1.Logistic Regression: R2 Score-> 91.29% <p>
2.Decision Tree Classifier: R2 Score-> 84.90%<p>
3.kNearestNeighbour Classifier: R2 Score->99.19%<p>
4.Random Forest Classifier: R2 Score->99.85%<p>

## Results:
Accuracy achieved on the models:<p>
1.Logistic Regression: Accuracy-> 97.82% <p>
2.Decision Tree Classifier: Accuracy-> 96.22%<p>
3.kNearestNeighbour Classifier: Accuracy-> 99.79%<p>
4.Random Forest Classifier: Accuracy->99.96%<p>

## Contributions:
1.Uplab Rajak(12311140):Data Collection,Model Development,Frontend-backend Integration,Deployment.

2.Brishti De(12310610):Data Preprocessing,Model Development,Testing,User Documentation and support.

