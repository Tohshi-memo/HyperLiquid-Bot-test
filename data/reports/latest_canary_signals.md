# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T10:22:24.662310+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1032` n `13`; crypto_alt avg `0.0843` n `239`; crypto_major avg `-0.0838` n `8`; equity avg `0.1058` n `158`; fx avg `-0.0012` n `6`; index avg `0.0126` n `27`; metal avg `0.0271` n `20`; unknown avg `-0.0671` n `1263`
- 1h: commodity avg `-0.0086` n `13`; crypto_alt avg `0.2792` n `239`; crypto_major avg `-0.4378` n `8`; equity avg `0.4828` n `158`; fx avg `-0.0029` n `6`; index avg `0.0656` n `27`; metal avg `0.0551` n `20`; unknown avg `-0.1819` n `1257`
- 4h: commodity avg `0.068` n `13`; crypto_alt avg `0.5584` n `239`; crypto_major avg `-0.5307` n `8`; equity avg `0.2803` n `158`; fx avg `0.0761` n `6`; index avg `0.0396` n `27`; metal avg `-0.1026` n `20`; unknown avg `170.544` n `1127`
- 24h: commodity avg `-0.0862` n `13`; crypto_alt avg `-1.5996` n `239`; crypto_major avg `-3.5753` n `8`; equity avg `-0.2664` n `158`; fx avg `-0.0912` n `6`; index avg `-0.0217` n `27`; metal avg `0.3011` n `20`; unknown avg `0.1684` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
