# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T19:22:24.440826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0026` n `12`; crypto_alt avg `-0.0504` n `231`; crypto_major avg `0.1487` n `8`; equity avg `-0.1359` n `122`; fx avg `-0.0023` n `6`; index avg `-0.0179` n `25`; metal avg `0.0433` n `20`; unknown avg `0.005` n `795`
- 1h: commodity avg `0.08` n `12`; crypto_alt avg `-0.3227` n `231`; crypto_major avg `-0.1485` n `8`; equity avg `-0.0186` n `122`; fx avg `-0.0029` n `6`; index avg `0.0082` n `25`; metal avg `0.1017` n `20`; unknown avg `-0.1214` n `795`
- 4h: commodity avg `0.1151` n `12`; crypto_alt avg `-0.0156` n `231`; crypto_major avg `0.3363` n `8`; equity avg `0.0265` n `122`; fx avg `-0.009` n `6`; index avg `0.0064` n `25`; metal avg `0.1719` n `20`; unknown avg `-0.1219` n `795`
- 24h: commodity avg `-0.5868` n `12`; crypto_alt avg `-0.1346` n `231`; crypto_major avg `1.2602` n `8`; equity avg `1.6102` n `122`; fx avg `0.0497` n `6`; index avg `0.1552` n `25`; metal avg `0.0365` n `20`; unknown avg `-0.5218` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
