# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T21:52:58.922830+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `12`; crypto_alt avg `-0.0002` n `230`; crypto_major avg `-0.0153` n `8`; equity avg `0.0492` n `94`; fx avg `0.0093` n `6`; index avg `-0.0008` n `25`; metal avg `0.0126` n `20`; unknown avg `-0.0185` n `768`
- 1h: commodity avg `-0.0102` n `12`; crypto_alt avg `0.252` n `230`; crypto_major avg `0.1256` n `8`; equity avg `0.0604` n `94`; fx avg `-0.0004` n `6`; index avg `0.0351` n `25`; metal avg `0.0552` n `20`; unknown avg `0.1002` n `768`
- 4h: commodity avg `0.2662` n `12`; crypto_alt avg `0.3012` n `230`; crypto_major avg `0.3254` n `8`; equity avg `0.0965` n `94`; fx avg `-0.0108` n `6`; index avg `0.0094` n `25`; metal avg `-0.0448` n `20`; unknown avg `-0.1313` n `768`
- 24h: commodity avg `-0.225` n `12`; crypto_alt avg `-0.8403` n `230`; crypto_major avg `-1.9042` n `8`; equity avg `-3.6878` n `94`; fx avg `-0.1695` n `6`; index avg `-0.4878` n `25`; metal avg `-0.8106` n `20`; unknown avg `-0.3763` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
