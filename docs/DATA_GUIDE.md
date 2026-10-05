# Dataset Loading and Analysis Notes

## Air quality

The CSV uses `;` separators and decimal commas. Drop columns with empty headers and records with an empty date before counting observations. Replace numerical `-200` sentinels with missing values after parsing. Join `Date` and `Time` explicitly, using day-first dates and the dotted hour format. Missingness and sensor drift can affect time-based evaluation.

## Online retail

The eight fields are InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, and Country. The UCI documentation identifies invoice numbers starting with C as cancellations. Treat negative quantities, zero prices, missing customer IDs, and non-product codes according to a documented analysis question. A row is an invoice line, not a unique order or customer. Keep an explicit cutoff when computing customer summaries intended for later prediction.

## Appliances energy

The CSV contains date, Appliances, lights, room temperatures/humidities, weather measurements, and the `rv1`/`rv2` random variables supplied by the dataset. For energy prediction, use Appliances as the target and document which contemporaneous inputs would actually be available at the prediction time. Random columns can serve as negative controls; do not describe them as measured household factors. Keep validation later than training for a temporal forecasting task.

## Minimal pandas loading examples

```python
import pandas as pd

air = pd.read_csv('AirQualityUCI.csv', sep=';', decimal=',')
air = air.loc[air['Date'].notna()].dropna(axis=1, how='all')
air = air.replace(-200, float('nan'))
retail = pd.read_excel('Online Retail.xlsx', engine='openpyxl')
energy = pd.read_csv('energydata_complete.csv', parse_dates=['date'])
```

Pandas and openpyxl are optional analysis dependencies. The supplied inspection script does not need them.
