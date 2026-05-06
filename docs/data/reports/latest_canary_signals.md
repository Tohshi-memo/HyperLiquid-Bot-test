# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T13:22:28.550799+00:00`
- Correlation status: `ready`
- Asset price records: `457`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0099` n `7`; crypto_alt avg `-0.0953` n `223`; crypto_major avg `-0.0461` n `7`; equity avg `-0.017` n `47`; fx avg `-0.0136` n `4`; index avg `0.026` n `6`; metal avg `-0.0777` n `7`; unknown avg `-0.0138` n `313`
- 1h: commodity avg `0.4049` n `7`; crypto_alt avg `-0.5855` n `223`; crypto_major avg `-0.8588` n `7`; equity avg `-0.4924` n `47`; fx avg `0.0358` n `4`; index avg `-0.1951` n `6`; metal avg `-0.1047` n `7`; unknown avg `1.2608` n `313`
- 4h: commodity avg `0.0686` n `7`; crypto_alt avg `-0.3168` n `223`; crypto_major avg `0.0563` n `7`; equity avg `-0.4728` n `47`; fx avg `0.0374` n `4`; index avg `-0.0529` n `6`; metal avg `-0.1194` n `7`; unknown avg `0.1975` n `313`
- 24h: commodity avg `-2.4617` n `7`; crypto_alt avg `2.5834` n `223`; crypto_major avg `1.4996` n `7`; equity avg `2.3793` n `47`; fx avg `-0.5696` n `4`; index avg `2.3187` n `6`; metal avg `2.0207` n `7`; unknown avg `2.9982` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1647`, n `453`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1588`, n `453`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1411`, n `453`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.125`, n `453`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1188`, n `453`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1153`, n `453`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0951`, n `449`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0888`, n `453`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0883`, n `453`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.087`, n `449`, weak_sample_signal
