# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T20:48:13.635766+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.008` n `12`; crypto_alt avg `0.1361` n `232`; crypto_major avg `0.1064` n `8`; equity avg `-0.0123` n `129`; fx avg `-0.0016` n `6`; index avg `0.002` n `26`; metal avg `-0.0025` n `20`; unknown avg `-0.0339` n `793`
- 1h: commodity avg `0.0264` n `12`; crypto_alt avg `0.1171` n `232`; crypto_major avg `-0.0272` n `8`; equity avg `-0.0162` n `129`; fx avg `-0.0071` n `6`; index avg `-0.0169` n `26`; metal avg `-0.0496` n `20`; unknown avg `1.1971` n `779`
- 4h: commodity avg `0.1271` n `12`; crypto_alt avg `0.3773` n `232`; crypto_major avg `0.3608` n `8`; equity avg `0.3366` n `129`; fx avg `0.0046` n `6`; index avg `0.0454` n `26`; metal avg `0.0434` n `20`; unknown avg `-0.1622` n `779`
- 24h: commodity avg `0.1928` n `12`; crypto_alt avg `-0.4861` n `231`; crypto_major avg `-0.4979` n `8`; equity avg `0.0249` n `129`; fx avg `-0.0917` n `6`; index avg `-0.1407` n `26`; metal avg `-0.4351` n `20`; unknown avg `-0.2175` n `746`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
