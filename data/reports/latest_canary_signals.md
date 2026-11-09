# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T04:52:26.671467+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `13`; crypto_alt avg `-0.3396` n `239`; crypto_major avg `-0.3988` n `8`; equity avg `-0.1429` n `158`; fx avg `-0.0075` n `6`; index avg `-0.0042` n `27`; metal avg `-0.0673` n `20`; unknown avg `1.5197` n `1263`
- 1h: commodity avg `0.0504` n `13`; crypto_alt avg `-0.1767` n `239`; crypto_major avg `-0.3005` n `8`; equity avg `-0.3264` n `158`; fx avg `-0.012` n `6`; index avg `-0.0568` n `27`; metal avg `0.0176` n `20`; unknown avg `19.3504` n `1247`
- 4h: commodity avg `0.2254` n `13`; crypto_alt avg `0.0018` n `239`; crypto_major avg `-0.4074` n `8`; equity avg `0.9095` n `158`; fx avg `-0.0434` n `6`; index avg `0.1284` n `27`; metal avg `0.1522` n `20`; unknown avg `0.7482` n `1232`
- 24h: commodity avg `0.1888` n `13`; crypto_alt avg `-1.6033` n `239`; crypto_major avg `-2.4241` n `8`; equity avg `0.4707` n `158`; fx avg `-0.0835` n `6`; index avg `0.0644` n `27`; metal avg `0.5204` n `20`; unknown avg `1.5596` n `984`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
