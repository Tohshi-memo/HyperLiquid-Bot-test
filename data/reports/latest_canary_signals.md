# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T01:45:26.892798+00:00`
- Correlation status: `ready`
- Asset price records: `411`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2062` n `7`; crypto_alt avg `0.2164` n `223`; crypto_major avg `-0.0065` n `7`; equity avg `0.0863` n `47`; fx avg `-0.0282` n `4`; index avg `-0.0243` n `6`; metal avg `0.0903` n `7`; unknown avg `-0.0686` n `313`
- 1h: commodity avg `-0.257` n `7`; crypto_alt avg `0.9108` n `223`; crypto_major avg `0.4123` n `7`; equity avg `0.1587` n `47`; fx avg `-0.0167` n `4`; index avg `0.1032` n `6`; metal avg `0.5069` n `7`; unknown avg `0.0772` n `313`
- 4h: commodity avg `-0.6993` n `7`; crypto_alt avg `0.542` n `223`; crypto_major avg `0.0497` n `7`; equity avg `0.5176` n `47`; fx avg `-0.2649` n `4`; index avg `0.6229` n `6`; metal avg `1.3238` n `7`; unknown avg `-0.3235` n `313`
- 24h: commodity avg `-1.6962` n `7`; crypto_alt avg `2.4764` n `223`; crypto_major avg `2.1572` n `7`; equity avg `2.7187` n `47`; fx avg `-0.2149` n `4`; index avg `2.286` n `6`; metal avg `1.8737` n `7`; unknown avg `1.3991` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1873`, n `407`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.181`, n `407`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.129`, n `407`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1251`, n `407`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1149`, n `407`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `407`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.102`, n `403`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0988`, n `407`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.098`, n `407`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0963`, n `403`, weak_sample_signal
