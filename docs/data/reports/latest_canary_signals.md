# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T07:07:26.128869+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0919` n `13`; crypto_alt avg `-0.1865` n `239`; crypto_major avg `-0.082` n `8`; equity avg `-0.0841` n `161`; fx avg `0.0111` n `6`; index avg `-0.0334` n `27`; metal avg `0.0445` n `20`; unknown avg `6.7229` n `1255`
- 1h: commodity avg `-0.0729` n `13`; crypto_alt avg `-0.81` n `239`; crypto_major avg `-0.6719` n `8`; equity avg `-0.1043` n `161`; fx avg `-0.0146` n `6`; index avg `-0.0108` n `27`; metal avg `0.0448` n `20`; unknown avg `6.8322` n `1243`
- 4h: commodity avg `-0.0391` n `13`; crypto_alt avg `-1.1622` n `239`; crypto_major avg `-0.7492` n `8`; equity avg `0.6253` n `161`; fx avg `-0.0297` n `6`; index avg `0.0832` n `27`; metal avg `0.1972` n `20`; unknown avg `-0.0242` n `1213`
- 24h: commodity avg `0.3259` n `13`; crypto_alt avg `-1.802` n `239`; crypto_major avg `-2.9026` n `8`; equity avg `1.715` n `161`; fx avg `-0.2025` n `6`; index avg `0.2083` n `27`; metal avg `-0.0064` n `20`; unknown avg `1.3068` n `1160`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
