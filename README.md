# Seasonal Flu Machine learning Prediction_model

A prediction Model of Season Flu Vaccine uptake

![seasonal](https://github.com/waihiga9/H1N1_and_Seasonal_Flu_Vaccines/blob/d02e9180ec5751259ea57f581310a769d05b6b2d/Images/vaccination.png)

## Introduction
The H1N1 pandemic emerged in 2009 as a global health crisis. The virus, originally originating in pigs, transmitted to humans and quickly spread worldwide. The pandemic had a devastating impact, resulting in an estimated 151,700 to 575,400 deaths worldwide. Young children and middle-aged adults were particularly vulnerable to the severe effects of the H1N1 virus.

In response to the pandemic, a vaccine for the H1N1 virus was developed and made available to the public in October 2009. This vaccine played a crucial role in mitigating the spread and severity of the virus. The efforts to combat the H1N1 pandemic were successful, and the World Health Organization (WHO) officially declared its end in August 2010.

However, it's important to note that the H1N1 virus has not been eradicated completely. It continues to circulate as a seasonal flu virus, requiring ongoing surveillance and preventive measures to protect public health. The availability of vaccines and ongoing awareness efforts are vital in minimizing the impact of the H1N1 virus and preventing future outbreaks.


## Business Understanding
The business problem at hand revolves around empowering ApexHealth Insurance - the stakeholders to make informed decisions during the flu season. Additionally, the model aims to classify individuals based on their risk of contracting the flu, considering factors such as age, gender, and household composition. This classification will enable ApexHealth Insurance to identify high-risk individuals and offer them personalized measures and preventive strategies to minimize the chances of flu contraction. By providing tailored recommendations, such as reminders for flu shots, hygiene practices, or access to additional preventive resources, ApexHealth Insurance can actively contribute to reducing the occurrence of flu cases among their policyholders and consequently minimize healthcare costs.

Furthermore, the predictive model will allow ApexHealth Insurance to identify individuals who are likely to come into contact with flu-infected individuals. By notifying these individuals proactively, ApexHealth Insurance can support early intervention measures, such as seeking medical advice, taking antiviral medications, or implementing isolation protocols. This proactive approach helps prevent severe flu scenarios, reduce hospital admissions, and ultimately minimize healthcare expenses for both policyholders and ApexHealth Insurance.


## Main Objectives

The goal of this project is to develop a predictive model using individual characteristics and behavioral patterns to estimate seasonal flu vaccine uptake


## Data Description
The datasets used in this project were obtained from Driven Data and originate from the National 2009 H1N1 Flu Survey (NHFS). These datasets provide comprehensive information on the social, economic, and demographic backgrounds of the survey respondents, along with their opinions on the H1N1 and seasonal flu vaccines. The data has been split into two parts: the training set features and the training set labels.


## Data Preparation

The data was loaded and assessed, followed by exploratory data analysis (EDA) to gain better understanding. The dataset contained numerous missing values, which were imputed. Furthermore, categorical features were converted to enable one-hot encoding, making the data suitable for modeling purposes.

Top 5 features that made it to modelling;
|No.| col_name    | scores|
|---| ---       | ---         |
|1| `opinion_seas_risk`| 2794.888237|
|2|`doctor_recc_seasonal`| 2421.579654|
|3|`age_group`| 1997.217625|
|4|`employment_industry`| 1669.849661|
|5|`opinion_seas_vacc_effective`| 991.273021|

Comaprison of the final features and feature importance analysis,
![features](https://github.com/waihiga9/H1N1_and_Seasonal_Flu_Vaccines/blob/9bc9b1ded9bd604318b5aa61cbbef60b6513f777/Images/feature_importance.png)


## Modelling

The data was split into training and test datasets, with the training data used to train the models and the test data used to evaluate their performance. A baseline model was established using Logistic Regression as the initial modeling approach.

Additionally the following models were used:
- Decision Tree Model
- RandomForest Model
- Gradient Boosting Model
- XGBoost Model


## Model Evaluation

The model selection was based on the following criteria:

|model_| train_accuracy| test_accuracy| cross_validation_accuracy|
|---| ---       | ---         | ---  |
| Logistic_Regression| 76.69| 76.92| 76.61|
| Decision_Tree| 76.94| 75.86| 75.69|
| Random_Forest| 77.43| 76.6| 76.59|
| Gradient_Boosting| 78.2| 77.55| 77.32|
| XGBoost| 76.6| 76.8| 76.23| 

 The Gradient Boosting model was selected as the top performer among the models, exhibiting strong predictive capabilities. Its superior performance in accurately predicting the seasonal flu vaccine uptake made it the preferred choice.

![confusion_matrix]

## Conclusion

The analysis of the data indicated that the Gradient Boosting model performed the best, achieving the highest train and test accuracies.
However, it is important to acknowledge the challenges that was faced during the project
- Data quality issues, including missing data and inconsistent formats, were addressed to ensure reliable and accurate analysis.
- The challenge of imbalanced race representation, with a higher proportion of white individuals in the dataset, as well as an overrepresentation of college students and homeowners, was managed to maintain fairness and avoid biased predictions.
- Model selection and tuning were carefully performed to identify the most suitable model and optimize its hyperparameters, although this process required considerable time and effort.
- Measures were taken to mitigate overfitting and enhance generalization by employing techniques such as cross-validation and regularization, ensuring the model's ability to perform well on unseen data.


## Recommendations

Based on the analysis and findings from the seasonal flu vaccine uptake prediction project, I would like to offer the following recommendations to Apex Health Insurance:

  1. Ensure free coverage of seasonal flu vaccines, including the vaccine and administration fees.
  2. Personalize outreach based on customer data, segmenting target audience and using multiple channels for effective communication.
  3. Collaborate with healthcare providers for widespread access to flu vaccines, sharing in-network providers and promoting accessible locations.
  4. Implement incentive programs (e.g., reduced premiums, cash-back, wellness points) to motivate vaccination.
  5. Incorporate flu vaccination into existing wellness programs, providing resources, support, and incentives for preventive measures