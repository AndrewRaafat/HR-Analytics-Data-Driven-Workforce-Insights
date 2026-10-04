# 📊 HR Analytics – Data-Driven Workforce Insights

## 📌 Project Overview

This project focuses on analyzing HR data for **999 employees** to discover workforce insights, understand salary patterns, and support data-driven HR decision-making.

The project combines **Data Cleaning, Exploratory Data Analysis, Power BI Dashboards, Feature Engineering, and Predictive Modeling** to provide a complete view of the organization's workforce.

---

## 🎯 Project Objectives

- Analyze the company's workforce structure.
- Understand salary distribution across departments and branches.
- Analyze employee age and experience.
- Identify the main factors affecting salary.
- Build interactive HR dashboards.
- Develop a machine learning model to predict employee salaries.
- Provide data-driven recommendations for HR management.

---

## 🗂️ Dataset

The dataset contains information about **999 employees** across different branches, departments, roles, salaries, and employee-related attributes.

### Main Data Categories

- Employee Information
- Branch
- Department
- Job Role
- Salary
- Date Information
- Age
- Experience / Tenure
- Employee Level

---

## 🧹 Data Cleaning & Preprocessing

Several preprocessing steps were performed before analysis and modeling.

### 1. Removing Non-Impactful Identifiers

Identifiers such as:

- Employee Names
- Employee IDs

were removed because they do not provide useful information for salary prediction and could introduce unnecessary bias.

### 2. Feature Engineering

New features were created from the available date information:

- **Age** – calculated from the employee's date of birth.
- **Tenure** – calculated from employment dates to measure years of experience.

These features helped identify important factors related to employee compensation.

### 3. Data Standardization

The dataset was cleaned and standardized by:

- Cleaning text values.
- Handling categorical variables.
- Encoding categorical features.
- Preparing numerical features for machine learning.

---

# 📊 Power BI Dashboards

The project includes two main dashboards.

## Dashboard 1 – Workforce Overview

### Scaling Operations and Budget

The first dashboard provides an overview of the company's workforce and financial structure.

### Key Insights

- **999 employees** across **5 branches**.
- Branches include:
  - Sharqia
  - Cairo
  - Giza
  - Ismailia
  - Alexandria
- Total salary budget is **over 9M**.
- Average salary is approximately **9.31K** per employee.
- **Compliance** is the largest department based on both employee headcount and salary expenditure.

<img width="1276" height="717" alt="Screenshot 2026-10-04 204828" src="https://github.com/user-attachments/assets/40e357dc-0018-46fe-8197-f340b0da1c69" />

---
## Dashboard 2 – Demographics & Experience

### Stability Through Experience

The second dashboard focuses on employee demographics, experience, and organizational hierarchy.

### Key Insights

- Average employee tenure is approximately **19.60 years**.
- The largest age group is between **30 and 40 years old**.
- The workforce consists of:
  - **671 Employees**
  - **159 Supervisors**
  - **169 Managers**

These insights indicate a relatively experienced and stable workforce.
<img width="1277" height="717" alt="Screenshot 2026-10-04 204802" src="https://github.com/user-attachments/assets/33c5019d-1384-4095-9b01-8ce7eaa6c166" />

---

# 🤖 Predictive Modeling

## Salary Prediction

A **Random Forest Regressor** was implemented to predict employee salaries.

### Model Goal

The model aims to understand the relationship between employee characteristics and salary, helping HR teams make better decisions when planning compensation and hiring.

### Model Performance

- **Model:** Random Forest Regressor
- **R² Score:** **0.90**

The model explains approximately **90% of the variation in salary within the dataset**, indicating strong predictive performance.

### Business Value

The model can help HR teams with:

- Salary benchmarking
- New employee salary planning
- Budget forecasting
- Compensation analysis
- Supporting internal pay equity

---

# 💡 Key Business Insights

### 👥 Workforce

The company has a workforce of **999 employees** distributed across five branches.

### 💰 Salary

The total salary budget exceeds **9M**, with an average salary of approximately **9.31K**.

### 🏢 Departments

**Compliance** has the highest employee count and salary expenditure.

### 📅 Experience

The average employee tenure is **19.60 years**, showing strong workforce stability and experience.

### 🎂 Age

Employees aged **30–40** represent the largest part of the workforce.

### 🤖 Salary Prediction

The Random Forest model achieved an **R² score of 0.90**, demonstrating strong performance in predicting salary.

---

# 📌 Recommendations

## 1. Equity First

Use the salary prediction model as a supporting benchmark when setting salaries for new hires and reviewing compensation.

## 2. Generational Balance

Although the organization has a highly experienced workforce, recruiting younger talent can help maintain long-term workforce sustainability and knowledge transfer.

## 3. Improve Efficiency

Departments such as **Logistics** can be studied further because they show relatively high efficiency compared with their salary costs.

## 4. Data-Driven HR Decisions

Continue using HR analytics and predictive models to support workforce planning, budgeting, recruitment, and compensation decisions.

---

# 🛠️ Tools & Technologies

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Power BI**
- **Excel**
- **Data Cleaning**
- **Feature Engineering**
- **Machine Learning**
- **Data Visualization**

---

# 📁 Project Structure

```text
HR-Analytics/
│
├── Dataset/
│   └── HR_Dataset.csv
│
├── Python/
│   └── HR_Analytics.ipynb
│
├── PowerBI/
│   └── HR_Analytics_Dashboard.pbix
│
├── Images/
│   ├── Dashboard_1.png
│   └── Dashboard_2.png
│
└── README.md
```

---

# 📈 Project Workflow

```text
Raw HR Data
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
Exploratory Data Analysis
     ↓
Power BI Dashboards
     ↓
Machine Learning Model
     ↓
Salary Prediction
     ↓
Business Insights & Recommendations
```

---

# 👨‍💻 Author

**Andrew Raafat**

Data Analyst | Data Science Student

### Skills Demonstrated

- Data Cleaning
- Data Analysis
- Power BI
- Python
- Pandas
- SQL
- Machine Learning
- Data Visualization
- Business Intelligence

---

## ⭐ Project Purpose

This project demonstrates how HR data can be transformed into meaningful business insights and predictive solutions to support better workforce and compensation decisions.
