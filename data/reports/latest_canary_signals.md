# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T12:28:19.505579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0641` n `13`; crypto_alt avg `0.6241` n `238`; crypto_major avg `0.5276` n `8`; equity avg `0.308` n `154`; fx avg `-0.0075` n `6`; index avg `0.0598` n `27`; metal avg `0.0502` n `20`; unknown avg `0.2687` n `1234`
- 1h: commodity avg `0.0412` n `13`; crypto_alt avg `0.3248` n `238`; crypto_major avg `0.4149` n `8`; equity avg `0.1766` n `154`; fx avg `0.0192` n `6`; index avg `0.047` n `27`; metal avg `0.035` n `20`; unknown avg `0.6862` n `1226`
- 4h: commodity avg `-0.3656` n `13`; crypto_alt avg `0.1243` n `238`; crypto_major avg `0.4423` n `8`; equity avg `1.0465` n `154`; fx avg `-0.0082` n `6`; index avg `0.1888` n `27`; metal avg `0.1652` n `20`; unknown avg `7.0127` n `1178`
- 24h: commodity avg `-0.1924` n `13`; crypto_alt avg `-0.1123` n `237`; crypto_major avg `0.2556` n `8`; equity avg `0.9906` n `153`; fx avg `-0.0386` n `6`; index avg `0.3698` n `27`; metal avg `-0.2567` n `20`; unknown avg `1021.339` n `1038`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1931`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1888`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
