# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T04:37:31.082381+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0544` n `12`; crypto_alt avg `0.0221` n `232`; crypto_major avg `0.0798` n `8`; equity avg `0.0907` n `133`; fx avg `-0.0025` n `6`; index avg `0.017` n `26`; metal avg `0.0401` n `20`; unknown avg `18.6983` n `793`
- 1h: commodity avg `-0.0457` n `12`; crypto_alt avg `0.2006` n `232`; crypto_major avg `0.2327` n `8`; equity avg `0.1845` n `133`; fx avg `0.0116` n `6`; index avg `0.0548` n `26`; metal avg `0.0066` n `20`; unknown avg `8.8202` n `791`
- 4h: commodity avg `0.0134` n `12`; crypto_alt avg `-0.4476` n `232`; crypto_major avg `-0.1574` n `8`; equity avg `0.2784` n `133`; fx avg `0.0237` n `6`; index avg `0.0689` n `26`; metal avg `-0.0891` n `20`; unknown avg `0.8405` n `791`
- 24h: commodity avg `-0.1167` n `12`; crypto_alt avg `2.9475` n `232`; crypto_major avg `4.6763` n `8`; equity avg `1.5066` n `133`; fx avg `-0.0695` n `6`; index avg `0.2382` n `26`; metal avg `0.4299` n `20`; unknown avg `0.9738` n `736`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
