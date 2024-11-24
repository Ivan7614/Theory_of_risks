lotteries = {
    "L1": {"values": [0, 20], "probabilities": [0.5, 0.5]},
    "L2": {"values": [10, 30], "probabilities": [0.5, 0.5]}
}

def utility(x):
    return 0.1 * x**2

results = []

for name, lottery in lotteries.items():
    values = lottery["values"]
    probabilities = lottery["probabilities"]

    expected_value = sum(p * x for p, x in zip(probabilities, values))

    expected_utility = sum(p * utility(x) for p, x in zip(probabilities, values))

    deterministic_equivalent = (expected_utility / 0.1)**0.5

    risk_premium = expected_value - deterministic_equivalent

    results.append({
        "Лотерея": name,
        "Ожидаемый выигрыш": expected_value,
        "Ожидаемая полезность": expected_utility,
        "Детерминированный эквивалент": deterministic_equivalent,
        "Премия за риск": risk_premium
    })

import pandas as pd
results_df = pd.DataFrame(results)

print(results_df)
