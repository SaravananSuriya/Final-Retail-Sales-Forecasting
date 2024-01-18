import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import mlflow
import mlflow.sklearn
from sklearn.metrics import mean_squared_error,mean_absolute_error,mean_absolute_percentage_error
from sklearn.model_selection import train_test_split
from math import sqrt
import warnings

warnings.filterwarnings("ignore")
df = pd.read_csv(r"Cleaned_Store_data2.csv")
data = df.copy()
print(len(df['Dept'].unique()))
def inv_trans(x):
  if x == 0:
    return x
  else:
    return 1/x

data['Markdown'] = data['Markdown'].apply(inv_trans)
x = data.drop(['Weekly_Sales','Size','Type','Date','weekly_sales'],axis = 1)
y = data['Weekly_Sales']

x_train,x_test,y_train,y_test = train_test_split(x, y,test_size = 0.25, random_state = 30)

def randomforest():
    n_estimators_val = [50, 100, 200, 300, 350, 400]
    Max_depth = [10,10,10,25, 25, 25]
    Min_sample_split = [5,5,5, 15,15,15]
    Min_samples_leaf = [7,7,7,13,13,13]

    for i,j,k,l in zip(Max_depth,Min_sample_split,Min_samples_leaf,n_estimators_val):
        model_rf = RandomForestRegressor(criterion = 'squared_error', n_estimators = l, max_depth = i, min_samples_split = j, min_samples_leaf = k, random_state=30)
        model_rf.fit(x_train,y_train)

        y_train_pred = model_rf.predict(x_train)
        y_test_pred = model_rf.predict(x_test)

        res = pd.DataFrame(data = list(zip(y_train,y_train_pred,y_test,y_test_pred)), columns = ['y_train','y_train_pred','y_test','y_test_pred'])
        print(res)

        train_MAE = mean_absolute_error(y_train_pred, y_train)
        test_MAE = mean_absolute_error(y_test_pred, y_test)

        #   train_MSE = mean_squared_error(y_train_pred, y_train)
        #   test_MSE = mean_squared_error(y_test_pred, y_test)

        # Train_RMSE = mean_squared_error(y_train_pred, y_train)
        # Test_RMSE = mean_squared_error(y_test_pred, y_test)
        # train_RMSE = sqrt(Train_RMSE)
        # test_RMSE = sqrt(Test_RMSE)
        
        train_MAPE = mean_absolute_percentage_error(y_train_pred, y_train)
        test_MAPE = mean_absolute_percentage_error(y_test_pred, y_test)

        with mlflow.start_run():
            mlflow.log_param('n_estimators', l)
            mlflow.log_param('max_depth', i)
            mlflow.log_param('min_sample_split', j)
            mlflow.log_param('min_samples_leaf', k)

            mlflow.log_metric('train_MeanAbsoluteError', train_MAE)
            mlflow.log_metric('test_MeanAbsoluteError', test_MAE)

            # mlflow.log_metric('train_MeanSquaredError', train_MSE)
            # mlflow.log_metric('test_MeanSquaredError', test_MSE)

            # mlflow.log_metric('train_RootMeanSquaredError', train_RMSE)
            # mlflow.log_metric('test_RootMeanSquaredError', test_RMSE)

            mlflow.log_metric('train_MeanAbsolutePercentageError', train_MAPE)
            mlflow.log_metric('test_MeanAbsolutePercentageError', test_MAPE)

            mlflow.sklearn.log_model(model_rf, 'model')
# randomforest()