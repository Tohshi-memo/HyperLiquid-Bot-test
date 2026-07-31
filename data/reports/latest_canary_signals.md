# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T12:37:37.388578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0882` n `12`; crypto_alt avg `0.0206` n `230`; crypto_major avg `-0.0521` n `8`; equity avg `-0.1371` n `102`; fx avg `-0.0049` n `6`; index avg `-0.0281` n `25`; metal avg `0.0026` n `20`; unknown avg `0.0861` n `780`
- 1h: commodity avg `-0.0111` n `12`; crypto_alt avg `-0.0115` n `230`; crypto_major avg `-0.0314` n `8`; equity avg `-0.56` n `102`; fx avg `-0.0213` n `6`; index avg `-0.0709` n `25`; metal avg `0.0104` n `20`; unknown avg `0.1485` n `780`
- 4h: commodity avg `0.4931` n `12`; crypto_alt avg `-0.4924` n `230`; crypto_major avg `-0.3222` n `8`; equity avg `-0.5601` n `102`; fx avg `0.0673` n `6`; index avg `-0.0758` n `25`; metal avg `-0.1141` n `20`; unknown avg `1.0294` n `780`
- 24h: commodity avg `0.4223` n `12`; crypto_alt avg `-0.6474` n `230`; crypto_major avg `-0.5183` n `8`; equity avg `5.5553` n `102`; fx avg `-0.1028` n `6`; index avg `0.8317` n `25`; metal avg `0.0083` n `20`; unknown avg `1.1616` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
