# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T15:05:19.230567+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.013` n `13`; crypto_alt avg `-0.0154` n `239`; crypto_major avg `-0.0877` n `8`; equity avg `-0.0212` n `158`; fx avg `-0.0001` n `6`; index avg `-0.0034` n `27`; metal avg `-0.007` n `20`; unknown avg `3.7873` n `1258`
- 1h: commodity avg `-0.0042` n `13`; crypto_alt avg `0.1991` n `239`; crypto_major avg `0.1894` n `8`; equity avg `-0.0017` n `158`; fx avg `0.0051` n `6`; index avg `-0.0156` n `27`; metal avg `-0.0059` n `20`; unknown avg `0.3926` n `1248`
- 4h: commodity avg `0.0557` n `13`; crypto_alt avg `-0.2549` n `239`; crypto_major avg `0.2691` n `8`; equity avg `0.0501` n `158`; fx avg `-0.0092` n `6`; index avg `-0.0078` n `27`; metal avg `-0.0045` n `20`; unknown avg `0.365` n `1242`
- 24h: commodity avg `0.0967` n `13`; crypto_alt avg `-1.3133` n `239`; crypto_major avg `-0.0904` n `8`; equity avg `0.1896` n `158`; fx avg `0.0242` n `6`; index avg `0.0048` n `27`; metal avg `-0.0454` n `20`; unknown avg `7.6781` n `1091`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
