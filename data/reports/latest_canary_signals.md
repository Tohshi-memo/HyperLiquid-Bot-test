# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T17:07:25.324510+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0809` n `12`; crypto_alt avg `-0.033` n `232`; crypto_major avg `-0.0271` n `8`; equity avg `-0.0194` n `128`; fx avg `-0.0048` n `6`; index avg `0.0013` n `26`; metal avg `-0.0275` n `20`; unknown avg `-0.0351` n `792`
- 1h: commodity avg `0.0619` n `12`; crypto_alt avg `0.2955` n `232`; crypto_major avg `0.2706` n `8`; equity avg `0.3026` n `128`; fx avg `-0.012` n `6`; index avg `0.0385` n `26`; metal avg `0.0052` n `20`; unknown avg `-0.1245` n `792`
- 4h: commodity avg `0.1917` n `12`; crypto_alt avg `0.4954` n `232`; crypto_major avg `0.7399` n `8`; equity avg `0.5093` n `128`; fx avg `0.0019` n `6`; index avg `-0.0546` n `26`; metal avg `-0.1274` n `20`; unknown avg `0.1197` n `790`
- 24h: commodity avg `0.5926` n `12`; crypto_alt avg `-1.5688` n `231`; crypto_major avg `-1.8481` n `8`; equity avg `-0.4808` n `128`; fx avg `-0.1145` n `6`; index avg `-0.2254` n `26`; metal avg `-0.5746` n `20`; unknown avg `0.0789` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.052`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
