# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T02:00:27.088082+00:00`
- Correlation status: `ready`
- Asset price records: `31`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0197` n `7`; crypto_alt avg `0.0421` n `223`; crypto_major avg `-0.0291` n `7`; equity avg `0.0565` n `42`; fx avg `0.0013` n `4`; index avg `-0.0084` n `9`; metal avg `0.0041` n `7`; unknown avg `0.0399` n `311`
- 1h: commodity avg `-0.0593` n `7`; crypto_alt avg `0.1664` n `223`; crypto_major avg `0.0527` n `7`; equity avg `0.0821` n `42`; fx avg `-0.0008` n `4`; index avg `0.014` n `9`; metal avg `0.012` n `7`; unknown avg `0.2636` n `311`
- 4h: commodity avg `0.0511` n `7`; crypto_alt avg `0.0511` n `223`; crypto_major avg `0.0244` n `7`; equity avg `0.1924` n `42`; fx avg `0.0528` n `4`; index avg `-0.0526` n `9`; metal avg `-0.0002` n `7`; unknown avg `0.0278` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6695`, n `27`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6453`, n `27`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5283`, n `27`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5209`, n `27`, strong_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.4787`, n `27`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4785`, n `27`, moderate_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.4729`, n `27`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3762`, n `27`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3569`, n `27`, moderate_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2899`, n `27`, moderate_sample_signal
