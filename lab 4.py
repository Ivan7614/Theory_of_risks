import numpy as np
import pandas as pd
from scipy.optimize import minimize

data = {
    "Жидычівський ЦПК": [0.16, 0.16, 0.16, 0.2, 0.25, 0.1, 0.25, 0.1, 0.08, 0.07, 0.15],
    "Запоріжтранспорт": [0.15, 0.12, 0.15, 0.1, 0.1, 0.09, 0.08, 0.12, 0.11, 0.1, 0.18],
    "Пивзавод 'Рогань'": [40, 37, 35, 40, 40, 33, 30, 35, 33, 30, 60]
}

returns_df = pd.DataFrame(data)
returns_df["Пивзавод 'Рогань'"] = returns_df["Пивзавод 'Рогань'"].pct_change().fillna(0)

mean_returns = returns_df.mean()
risks = returns_df.std()
cov_matrix = returns_df.cov()

def portfolio_variance(weights, cov_matrix):
    return np.dot(weights.T, np.dot(cov_matrix, weights))

def target_return_constraint(weights, mean_returns, target_return):
    return np.dot(weights, mean_returns) - target_return

def weight_sum_constraint(weights):
    return np.sum(weights) - 1

n_assets = len(mean_returns)
constraints = ({
    'type': 'eq',
    'fun': weight_sum_constraint
}, {
    'type': 'eq',
    'fun': target_return_constraint,
    'args': (mean_returns, 0.05)
})
bounds = tuple((0, 1) for _ in range(n_assets))

result = minimize(
    portfolio_variance,
    n_assets * [1. / n_assets],
    args=(cov_matrix,),
    method='SLSQP',
    bounds=bounds,
    constraints=constraints
)

optimal_weights = result.x
optimal_weights
