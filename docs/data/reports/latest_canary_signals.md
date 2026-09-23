# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T06:22:38.155342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0427` n `12`; crypto_alt avg `0.2867` n `234`; crypto_major avg `0.1999` n `8`; equity avg `-0.0036` n `140`; fx avg `0.0308` n `6`; index avg `-0.0041` n `26`; metal avg `-0.026` n `20`; unknown avg `-0.0614` n `945`
- 1h: commodity avg `0.0455` n `12`; crypto_alt avg `0.1722` n `234`; crypto_major avg `-0.1174` n `8`; equity avg `-0.0065` n `140`; fx avg `0.0545` n `6`; index avg `0.0139` n `26`; metal avg `-0.0913` n `20`; unknown avg `0.1269` n `927`
- 4h: commodity avg `-0.048` n `12`; crypto_alt avg `1.1482` n `234`; crypto_major avg `0.4267` n `8`; equity avg `0.1377` n `140`; fx avg `0.0482` n `6`; index avg `0.0396` n `26`; metal avg `-0.0767` n `20`; unknown avg `-0.182` n `921`
- 24h: commodity avg `-0.1945` n `12`; crypto_alt avg `4.513` n `234`; crypto_major avg `2.3987` n `8`; equity avg `1.414` n `140`; fx avg `-0.1254` n `6`; index avg `0.1459` n `26`; metal avg `0.2052` n `20`; unknown avg `2.5378` n `840`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.16`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
