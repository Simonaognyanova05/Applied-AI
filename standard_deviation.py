import json
import math
import statistics
from pathlib import Path


def main():
    dataset = Path(__file__).with_name('students_1000_30percent_missing.json')
    records = json.loads(dataset.read_text(encoding='utf-8'))
    features = ['age', 'study_hours', 'attendance', 'sleep_hours', 'previous_grade']

    # Sample standard deviation uses n - 1 in the denominator.
    # Skip missing values, without replacing them with zero.
    print('Feature          Count  Missing  Sample std (ddof=1)')
    for feature in features:
        values = [row[feature] for row in records
                  if isinstance(row.get(feature), (int, float))
                  and not isinstance(row[feature], bool)
                  and math.isfinite(row[feature])]
        deviation = statistics.stdev(values) if len(values) >= 2 else math.nan
        print(f'{feature:<16} {len(values):>5}  {len(records) - len(values):>7}  {deviation:>19.4f}')


if __name__ == '__main__':
    main()
