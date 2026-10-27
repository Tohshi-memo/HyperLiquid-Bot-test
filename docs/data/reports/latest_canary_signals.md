# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T19:52:30.679156+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0239` n `13`; crypto_alt avg `-0.045` n `238`; crypto_major avg `-0.0248` n `8`; equity avg `-0.1865` n `154`; fx avg `-0.001` n `6`; index avg `-0.0309` n `27`; metal avg `-0.0088` n `20`; unknown avg `9.659` n `1238`
- 1h: commodity avg `0.0966` n `13`; crypto_alt avg `-0.0158` n `238`; crypto_major avg `0.0861` n `8`; equity avg `-0.0091` n `154`; fx avg `0.0098` n `6`; index avg `0.0227` n `27`; metal avg `0.0842` n `20`; unknown avg `113.3108` n `1234`
- 4h: commodity avg `-0.0253` n `13`; crypto_alt avg `0.2276` n `238`; crypto_major avg `0.3321` n `8`; equity avg `0.105` n `154`; fx avg `0.0003` n `6`; index avg `-0.012` n `27`; metal avg `-0.0039` n `20`; unknown avg `1.9652` n `1228`
- 24h: commodity avg `-0.3574` n `13`; crypto_alt avg `1.2057` n `237`; crypto_major avg `1.3965` n `8`; equity avg `1.8214` n `154`; fx avg `-0.0543` n `6`; index avg `0.4316` n `27`; metal avg `0.2124` n `20`; unknown avg `26.1429` n `1044`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2309`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1964`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
