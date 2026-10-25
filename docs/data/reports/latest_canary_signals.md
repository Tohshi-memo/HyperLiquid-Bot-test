# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T13:52:30.617884+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0271` n `13`; crypto_alt avg `0.11` n `237`; crypto_major avg `0.1077` n `8`; equity avg `0.01` n `152`; fx avg `0.0106` n `6`; index avg `0.0064` n `26`; metal avg `0.0158` n `20`; unknown avg `0.7238` n `1231`
- 1h: commodity avg `-0.0483` n `13`; crypto_alt avg `-0.0315` n `237`; crypto_major avg `0.03` n `8`; equity avg `0.1178` n `152`; fx avg `0.0092` n `6`; index avg `0.0219` n `26`; metal avg `0.025` n `20`; unknown avg `174.8644` n `1231`
- 4h: commodity avg `-0.0727` n `13`; crypto_alt avg `0.3012` n `237`; crypto_major avg `0.3141` n `8`; equity avg `0.3267` n `152`; fx avg `0.0364` n `6`; index avg `0.0504` n `26`; metal avg `0.063` n `20`; unknown avg `8.0191` n `1221`
- 24h: commodity avg `-0.1688` n `13`; crypto_alt avg `-1.0657` n `237`; crypto_major avg `-0.0452` n `8`; equity avg `0.2006` n `152`; fx avg `0.0159` n `6`; index avg `0.0669` n `26`; metal avg `-0.008` n `20`; unknown avg `18.1809` n `1080`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2237`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1721`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1702`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
