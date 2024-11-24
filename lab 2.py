import pandas as pd

data = {
    "Компанія": ["A.Ink", "B.Ltd", "AT”C"],
    "Вартість ($)": [3400000, 2930000, 2500000],
    "Терміни будівництва (років)": [
        [3, 3.5, 4],  
        [2, 2.5, 4.5],  
        [4, 4.5, 5]  
    ],
    "Ймовірності": [
        [0.5, 0.3, 0.2],  
        [0.4, 0.3, 0.3],  
        [0.1, 0.4, 0.5]   
    ]
}

monthly_risk_cost = 40000

def calculate_average_period(periods, probabilities):
    return sum(p * t for p, t in zip(probabilities, periods))

results = []
for i in range(len(data["Компанія"])):
    avg_period_years = calculate_average_period(data["Терміни будівництва (років)"][i], data["Ймовірності"][i])
    avg_period_months = avg_period_years * 12  
    risk_cost = avg_period_months * monthly_risk_cost 
    total_cost = data["Вартість ($)"][i] + risk_cost 
    results.append({
        "Компанія": data["Компанія"][i],
        "Середній термін будівництва (років)": avg_period_years,
        "Ризик ($)": risk_cost,
        "Загальна вартість ($)": total_cost
    })

results_df = pd.DataFrame(results)

print(results_df)
