# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T13:52:26.264474+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0725` n `12`; crypto_alt avg `0.2564` n `230`; crypto_major avg `0.2304` n `8`; equity avg `0.6742` n `109`; fx avg `-0.0005` n `6`; index avg `0.0827` n `25`; metal avg `-0.0566` n `20`; unknown avg `0.1811` n `781`
- 1h: commodity avg `-0.1395` n `12`; crypto_alt avg `0.2632` n `230`; crypto_major avg `0.0333` n `8`; equity avg `0.6596` n `109`; fx avg `0.0022` n `6`; index avg `0.0844` n `25`; metal avg `-0.029` n `20`; unknown avg `0.2225` n `781`
- 4h: commodity avg `0.042` n `12`; crypto_alt avg `0.3884` n `230`; crypto_major avg `-0.1865` n `8`; equity avg `0.2742` n `109`; fx avg `0.0034` n `6`; index avg `0.0319` n `25`; metal avg `-0.2602` n `20`; unknown avg `42.4156` n `781`
- 24h: commodity avg `0.0145` n `12`; crypto_alt avg `0.5302` n `230`; crypto_major avg `-0.6605` n `8`; equity avg `-1.7784` n `109`; fx avg `0.0151` n `6`; index avg `-0.4316` n `25`; metal avg `0.1529` n `20`; unknown avg `113.3483` n `749`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
