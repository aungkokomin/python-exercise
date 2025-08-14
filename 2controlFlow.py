from typing import Iterable, List

def avg(values: Iterable [float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0

result = avg([10.0, 2.0, 3.0, 4.0, 5.0])  # Example usage
print(f"The average is: {result}")