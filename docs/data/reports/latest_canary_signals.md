# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T08:22:35.608263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0575` n `12`; crypto_alt avg `0.7599` n `234`; crypto_major avg `0.5587` n `8`; equity avg `0.1999` n `141`; fx avg `0.0144` n `6`; index avg `0.0377` n `26`; metal avg `0.0259` n `20`; unknown avg `2.0891` n `944`
- 1h: commodity avg `-0.0433` n `12`; crypto_alt avg `0.9898` n `234`; crypto_major avg `0.5774` n `8`; equity avg `0.1123` n `141`; fx avg `0.0155` n `6`; index avg `0.0089` n `26`; metal avg `0.0855` n `20`; unknown avg `5.5381` n `926`
- 4h: commodity avg `0.0084` n `12`; crypto_alt avg `1.3552` n `234`; crypto_major avg `0.7429` n `8`; equity avg `0.495` n `141`; fx avg `-0.0149` n `6`; index avg `0.1059` n `26`; metal avg `0.1009` n `20`; unknown avg `3.2285` n `904`
- 24h: commodity avg `0.0234` n `12`; crypto_alt avg `3.1463` n `234`; crypto_major avg `1.1372` n `8`; equity avg `1.6006` n `141`; fx avg `-0.1895` n `6`; index avg `0.2596` n `26`; metal avg `0.0272` n `20`; unknown avg `14.4092` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
