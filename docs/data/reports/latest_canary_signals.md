# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T15:07:35.611782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.31` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0405` n `13`; crypto_alt avg `-0.1366` n `239`; crypto_major avg `-0.0851` n `8`; equity avg `0.6703` n `164`; fx avg `-0.0113` n `6`; index avg `0.0685` n `27`; metal avg `-0.0434` n `20`; unknown avg `6.8403` n `1259`
- 1h: commodity avg `-0.2694` n `13`; crypto_alt avg `-0.4153` n `239`; crypto_major avg `-0.5776` n `8`; equity avg `-0.746` n `164`; fx avg `-0.0146` n `6`; index avg `-0.0549` n `27`; metal avg `-0.2169` n `20`; unknown avg `3.5458` n `1263`
- 4h: commodity avg `-0.0256` n `13`; crypto_alt avg `-0.3544` n `239`; crypto_major avg `-0.8151` n `8`; equity avg `-1.2825` n `164`; fx avg `-0.009` n `6`; index avg `-0.127` n `27`; metal avg `-0.1559` n `20`; unknown avg `2.4759` n `1257`
- 24h: commodity avg `-0.2817` n `13`; crypto_alt avg `-0.0815` n `239`; crypto_major avg `-0.3544` n `8`; equity avg `-0.0238` n `164`; fx avg `-0.1299` n `6`; index avg `0.0133` n `27`; metal avg `-1.1482` n `20`; unknown avg `0.294` n `1134`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
