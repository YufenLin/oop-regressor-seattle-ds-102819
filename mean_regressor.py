class MeanRegressor():
    def __init__(self, y_mean=None,pred=None):
        self.y_mean = y_mean

    def fit(self, X, y):
        self.y_mean = y.mean()
        
    def predict(self, X):
        mean_list=[]
        for i in range(X.shape[0]):
            mean_list.append(self.y_mean)
       
        return mean_list
    
    def score(self, X, y):
        import numpy as np

        res_sum_sqr = 0
        sum_sqr = 0

        y_array = np.array(y)
        y_hat_array = np.array(self.predict(X))
        
        res_sum_sqr = ((y_array - y_hat_array) ** 2).sum()
        sum_sqr = ((y_array - y.mean()) ** 2).sum()
        
        r2 = 1 - (res_sum_sqr/sum_sqr)
        
        return r2