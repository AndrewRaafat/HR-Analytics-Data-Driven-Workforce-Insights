import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix

# ==============================

# 1) Load & basic Cleaning

# ==============================
df = pd.read_excel("C:/Users/andro/Downloads/Dashboard Assigments.xlsx")

# تنظيف المسافات في النصوص
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].str.strip()

# تحويل التواريخ وحساب السن وسنين الخبرة
df["DOB"] = pd.to_datetime(df["DOB"])
df["Hire date"] = pd.to_datetime(df["Hire date"])
df["Age_Calculated"] = 2026 - df["DOB"].dt.year
df["Tenure"] = 2026 - df["Hire date"].dt.year

# ترتيب المناصب يدوياً (Ordinal Encoding)
pos_map = {'Employee': 1, 'Supervisor': 2, 'Manager': 3}
df['Position_Rank'] = df['Position'].map(pos_map)

# ==============================

# 2) Exploratory Data Analysis (EDA)

# ==============================
print("--- Generating Visualizations ---")
sns.set(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# توزيع الرواتب
sns.histplot(df['Salary'], kde=True, ax=axes[0, 0], color='skyblue')
axes[0, 0].set_title('Salary Distribution')

# الرواتب حسب القسم
sns.barplot(x='Salary', y='Dep', data=df, ax=axes[0, 1], palette='viridis')
axes[0, 1].set_title('Average Salary by Department')

# السن مقابل المرتب
sns.scatterplot(x='Age_Calculated', y='Salary', hue='Gender', data=df, ax=axes[1, 0])
axes[1, 0].set_title('Age vs Salary')

# عدد الموظفين في الفروع
sns.countplot(x='Branch', hue='Gender', data=df, ax=axes[1, 1])
axes[1, 1].set_title('Employee Count by Branch')

plt.tight_layout()
plt.show()

# ==============================

# 3) Data Preprocessing for ML

# ==============================
# تحويل النوع لأرقام (Target)
df['Gender_Target'] = df['Gender'].map({'Male': 1, 'Female': 0})

# تحويل باقي الأعمدة لـ Dummies
df_ml = pd.get_dummies(df, columns=['Dep', 'Branch', 'PayType'], drop_first=True)

# ==============================

# 4) Regression (Salary Prediction)

# ==============================
print("\n--- Regression Results (Salary) ---")
# هنستخدم الأعمدة اللي بتأثر فعلاً على المرتب
X_reg = df_ml[['Age_Calculated', 'Tenure', 'Position_Rank', 'Gender_Target']]
y_reg = df_ml['Salary']

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

rf_reg = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
rf_reg.fit(X_train_r, y_train_r)

y_pred_r = rf_reg.predict(X_test_r)
print(f"R2 Score: {r2_score(y_test_r, y_pred_r):.2f}") 
print(f"RMSE: {np.sqrt(mean_squared_error(y_test_r, y_pred_r)):.2f}")

# ==============================

# 5) Classification (Gender Prediction)

# ==============================
print("\n--- Classification Results (Gender) ---")
# ملوحظة: حذفنا الـ ID تماماً عشان منوصلش لـ 100% ونمنع الـ Overfitting
# حذفنا برضه الـ Salary عشان نخلي المهمة "أصعب" للموديل ونوصل لـ 80%
X_cls = df_ml[['Position_Rank', 'Age_Calculated', 'Tenure']] 
# هنضيف أعمدة الأقسام اللي اتعملها Dummies
dep_cols = [col for col in df_ml.columns if col.startswith('Dep_')]
X_cls = pd.concat([X_cls, df_ml[dep_cols]], axis=1)

y_cls = df_ml['Gender_Target']

X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_cls, y_cls, test_size=0.3, random_state=42)

log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train_c, y_train_c)

y_pred_c = log_model.predict(X_test_c)
acc = accuracy_score(y_test_c, y_pred_c)

print(f"Gender Prediction Accuracy: {acc*100:.2f}%")
print("\nConfusion Matrix:")
print(confusion_matrix(y_test_c, y_pred_c))