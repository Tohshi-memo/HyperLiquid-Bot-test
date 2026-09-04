# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T11:29:39.022621+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0262` n `12`; crypto_alt avg `0.1335` n `232`; crypto_major avg `0.1232` n `8`; equity avg `0.0412` n `133`; fx avg `-0.0` n `6`; index avg `0.0155` n `26`; metal avg `-0.0191` n `20`; unknown avg `-0.1258` n `793`
- 1h: commodity avg `-0.0235` n `12`; crypto_alt avg `0.5358` n `232`; crypto_major avg `0.5274` n `8`; equity avg `0.054` n `133`; fx avg `0.0038` n `6`; index avg `0.0243` n `26`; metal avg `0.0048` n `20`; unknown avg `-0.0194` n `791`
- 4h: commodity avg `-0.1358` n `12`; crypto_alt avg `0.99` n `232`; crypto_major avg `0.5811` n `8`; equity avg `0.4155` n `133`; fx avg `-0.0171` n `6`; index avg `0.0602` n `26`; metal avg `-0.0093` n `20`; unknown avg `-0.0391` n `785`
- 24h: commodity avg `-0.47` n `12`; crypto_alt avg `2.8733` n `232`; crypto_major avg `4.2937` n `8`; equity avg `2.2072` n `133`; fx avg `0.0281` n `6`; index avg `0.4273` n `26`; metal avg `0.4609` n `20`; unknown avg `1.9621` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
