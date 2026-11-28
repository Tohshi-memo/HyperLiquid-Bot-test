# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T09:07:28.484746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0183` n `13`; crypto_alt avg `0.1496` n `239`; crypto_major avg `0.0444` n `8`; equity avg `-0.0276` n `168`; fx avg `0.007` n `6`; index avg `-0.0065` n `27`; metal avg `-0.0018` n `20`; unknown avg `2.6355` n `1241`
- 1h: commodity avg `-0.0259` n `13`; crypto_alt avg `0.1701` n `239`; crypto_major avg `-0.2378` n `8`; equity avg `-0.0843` n `168`; fx avg `0.0085` n `6`; index avg `-0.0187` n `27`; metal avg `0.0083` n `20`; unknown avg `1.9423` n `1225`
- 4h: commodity avg `-0.0341` n `13`; crypto_alt avg `-0.3745` n `239`; crypto_major avg `-0.3583` n `8`; equity avg `-0.1113` n `168`; fx avg `-0.0022` n `6`; index avg `-0.0305` n `27`; metal avg `0.0093` n `20`; unknown avg `2.3607` n `1193`
- 24h: commodity avg `-0.6537` n `13`; crypto_alt avg `-3.06` n `239`; crypto_major avg `-3.0175` n `8`; equity avg `-0.7258` n `168`; fx avg `-0.0731` n `6`; index avg `-0.0345` n `27`; metal avg `-0.3848` n `20`; unknown avg `191.4453` n `1085`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
