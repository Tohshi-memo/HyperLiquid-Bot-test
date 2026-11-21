# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T21:07:28.360003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `13`; crypto_alt avg `-0.0002` n `239`; crypto_major avg `0.0359` n `8`; equity avg `0.0418` n `166`; fx avg `-0.0096` n `6`; index avg `0.0055` n `27`; metal avg `0.0003` n `20`; unknown avg `0.1356` n `1236`
- 1h: commodity avg `0.0004` n `13`; crypto_alt avg `0.0508` n `239`; crypto_major avg `0.0131` n `8`; equity avg `0.1103` n `166`; fx avg `-0.0057` n `6`; index avg `0.016` n `27`; metal avg `-0.0078` n `20`; unknown avg `164.2563` n `1224`
- 4h: commodity avg `0.0787` n `13`; crypto_alt avg `0.0461` n `239`; crypto_major avg `0.3481` n `8`; equity avg `0.1786` n `166`; fx avg `0.0042` n `6`; index avg `0.0603` n `27`; metal avg `0.0204` n `20`; unknown avg `0.4555` n `1168`
- 24h: commodity avg `0.0284` n `13`; crypto_alt avg `1.7814` n `239`; crypto_major avg `3.614` n `8`; equity avg `1.6177` n `166`; fx avg `-0.0759` n `6`; index avg `0.2448` n `27`; metal avg `0.2932` n `20`; unknown avg `48.7958` n `1086`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
