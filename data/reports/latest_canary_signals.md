# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T17:07:31.536485+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `-0.012` n `230`; crypto_major avg `-0.0663` n `8`; equity avg `0.0319` n `102`; fx avg `0.015` n `6`; index avg `0.0227` n `25`; metal avg `0.0191` n `20`; unknown avg `-0.0398` n `780`
- 1h: commodity avg `0.0414` n `12`; crypto_alt avg `0.1353` n `230`; crypto_major avg `-0.0613` n `8`; equity avg `0.5812` n `102`; fx avg `0.0426` n `6`; index avg `0.1228` n `25`; metal avg `-0.0053` n `20`; unknown avg `-0.2185` n `780`
- 4h: commodity avg `-0.2528` n `12`; crypto_alt avg `-0.0835` n `230`; crypto_major avg `-1.1244` n `8`; equity avg `-1.7478` n `102`; fx avg `-0.0385` n `6`; index avg `-0.1525` n `25`; metal avg `-0.0111` n `20`; unknown avg `-0.0308` n `780`
- 24h: commodity avg `0.0239` n `12`; crypto_alt avg `-0.1997` n `230`; crypto_major avg `-1.8795` n `8`; equity avg `0.4158` n `102`; fx avg `0.1381` n `6`; index avg `0.2817` n `25`; metal avg `-0.3786` n `20`; unknown avg `0.5503` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
