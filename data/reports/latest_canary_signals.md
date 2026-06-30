# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T23:52:25.766241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `0.0358` n `228`; crypto_major avg `0.0456` n `8`; equity avg `0.0396` n `88`; fx avg `0.0117` n `6`; index avg `-0.0072` n `23`; metal avg `-0.0483` n `20`; unknown avg `-0.1299` n `765`
- 1h: commodity avg `0.0376` n `12`; crypto_alt avg `0.0307` n `228`; crypto_major avg `0.1666` n `8`; equity avg `0.1418` n `88`; fx avg `0.0156` n `6`; index avg `-0.0064` n `23`; metal avg `-0.0973` n `20`; unknown avg `-0.4093` n `765`
- 4h: commodity avg `-0.0075` n `12`; crypto_alt avg `-0.389` n `228`; crypto_major avg `-0.325` n `8`; equity avg `0.2499` n `88`; fx avg `0.006` n `6`; index avg `-0.0252` n `23`; metal avg `-0.2465` n `20`; unknown avg `-0.2899` n `765`
- 24h: commodity avg `0.1816` n `12`; crypto_alt avg `-2.1302` n `228`; crypto_major avg `-2.0599` n `8`; equity avg `1.3153` n `88`; fx avg `0.1286` n `6`; index avg `0.2446` n `23`; metal avg `-0.1862` n `20`; unknown avg `7.6571` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
