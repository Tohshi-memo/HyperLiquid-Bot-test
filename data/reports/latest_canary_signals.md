# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T13:07:19.683941+00:00`
- Correlation status: `ready`
- Asset price records: `456`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2168` n `7`; crypto_alt avg `-0.6687` n `223`; crypto_major avg `-0.8314` n `7`; equity avg `-0.2075` n `47`; fx avg `0.0407` n `4`; index avg `-0.0484` n `6`; metal avg `-0.1824` n `7`; unknown avg `1.0441` n `313`
- 1h: commodity avg `0.6636` n `7`; crypto_alt avg `-0.3236` n `223`; crypto_major avg `-0.6717` n `7`; equity avg `-0.6329` n `47`; fx avg `0.0663` n `4`; index avg `-0.4819` n `6`; metal avg `-0.017` n `7`; unknown avg `1.3106` n `313`
- 4h: commodity avg `0.1283` n `7`; crypto_alt avg `-0.2619` n `223`; crypto_major avg `-0.146` n `7`; equity avg `-0.5753` n `47`; fx avg `0.0393` n `4`; index avg `-0.1971` n `6`; metal avg `-0.2387` n `7`; unknown avg `1.0959` n `313`
- 24h: commodity avg `-2.5392` n `7`; crypto_alt avg `2.9146` n `223`; crypto_major avg `1.8923` n `7`; equity avg `2.3853` n `47`; fx avg `-0.5443` n `4`; index avg `2.2926` n `6`; metal avg `2.361` n `7`; unknown avg `3.182` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1647`, n `452`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1588`, n `452`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1414`, n `452`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1256`, n `452`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1194`, n `452`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1158`, n `452`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0951`, n `448`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0889`, n `452`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0883`, n `452`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.088`, n `448`, weak_sample_signal
