# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T20:22:34.727313+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0308` n `13`; crypto_alt avg `0.4045` n `239`; crypto_major avg `0.4201` n `8`; equity avg `0.4827` n `160`; fx avg `-0.0016` n `6`; index avg `0.0433` n `27`; metal avg `0.0589` n `20`; unknown avg `0.8847` n `1262`
- 1h: commodity avg `0.1042` n `13`; crypto_alt avg `0.5409` n `239`; crypto_major avg `0.4783` n `8`; equity avg `0.5143` n `160`; fx avg `-0.0076` n `6`; index avg `0.0467` n `27`; metal avg `0.052` n `20`; unknown avg `21.5366` n `1248`
- 4h: commodity avg `0.2082` n `13`; crypto_alt avg `-0.1825` n `239`; crypto_major avg `0.6434` n `8`; equity avg `-0.1587` n `160`; fx avg `0.0307` n `6`; index avg `-0.0181` n `27`; metal avg `0.1128` n `20`; unknown avg `18.6126` n `1248`
- 24h: commodity avg `0.2181` n `13`; crypto_alt avg `-1.8708` n `239`; crypto_major avg `-2.7099` n `8`; equity avg `-1.9819` n `160`; fx avg `-0.0708` n `6`; index avg `-0.232` n `27`; metal avg `-0.6703` n `20`; unknown avg `0.0545` n `1161`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2557`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
