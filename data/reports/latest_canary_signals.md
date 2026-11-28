# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T11:22:25.882918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.56` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0157` n `13`; crypto_alt avg `-0.0168` n `239`; crypto_major avg `-0.0223` n `8`; equity avg `0.0223` n `168`; fx avg `0.0019` n `6`; index avg `0.003` n `27`; metal avg `0.0015` n `20`; unknown avg `1.6845` n `1267`
- 1h: commodity avg `-0.0199` n `13`; crypto_alt avg `-0.1857` n `239`; crypto_major avg `-0.247` n `8`; equity avg `-0.141` n `168`; fx avg `0.0019` n `6`; index avg `-0.0163` n `27`; metal avg `0.0065` n `20`; unknown avg `0.5774` n `1261`
- 4h: commodity avg `-0.045` n `13`; crypto_alt avg `-0.5587` n `239`; crypto_major avg `-0.5752` n `8`; equity avg `-0.1443` n `168`; fx avg `0.006` n `6`; index avg `-0.0199` n `27`; metal avg `0.0152` n `20`; unknown avg `3.4508` n `1215`
- 24h: commodity avg `-0.6305` n `13`; crypto_alt avg `-3.4408` n `239`; crypto_major avg `-3.5795` n `8`; equity avg `-0.4722` n `168`; fx avg `-0.076` n `6`; index avg `-0.0001` n `27`; metal avg `-0.2197` n `20`; unknown avg `190.4643` n `1089`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
