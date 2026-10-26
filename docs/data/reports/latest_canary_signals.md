# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T12:52:27.652268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.016` n `13`; crypto_alt avg `-0.0299` n `237`; crypto_major avg `-0.0816` n `8`; equity avg `-0.0255` n `152`; fx avg `-0.0029` n `6`; index avg `0.0016` n `26`; metal avg `-0.0574` n `20`; unknown avg `3.2707` n `1240`
- 1h: commodity avg `-0.045` n `13`; crypto_alt avg `0.2509` n `237`; crypto_major avg `0.0891` n `8`; equity avg `0.2127` n `152`; fx avg `-0.0022` n `6`; index avg `0.0108` n `26`; metal avg `-0.0235` n `20`; unknown avg `16.5069` n `1234`
- 4h: commodity avg `0.0551` n `13`; crypto_alt avg `0.1612` n `237`; crypto_major avg `0.2604` n `8`; equity avg `0.6741` n `152`; fx avg `0.0085` n `6`; index avg `0.0701` n `26`; metal avg `-0.0096` n `20`; unknown avg `1.8458` n `1234`
- 24h: commodity avg `-0.3855` n `13`; crypto_alt avg `0.4031` n `237`; crypto_major avg `0.3635` n `8`; equity avg `0.1932` n `152`; fx avg `0.0358` n `6`; index avg `0.0758` n `26`; metal avg `0.1595` n `20`; unknown avg `0.1714` n `977`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2554`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.213`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
