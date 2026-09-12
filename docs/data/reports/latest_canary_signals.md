# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T23:37:29.071504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0211` n `12`; crypto_alt avg `-0.0069` n `233`; crypto_major avg `0.0069` n `8`; equity avg `0.0036` n `130`; fx avg `-0.0019` n `6`; index avg `-0.001` n `26`; metal avg `0.0054` n `20`; unknown avg `0.3148` n `835`
- 1h: commodity avg `-0.027` n `12`; crypto_alt avg `0.1546` n `233`; crypto_major avg `0.1242` n `8`; equity avg `0.0043` n `130`; fx avg `-0.0046` n `6`; index avg `-0.0025` n `26`; metal avg `-0.006` n `20`; unknown avg `0.0807` n `833`
- 4h: commodity avg `-0.0357` n `12`; crypto_alt avg `0.1174` n `233`; crypto_major avg `0.1814` n `8`; equity avg `-0.0802` n `130`; fx avg `-0.0052` n `6`; index avg `-0.0139` n `26`; metal avg `-0.0253` n `20`; unknown avg `0.4924` n `793`
- 24h: commodity avg `-0.0951` n `12`; crypto_alt avg `1.4694` n `233`; crypto_major avg `0.2817` n `8`; equity avg `-0.2256` n `130`; fx avg `-0.0123` n `6`; index avg `-0.004` n `26`; metal avg `0.0126` n `20`; unknown avg `0.3545` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.05`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0471`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.044`, n `668`, weak_sample_signal
