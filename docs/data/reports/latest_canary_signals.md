# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T01:37:26.512459+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0144` n `12`; crypto_alt avg `0.1236` n `232`; crypto_major avg `0.1529` n `8`; equity avg `0.0143` n `134`; fx avg `-0.0405` n `6`; index avg `-0.0078` n `26`; metal avg `-0.0014` n `20`; unknown avg `-0.1284` n `794`
- 1h: commodity avg `0.0207` n `12`; crypto_alt avg `0.4938` n `232`; crypto_major avg `0.2742` n `8`; equity avg `0.0614` n `134`; fx avg `-0.0101` n `6`; index avg `-0.0007` n `26`; metal avg `-0.0087` n `20`; unknown avg `-0.0687` n `792`
- 4h: commodity avg `0.028` n `12`; crypto_alt avg `0.7663` n `232`; crypto_major avg `0.0213` n `8`; equity avg `0.1442` n `134`; fx avg `-0.0204` n `6`; index avg `0.0078` n `26`; metal avg `-0.0068` n `20`; unknown avg `0.0906` n `786`
- 24h: commodity avg `0.1456` n `12`; crypto_alt avg `3.4039` n `232`; crypto_major avg `2.5283` n `8`; equity avg `0.4794` n `134`; fx avg `-0.0836` n `6`; index avg `0.071` n `26`; metal avg `0.0336` n `20`; unknown avg `0.4482` n `694`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
