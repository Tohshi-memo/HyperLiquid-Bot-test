# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T04:22:42.220387+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0126` n `13`; crypto_alt avg `0.0827` n `239`; crypto_major avg `0.1612` n `8`; equity avg `0.221` n `160`; fx avg `0.0017` n `6`; index avg `0.0154` n `27`; metal avg `0.0489` n `20`; unknown avg `0.4676` n `1259`
- 1h: commodity avg `0.039` n `13`; crypto_alt avg `0.3787` n `239`; crypto_major avg `0.2377` n `8`; equity avg `-0.135` n `160`; fx avg `-0.0083` n `6`; index avg `-0.0254` n `27`; metal avg `-0.0248` n `20`; unknown avg `0.1887` n `1241`
- 4h: commodity avg `-0.1488` n `13`; crypto_alt avg `0.1627` n `239`; crypto_major avg `-0.3261` n `8`; equity avg `-0.7934` n `160`; fx avg `-0.0055` n `6`; index avg `-0.1115` n `27`; metal avg `-0.0201` n `20`; unknown avg `0.2268` n `1239`
- 24h: commodity avg `-0.7961` n `13`; crypto_alt avg `0.926` n `239`; crypto_major avg `-0.5291` n `8`; equity avg `3.4204` n `160`; fx avg `0.032` n `6`; index avg `0.3274` n `27`; metal avg `0.0545` n `20`; unknown avg `188.5774` n `1071`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1925`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
