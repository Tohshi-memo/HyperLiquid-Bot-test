# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T21:07:30.952784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0066` n `12`; crypto_alt avg `-0.0869` n `232`; crypto_major avg `-0.0424` n `8`; equity avg `0.018` n `134`; fx avg `0.0026` n `6`; index avg `-0.0111` n `26`; metal avg `-0.0011` n `20`; unknown avg `33.5107` n `788`
- 1h: commodity avg `0.0095` n `12`; crypto_alt avg `-0.0789` n `232`; crypto_major avg `-0.1715` n `8`; equity avg `-0.0485` n `134`; fx avg `-0.0007` n `6`; index avg `-0.0227` n `26`; metal avg `0.0025` n `20`; unknown avg `0.1369` n `770`
- 4h: commodity avg `0.0509` n `12`; crypto_alt avg `0.0084` n `232`; crypto_major avg `-0.0392` n `8`; equity avg `0.0234` n `134`; fx avg `-0.039` n `6`; index avg `0.0154` n `26`; metal avg `0.0033` n `20`; unknown avg `1.3662` n `770`
- 24h: commodity avg `0.0963` n `12`; crypto_alt avg `2.7565` n `232`; crypto_major avg `2.3962` n `8`; equity avg `0.2313` n `134`; fx avg `-0.0357` n `6`; index avg `0.0166` n `26`; metal avg `0.0669` n `20`; unknown avg `1281.0193` n `700`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
