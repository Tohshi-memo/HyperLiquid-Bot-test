# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T03:52:26.738948+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0196` n `13`; crypto_alt avg `0.0322` n `239`; crypto_major avg `0.0589` n `8`; equity avg `-0.0879` n `158`; fx avg `-0.0009` n `6`; index avg `0.0062` n `27`; metal avg `0.0069` n `20`; unknown avg `-0.0416` n `1263`
- 1h: commodity avg `0.0678` n `13`; crypto_alt avg `-0.278` n `239`; crypto_major avg `-0.2487` n `8`; equity avg `-0.0779` n `158`; fx avg `0.0206` n `6`; index avg `0.0302` n `27`; metal avg `-0.0129` n `20`; unknown avg `-0.3376` n `1252`
- 4h: commodity avg `0.174` n `13`; crypto_alt avg `1.2841` n `239`; crypto_major avg `0.6375` n `8`; equity avg `1.6135` n `158`; fx avg `-0.0582` n `6`; index avg `0.2821` n `27`; metal avg `0.5022` n `20`; unknown avg `2.6055` n `1236`
- 24h: commodity avg `0.1433` n `13`; crypto_alt avg `-1.743` n `239`; crypto_major avg `-2.2453` n `8`; equity avg `0.7325` n `158`; fx avg `-0.0723` n `6`; index avg `0.1135` n `27`; metal avg `0.4918` n `20`; unknown avg `1.1698` n `988`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
