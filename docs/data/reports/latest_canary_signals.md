# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T16:52:26.655454+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1162` n `12`; crypto_alt avg `0.154` n `230`; crypto_major avg `0.2374` n `8`; equity avg `0.2253` n `92`; fx avg `0.015` n `6`; index avg `0.0349` n `25`; metal avg `0.0049` n `20`; unknown avg `0.0428` n `766`
- 1h: commodity avg `0.2123` n `12`; crypto_alt avg `-0.335` n `230`; crypto_major avg `-0.4078` n `8`; equity avg `-0.5479` n `92`; fx avg `0.0049` n `6`; index avg `-0.0924` n `25`; metal avg `-0.1786` n `20`; unknown avg `0.0162` n `766`
- 4h: commodity avg `0.3846` n `12`; crypto_alt avg `-0.366` n `230`; crypto_major avg `-0.4158` n `8`; equity avg `-0.8187` n `92`; fx avg `-0.0252` n `6`; index avg `-0.1145` n `25`; metal avg `-0.4004` n `20`; unknown avg `-0.0531` n `766`
- 24h: commodity avg `0.2477` n `12`; crypto_alt avg `-1.8623` n `230`; crypto_major avg `-2.8574` n `8`; equity avg `-2.9435` n `92`; fx avg `-0.0829` n `6`; index avg `-0.6065` n `25`; metal avg `-0.5736` n `20`; unknown avg `-0.1038` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
