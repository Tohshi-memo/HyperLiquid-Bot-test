# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T05:52:35.252417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.092` n `12`; crypto_alt avg `-0.1772` n `228`; crypto_major avg `-0.2458` n `8`; equity avg `-0.1928` n `86`; fx avg `-0.0008` n `6`; index avg `-0.0636` n `23`; metal avg `-0.049` n `20`; unknown avg `1.1156` n `765`
- 1h: commodity avg `0.176` n `12`; crypto_alt avg `0.1531` n `228`; crypto_major avg `0.0459` n `8`; equity avg `0.3626` n `86`; fx avg `-0.0168` n `6`; index avg `0.1192` n `23`; metal avg `0.1168` n `20`; unknown avg `124.1922` n `765`
- 4h: commodity avg `0.0462` n `12`; crypto_alt avg `0.0321` n `228`; crypto_major avg `0.1435` n `8`; equity avg `-0.9864` n `86`; fx avg `-0.0297` n `6`; index avg `-0.2105` n `23`; metal avg `-0.0707` n `20`; unknown avg `1.6492` n `749`
- 24h: commodity avg `0.4935` n `12`; crypto_alt avg `-2.7006` n `228`; crypto_major avg `-2.7879` n `8`; equity avg `-4.142` n `86`; fx avg `0.0471` n `6`; index avg `-0.6729` n `23`; metal avg `0.0722` n `20`; unknown avg `0.6075` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2059`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
