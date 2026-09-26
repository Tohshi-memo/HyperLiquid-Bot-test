# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T09:57:51.449198+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `0.1688` n `234`; crypto_major avg `0.0284` n `8`; equity avg `0.0035` n `141`; fx avg `0.0013` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0035` n `20`; unknown avg `0.9448` n `961`
- 1h: commodity avg `-0.0119` n `12`; crypto_alt avg `-0.2784` n `234`; crypto_major avg `-0.3837` n `8`; equity avg `-0.0402` n `141`; fx avg `0.0275` n `6`; index avg `-0.0008` n `26`; metal avg `-0.0034` n `20`; unknown avg `1.1591` n `959`
- 4h: commodity avg `-0.0669` n `12`; crypto_alt avg `0.4857` n `234`; crypto_major avg `-0.2361` n `8`; equity avg `-0.016` n `141`; fx avg `0.0156` n `6`; index avg `-0.0022` n `26`; metal avg `-0.0098` n `20`; unknown avg `0.1111` n `919`
- 24h: commodity avg `0.0494` n `12`; crypto_alt avg `2.0102` n `234`; crypto_major avg `-0.3668` n `8`; equity avg `-0.8895` n `141`; fx avg `-0.0616` n `6`; index avg `0.0058` n `26`; metal avg `0.0531` n `20`; unknown avg `1121.4521` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
