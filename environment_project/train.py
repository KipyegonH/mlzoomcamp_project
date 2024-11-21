import xgboost as xgb
import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
import pickle

df = pd.read_excel(r"C:\Users\hillarik\Desktop\ML PROJECT\data\default of credit card clients.xls", engine='xlrd')
df.columns = df.columns.str.lower().str.replace(' ', '_')
df = df.drop(columns=['id'])

sex_values = {1: 'male', 2: 'female'}
df['sex'] = df['sex'].map(sex_values)

education_values = {1: 'graduate school', 2: 'university', 3: 'high school', 4: 'others', 0: 'others', 5: 'others', 6: 'others'}
df['education'] = df['education'].map(education_values)

marriage_values = {1: 'married', 2: 'single', 3: 'others', 0: 'others'}
df['marriage'] = df['marriage'].map(marriage_values)

pay_values = {
    -2: 'not paid duly', -1: 'pay duly', 0: 'no delay', 1: 'payment delay for one month',
    2: 'payment delay for two months', 3: 'payment delay for three months',
    4: 'payment delay for four months', 5: 'payment delay for five months',
    6: 'payment delay for six months', 7: 'payment delay for seven months',
    8: 'payment delay for eight months', 9: 'payment delay for nine months and above'
}
pay_columns = ['pay_0', 'pay_2', 'pay_3', 'pay_4', 'pay_5', 'pay_6']
for col in pay_columns:
    df[col] = df[col].map(pay_values)

string_columns = list(df.dtypes[df.dtypes == object].index)
for c in string_columns:
    df[c] = df[c].str.lower().str.replace(' ', '_')

X = df.drop(columns=['default_payment'])
y = df['default_payment']

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_full_train = df_full_train.reset_index(drop=True)
y_full_train = df_full_train['default_payment'].values
y_test = df_test['default_payment'].values

df_full_train = df_full_train.drop(columns=['default_payment'])
dicts_full_train = df_full_train.to_dict(orient='records')
dv = DictVectorizer(sparse=False)
X_full_train = dv.fit_transform(dicts_full_train)

dicts_test = df_test.drop(columns=['default_payment']).to_dict(orient='records')
X_test = dv.transform(dicts_test)
print(f"feature names==========data type {type(dv.get_feature_names_out())}======={dv.get_feature_names_out()}")
dfulltrain = xgb.DMatrix(X_full_train, label=y_full_train, feature_names=dv.get_feature_names_out().tolist())
dtest = xgb.DMatrix(X_test, label=y_test, feature_names=dv.get_feature_names_out().tolist())

watchlist = [(dfulltrain, 'train'), (dtest, 'test')]

xgb_params = {
    'eta': 0.1,
    'max_depth': 4,
    'min_child_weight': 10,
    'objective': 'binary:logistic',
    'eval_metric': 'auc',
    'nthread': 8,
    'seed': 1,
}

model = xgb.train(xgb_params, dfulltrain, num_boost_round=80, verbose_eval=10, evals=watchlist)

y_pred = model.predict(dtest)
auc_score = roc_auc_score(y_test, y_pred)
print(f"ROC AUC score: {auc_score}")

model_path = 'xgb_model.pkl'
with open(model_path, 'wb') as f:
    pickle.dump(model, f)
print(f"Model saved to {model_path}")

dv_path = 'dv.pkl'
with open(dv_path, 'wb') as f:
    pickle.dump(dv, f)
print(f"DictVectorizer saved to {dv_path}")


