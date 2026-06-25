# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T19:07:27.168139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0092` n `12`; crypto_alt avg `-0.2388` n `228`; crypto_major avg `-0.3703` n `8`; equity avg `-0.2873` n `86`; fx avg `-0.0018` n `6`; index avg `-0.0389` n `23`; metal avg `-0.048` n `20`; unknown avg `-0.1627` n `765`
- 1h: commodity avg `-0.062` n `12`; crypto_alt avg `-0.7307` n `228`; crypto_major avg `-0.704` n `8`; equity avg `-0.275` n `86`; fx avg `-0.0014` n `6`; index avg `-0.0322` n `23`; metal avg `0.0205` n `20`; unknown avg `-0.1347` n `765`
- 4h: commodity avg `0.1405` n `12`; crypto_alt avg `-0.1649` n `228`; crypto_major avg `0.6245` n `8`; equity avg `-0.2026` n `86`; fx avg `0.0391` n `6`; index avg `-0.0053` n `23`; metal avg `0.0922` n `20`; unknown avg `0.6298` n `765`
- 24h: commodity avg `0.5321` n `12`; crypto_alt avg `-0.0682` n `228`; crypto_major avg `0.0046` n `8`; equity avg `0.5237` n `86`; fx avg `0.0708` n `6`; index avg `0.5097` n `23`; metal avg `0.8104` n `20`; unknown avg `0.4898` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
