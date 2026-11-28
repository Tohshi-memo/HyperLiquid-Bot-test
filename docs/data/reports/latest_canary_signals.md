# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T10:37:30.282754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.38` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0014` n `13`; crypto_alt avg `-0.0961` n `239`; crypto_major avg `-0.2239` n `8`; equity avg `-0.0599` n `168`; fx avg `-0.0023` n `6`; index avg `-0.004` n `27`; metal avg `-0.0045` n `20`; unknown avg `0.586` n `1269`
- 1h: commodity avg `0.0098` n `13`; crypto_alt avg `-0.1814` n `239`; crypto_major avg `-0.37` n `8`; equity avg `0.006` n `168`; fx avg `-0.0046` n `6`; index avg `0.0058` n `27`; metal avg `0.0117` n `20`; unknown avg `177.6318` n `1263`
- 4h: commodity avg `-0.021` n `13`; crypto_alt avg `-0.5208` n `239`; crypto_major avg `-0.9001` n `8`; equity avg `-0.058` n `168`; fx avg `-0.0147` n `6`; index avg `-0.0091` n `27`; metal avg `0.021` n `20`; unknown avg `0.6677` n `1215`
- 24h: commodity avg `-0.64` n `13`; crypto_alt avg `-3.3721` n `239`; crypto_major avg `-3.4844` n `8`; equity avg `-0.4735` n `168`; fx avg `-0.0932` n `6`; index avg `0.0127` n `27`; metal avg `-0.2668` n `20`; unknown avg `190.6779` n `1087`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
