# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T08:07:30.075883+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0516` n `13`; crypto_alt avg `0.3448` n `239`; crypto_major avg `0.1749` n `8`; equity avg `0.1195` n `158`; fx avg `0.0073` n `6`; index avg `0.0092` n `27`; metal avg `0.0458` n `20`; unknown avg `-0.0542` n `1194`
- 1h: commodity avg `0.0072` n `13`; crypto_alt avg `0.3875` n `239`; crypto_major avg `0.3177` n `8`; equity avg `0.4253` n `158`; fx avg `-0.0222` n `6`; index avg `0.046` n `27`; metal avg `0.1149` n `20`; unknown avg `0.5494` n `1194`
- 4h: commodity avg `-0.017` n `13`; crypto_alt avg `0.4414` n `239`; crypto_major avg `-0.151` n `8`; equity avg `0.282` n `158`; fx avg `-0.0869` n `6`; index avg `0.0222` n `27`; metal avg `0.1203` n `20`; unknown avg `0.0328` n `1166`
- 24h: commodity avg `1.1933` n `13`; crypto_alt avg `-3.6108` n `239`; crypto_major avg `-5.7753` n `8`; equity avg `-5.7779` n `158`; fx avg `-0.0083` n `6`; index avg `-0.7875` n `27`; metal avg `-0.3397` n `20`; unknown avg `241.4702` n `991`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
