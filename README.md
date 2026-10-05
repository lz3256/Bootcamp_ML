# Machine Learning Data Collection

A collection of three public datasets for exploratory analysis and machine-learning exercises. The original repository contains dataset files; this update adds source attribution, loading notes, and a reproducible CSV inspection script. It does not claim completed model experiments.

## Dataset guide

| File | Dataset | Main use | Loading detail |
| --- | --- | --- | --- |
| `AirQualityUCI.csv` | [UCI Air Quality](https://archive.ics.uci.edu/dataset/360/air+quality) | Sensor measurements and concentration regression | Semicolon delimiter, decimal comma, `-200` missing-value marker, trailing empty columns/rows |
| `Online Retail.xlsx` | [UCI Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail) | Transaction analysis and customer segmentation | Invoice lines; cancellations and missing customer IDs need explicit treatment |
| `energydata_complete.csv` | [UCI Appliances Energy Prediction](https://archive.ics.uci.edu/dataset/374/appliances+energy+prediction) | Energy-demand regression with room/weather measurements | Ten-minute timestamps; split chronologically for forecasting |

The retail worksheet range contains 541,909 data rows and eight columns. The energy CSV contains 19,735 observations. Air-quality physical CSV rows include trailing empty records; use the inspection report for its non-empty date rows rather than counting every line as an observation.

## Inspect the CSVs

The inspection uses only Python's standard library, keeps source files unchanged, and reports physical/non-empty row counts, time endpoints, columns, and missing-value markers:

```bash
python3 scripts/inspect_data.py
```

See [the recorded inspection](reports/data_inventory.json) and [data notes](docs/DATA_GUIDE.md). Inspection is a data-quality entry point, not a fitted-model benchmark.

## Analysis starting points

- **Air quality:** audit missing-marker prevalence by sensor, then compare a simple concentration regression with a stronger baseline on later dates.
- **Retail:** distinguish cancellations from completed purchases before building customer-level recency, frequency, and monetary summaries.
- **Energy:** compare chronological mean/persistence baselines with regression models; exclude future target information from predictors.

These are proposed exercises. No trained models, completed notebooks, or model-performance results are present in the original repository.

## Attribution

Air Quality: Saverio Vito, UCI dataset DOI `10.24432/C59K5F`. Online Retail: Daqing Chen, DOI `10.24432/C5BW33`. Appliances Energy Prediction: Luis Candanedo, DOI `10.24432/C5VC8G`. Follow each linked source's attribution and usage terms; dataset permissions do not automatically license this repository's own code.

Repository maintained by [@lz3256](https://github.com/lz3256). The catalog and inspection entry point were prepared with OpenAI Codex.
