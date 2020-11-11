import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

data = pd.read_csv(r'C:\Users\aacjp\OneDrive\Desktop\data\tables\Churn3.csv')
data = data.drop(['Unnamed: 0'], axis='columns')
val = pd.read_csv(r'C:\Users\aacjp\OneDrive\Desktop\data\tables\ChurnValidation.csv')
val = val.drop(['Unnamed: 0'], axis='columns')
X = data.drop(['churn'], axis='columns')
y = data['churn']
Xval = val.drop(['churn'], axis='columns')
yval = val['churn']

model = GradientBoostingClassifier(max_depth=9, min_samples_leaf=2, n_estimators=250).fit(X, y)
international_plan = 0
voice_mail_plan = 1
total_day_minutes = 265
total_eve_minutes = 195
total_intl_minutes = 10
total_intl_charge = 3
customer_service_calls = 1
avg_duration = 3
total_minutes = 595
irreg_calls = 6
arr = [international_plan, voice_mail_plan, total_day_minutes, total_eve_minutes, total_intl_minutes,
        total_intl_charge, customer_service_calls, avg_duration, total_minutes, irreg_calls]
pipe = Pipeline([('scaler', StandardScaler()), ('model', GradientBoostingClassifier(max_depth=9, min_samples_leaf=2, n_estimators=250))]).fit(X, y)
print(pipe.predict([arr]))