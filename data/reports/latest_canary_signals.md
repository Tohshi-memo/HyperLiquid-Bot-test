# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T14:37:31.751576+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0098` n `12`; crypto_alt avg `-0.4804` n `228`; crypto_major avg `-0.6788` n `8`; equity avg `-0.3799` n `86`; fx avg `-0.0009` n `6`; index avg `-0.0867` n `23`; metal avg `-0.152` n `20`; unknown avg `0.1046` n `765`
- 1h: commodity avg `-0.0844` n `12`; crypto_alt avg `0.8471` n `228`; crypto_major avg `1.206` n `8`; equity avg `1.093` n `86`; fx avg `-0.0141` n `6`; index avg `0.1543` n `23`; metal avg `0.3877` n `20`; unknown avg `0.2947` n `765`
- 4h: commodity avg `-0.0386` n `12`; crypto_alt avg `0.3519` n `228`; crypto_major avg `0.6173` n `8`; equity avg `1.0477` n `86`; fx avg `-0.0016` n `6`; index avg `0.1085` n `23`; metal avg `0.3037` n `20`; unknown avg `0.0952` n `765`
- 24h: commodity avg `-0.1232` n `12`; crypto_alt avg `0.8077` n `228`; crypto_major avg `1.6145` n `8`; equity avg `-0.8764` n `86`; fx avg `0.0326` n `6`; index avg `-0.2844` n `23`; metal avg `0.6969` n `20`; unknown avg `0.5754` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.3619`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.2435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.2389`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2012`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
