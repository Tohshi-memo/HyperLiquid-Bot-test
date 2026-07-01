# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T03:22:30.636191+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.5` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0007` n `12`; crypto_alt avg `-0.2809` n `228`; crypto_major avg `-0.3531` n `8`; equity avg `-0.057` n `88`; fx avg `0.0126` n `6`; index avg `-0.0271` n `23`; metal avg `-0.0074` n `20`; unknown avg `-0.0782` n `765`
- 1h: commodity avg `0.0175` n `12`; crypto_alt avg `0.1017` n `228`; crypto_major avg `-0.0261` n `8`; equity avg `0.2434` n `88`; fx avg `0.0168` n `6`; index avg `0.026` n `23`; metal avg `0.0331` n `20`; unknown avg `-0.2181` n `765`
- 4h: commodity avg `-0.072` n `12`; crypto_alt avg `0.5444` n `228`; crypto_major avg `0.6024` n `8`; equity avg `-0.6102` n `88`; fx avg `0.1017` n `6`; index avg `-0.2337` n `23`; metal avg `-0.3555` n `20`; unknown avg `0.1313` n `765`
- 24h: commodity avg `0.0302` n `12`; crypto_alt avg `-1.2482` n `228`; crypto_major avg `-0.9166` n `8`; equity avg `0.5981` n `88`; fx avg `0.1749` n `6`; index avg `0.0032` n `23`; metal avg `-0.07` n `20`; unknown avg `6.4583` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
