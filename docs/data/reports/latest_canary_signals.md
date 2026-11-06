# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T08:37:38.534351+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0873` n `13`; crypto_alt avg `-0.1378` n `239`; crypto_major avg `-0.1018` n `8`; equity avg `-0.0019` n `158`; fx avg `0.0063` n `6`; index avg `0.0164` n `27`; metal avg `-0.0183` n `20`; unknown avg `-0.1022` n `1256`
- 1h: commodity avg `-0.2796` n `13`; crypto_alt avg `0.5674` n `239`; crypto_major avg `0.4589` n `8`; equity avg `0.8193` n `158`; fx avg `0.032` n `6`; index avg `0.1516` n `27`; metal avg `0.2899` n `20`; unknown avg `0.8662` n `1194`
- 4h: commodity avg `-0.2446` n `13`; crypto_alt avg `0.0982` n `239`; crypto_major avg `-0.2734` n `8`; equity avg `0.0824` n `158`; fx avg `-0.0798` n `6`; index avg `0.0053` n `27`; metal avg `0.2022` n `20`; unknown avg `-0.0501` n `1166`
- 24h: commodity avg `0.9358` n `13`; crypto_alt avg `-4.4134` n `239`; crypto_major avg `-6.2682` n `8`; equity avg `-5.9807` n `158`; fx avg `-0.0326` n `6`; index avg `-0.8134` n `27`; metal avg `-0.2578` n `20`; unknown avg `241.4739` n `991`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
