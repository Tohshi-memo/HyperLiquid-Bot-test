# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T04:22:24.229593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0197` n `13`; crypto_alt avg `0.2228` n `237`; crypto_major avg `0.1933` n `8`; equity avg `0.0785` n `152`; fx avg `0.0049` n `6`; index avg `0.0162` n `26`; metal avg `0.0071` n `20`; unknown avg `0.3655` n `1238`
- 1h: commodity avg `0.0066` n `13`; crypto_alt avg `-0.0968` n `237`; crypto_major avg `0.0396` n `8`; equity avg `0.1403` n `152`; fx avg `0.0083` n `6`; index avg `0.0551` n `26`; metal avg `-0.0674` n `20`; unknown avg `0.395` n `1232`
- 4h: commodity avg `-0.1434` n `13`; crypto_alt avg `-1.0147` n `237`; crypto_major avg `-0.6591` n `8`; equity avg `-0.8072` n `152`; fx avg `-0.0343` n `6`; index avg `-0.0681` n `26`; metal avg `0.0323` n `20`; unknown avg `0.2744` n `1160`
- 24h: commodity avg `-0.6291` n `13`; crypto_alt avg `-1.7383` n `237`; crypto_major avg `-1.4667` n `8`; equity avg `-0.6919` n `152`; fx avg `0.05` n `6`; index avg `0.0133` n `26`; metal avg `0.1641` n `20`; unknown avg `1.3729` n `987`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.249`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1916`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1538`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
