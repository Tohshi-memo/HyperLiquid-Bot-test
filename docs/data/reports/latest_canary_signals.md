# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T18:07:30.444336+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `13`; crypto_alt avg `0.1791` n `239`; crypto_major avg `0.239` n `8`; equity avg `0.4043` n `158`; fx avg `0.0068` n `6`; index avg `0.041` n `27`; metal avg `0.0607` n `20`; unknown avg `10.9241` n `1253`
- 1h: commodity avg `0.0287` n `13`; crypto_alt avg `-0.4501` n `239`; crypto_major avg `-0.4287` n `8`; equity avg `-0.6701` n `158`; fx avg `-0.0167` n `6`; index avg `-0.0904` n `27`; metal avg `0.007` n `20`; unknown avg `16.8813` n `1251`
- 4h: commodity avg `-0.1745` n `13`; crypto_alt avg `0.194` n `239`; crypto_major avg `0.2052` n `8`; equity avg `-1.0574` n `158`; fx avg `-0.0004` n `6`; index avg `-0.0316` n `27`; metal avg `0.2008` n `20`; unknown avg `5.0898` n `1245`
- 24h: commodity avg `-0.0148` n `13`; crypto_alt avg `2.7784` n `239`; crypto_major avg `0.0384` n `8`; equity avg `2.0284` n `158`; fx avg `-0.1313` n `6`; index avg `0.1618` n `27`; metal avg `-0.1756` n `20`; unknown avg `53.1093` n `1076`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
