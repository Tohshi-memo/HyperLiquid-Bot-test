# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T20:07:32.515736+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0315` n `12`; crypto_alt avg `-0.0712` n `229`; crypto_major avg `-0.1705` n `8`; equity avg `-0.064` n `92`; fx avg `-0.0083` n `6`; index avg `0.0013` n `25`; metal avg `0.0414` n `20`; unknown avg `-0.0902` n `765`
- 1h: commodity avg `-0.0179` n `12`; crypto_alt avg `0.1568` n `229`; crypto_major avg `0.1393` n `8`; equity avg `-0.1646` n `92`; fx avg `-0.0075` n `6`; index avg `-0.0176` n `25`; metal avg `0.0677` n `20`; unknown avg `-0.1483` n `765`
- 4h: commodity avg `0.1465` n `12`; crypto_alt avg `-0.0015` n `229`; crypto_major avg `-0.1159` n `8`; equity avg `0.0487` n `92`; fx avg `-0.0287` n `6`; index avg `0.0509` n `25`; metal avg `-0.015` n `20`; unknown avg `-0.2168` n `765`
- 24h: commodity avg `-0.2306` n `12`; crypto_alt avg `0.6755` n `229`; crypto_major avg `0.7865` n `8`; equity avg `-0.6804` n `92`; fx avg `-0.1537` n `6`; index avg `0.0217` n `25`; metal avg `0.1468` n `20`; unknown avg `-0.1006` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
