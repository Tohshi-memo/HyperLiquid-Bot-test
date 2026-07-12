# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T19:22:27.723958+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0285` n `12`; crypto_alt avg `0.0361` n `230`; crypto_major avg `-0.0181` n `8`; equity avg `0.0259` n `92`; fx avg `-0.0135` n `6`; index avg `0.0096` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.0191` n `765`
- 1h: commodity avg `-0.0763` n `12`; crypto_alt avg `0.1607` n `230`; crypto_major avg `0.2453` n `8`; equity avg `0.0826` n `92`; fx avg `0.0147` n `6`; index avg `-0.0163` n `25`; metal avg `-0.006` n `20`; unknown avg `-0.0704` n `765`
- 4h: commodity avg `0.1145` n `12`; crypto_alt avg `-0.1252` n `230`; crypto_major avg `0.0949` n `8`; equity avg `0.0196` n `92`; fx avg `-0.0133` n `6`; index avg `0.0141` n `25`; metal avg `-0.0232` n `20`; unknown avg `-0.1868` n `759`
- 24h: commodity avg `0.5704` n `12`; crypto_alt avg `-1.4054` n `230`; crypto_major avg `-0.566` n `8`; equity avg `-0.1482` n `92`; fx avg `0.0189` n `6`; index avg `-0.0934` n `25`; metal avg `-0.1069` n `20`; unknown avg `0.1575` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1794`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
