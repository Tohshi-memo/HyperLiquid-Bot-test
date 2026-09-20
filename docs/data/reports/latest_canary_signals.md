# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T15:52:29.678410+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.02` n `12`; crypto_alt avg `0.2536` n `234`; crypto_major avg `0.2082` n `8`; equity avg `0.0861` n `140`; fx avg `0.0318` n `6`; index avg `0.0048` n `26`; metal avg `-0.0007` n `20`; unknown avg `2.6824` n `943`
- 1h: commodity avg `0.0021` n `12`; crypto_alt avg `0.7093` n `234`; crypto_major avg `0.4567` n `8`; equity avg `0.1419` n `140`; fx avg `0.0099` n `6`; index avg `0.0011` n `26`; metal avg `0.0007` n `20`; unknown avg `5.5513` n `941`
- 4h: commodity avg `0.0563` n `12`; crypto_alt avg `0.5783` n `234`; crypto_major avg `0.4616` n `8`; equity avg `0.1301` n `140`; fx avg `0.0092` n `6`; index avg `0.0077` n `26`; metal avg `-0.0024` n `20`; unknown avg `2.2764` n `935`
- 24h: commodity avg `0.4426` n `12`; crypto_alt avg `-1.4471` n `234`; crypto_major avg `-1.9212` n `8`; equity avg `-0.1669` n `140`; fx avg `-0.0138` n `6`; index avg `-0.0528` n `26`; metal avg `-0.0362` n `20`; unknown avg `170.0282` n `819`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
