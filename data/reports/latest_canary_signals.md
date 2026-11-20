# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T21:52:34.883362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.13` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0073` n `13`; crypto_alt avg `0.4746` n `239`; crypto_major avg `0.443` n `8`; equity avg `0.3025` n `166`; fx avg `0.0` n `6`; index avg `0.0304` n `27`; metal avg `0.0709` n `20`; unknown avg `0.8363` n `1262`
- 1h: commodity avg `-0.0405` n `13`; crypto_alt avg `1.2752` n `239`; crypto_major avg `1.4188` n `8`; equity avg `0.8743` n `166`; fx avg `0.0099` n `6`; index avg `0.1091` n `27`; metal avg `0.06` n `20`; unknown avg `0.4291` n `1228`
- 4h: commodity avg `0.4824` n `13`; crypto_alt avg `0.6917` n `239`; crypto_major avg `0.2061` n `8`; equity avg `-0.4603` n `166`; fx avg `-0.0152` n `6`; index avg `-0.1263` n `27`; metal avg `0.0569` n `20`; unknown avg `2.6584` n `1218`
- 24h: commodity avg `0.2605` n `13`; crypto_alt avg `-4.7785` n `239`; crypto_major avg `-5.2316` n `8`; equity avg `-6.2196` n `166`; fx avg `0.0013` n `6`; index avg `-0.701` n `27`; metal avg `-0.8142` n `20`; unknown avg `34.1897` n `1135`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
