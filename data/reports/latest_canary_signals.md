# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T12:52:25.175401+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0896` n `13`; crypto_alt avg `0.3015` n `239`; crypto_major avg `0.194` n `8`; equity avg `0.4048` n `158`; fx avg `-0.0022` n `6`; index avg `0.0523` n `27`; metal avg `-0.0129` n `20`; unknown avg `-0.0098` n `1263`
- 1h: commodity avg `0.094` n `13`; crypto_alt avg `1.2504` n `239`; crypto_major avg `0.9111` n `8`; equity avg `0.5995` n `158`; fx avg `0.0176` n `6`; index avg `0.0568` n `27`; metal avg `-0.0068` n `20`; unknown avg `19.0932` n `1251`
- 4h: commodity avg `-0.3057` n `13`; crypto_alt avg `1.7411` n `239`; crypto_major avg `0.366` n `8`; equity avg `1.0326` n `158`; fx avg `-0.0473` n `6`; index avg `0.1278` n `27`; metal avg `0.0812` n `20`; unknown avg `153.9199` n `1251`
- 24h: commodity avg `-0.5245` n `13`; crypto_alt avg `-0.1055` n `239`; crypto_major avg `-2.8626` n `8`; equity avg `0.2998` n `158`; fx avg `-0.126` n `6`; index avg `0.0637` n `27`; metal avg `0.3325` n `20`; unknown avg `0.0394` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
