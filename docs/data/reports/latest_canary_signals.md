# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T03:37:28.184534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0069` n `12`; crypto_alt avg `0.1197` n `230`; crypto_major avg `0.0009` n `8`; equity avg `0.0364` n `108`; fx avg `0.0287` n `6`; index avg `0.0032` n `25`; metal avg `-0.0295` n `20`; unknown avg `-0.126` n `781`
- 1h: commodity avg `0.0483` n `12`; crypto_alt avg `-0.2025` n `230`; crypto_major avg `-0.4634` n `8`; equity avg `0.2806` n `108`; fx avg `0.0052` n `6`; index avg `0.0217` n `25`; metal avg `0.0292` n `20`; unknown avg `0.5091` n `781`
- 4h: commodity avg `-0.0735` n `12`; crypto_alt avg `0.2563` n `230`; crypto_major avg `0.1448` n `8`; equity avg `0.6773` n `108`; fx avg `-0.0873` n `6`; index avg `0.0617` n `25`; metal avg `0.4127` n `20`; unknown avg `-0.2271` n `781`
- 24h: commodity avg `-1.4951` n `12`; crypto_alt avg `0.1915` n `230`; crypto_major avg `0.419` n `8`; equity avg `4.0074` n `108`; fx avg `-0.0113` n `6`; index avg `0.8288` n `25`; metal avg `1.0393` n `20`; unknown avg `0.339` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
