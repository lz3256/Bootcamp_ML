"""Inspect the two tracked CSV datasets without altering the inputs."""
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[1]

def inspect(path, delimiter, missing_marker=None):
    with path.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        fields = [c for c in reader.fieldnames if c]
        physical = valid = 0
        first = last = None
        missing = {c: 0 for c in fields}
        sentinels = {c: 0 for c in fields}
        date_key = 'Date' if 'Date' in fields else 'date'
        for row in reader:
            physical += 1
            date = (row.get(date_key) or '').strip()
            if not date:
                continue
            valid += 1
            first = first or date
            last = date
            for c in fields:
                value = (row.get(c) or '').strip()
                if not value:
                    missing[c] += 1
                elif missing_marker is not None:
                    try:
                        if float(value.replace(',', '.')) == missing_marker:
                            sentinels[c] += 1
                    except ValueError:
                        pass
    return {'file':path.name, 'physical_data_rows':physical,
            'rows_with_date':valid, 'first_date':first, 'last_date':last,
            'columns':fields, 'blank_cells_by_column':missing,
            'missing_marker':missing_marker, 'marker_cells_by_column':sentinels}

if __name__ == '__main__':
    report = {'scope':'CSV inventory; no fitted models or Excel row-level audit',
              'datasets':[inspect(ROOT/'AirQualityUCI.csv',';',-200),
                          inspect(ROOT/'energydata_complete.csv',',')]}
    print(json.dumps(report, indent=2, ensure_ascii=False))
