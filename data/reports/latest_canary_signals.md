# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T13:07:43.502270+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.037` n `13`; crypto_alt avg `0.0372` n `239`; crypto_major avg `-0.1397` n `8`; equity avg `0.1289` n `158`; fx avg `0.0042` n `6`; index avg `-0.0003` n `27`; metal avg `0.0497` n `20`; unknown avg `19.0374` n `1257`
- 1h: commodity avg `0.0417` n `13`; crypto_alt avg `0.837` n `239`; crypto_major avg `0.5004` n `8`; equity avg `0.5891` n `158`; fx avg `0.0258` n `6`; index avg `0.0623` n `27`; metal avg `0.0813` n `20`; unknown avg `19.0148` n `1257`
- 4h: commodity avg `-0.2653` n `13`; crypto_alt avg `1.6022` n `239`; crypto_major avg `0.0786` n `8`; equity avg `1.0869` n `158`; fx avg `-0.0439` n `6`; index avg `0.0944` n `27`; metal avg `0.0977` n `20`; unknown avg `0.6631` n `1251`
- 24h: commodity avg `-0.4896` n `13`; crypto_alt avg `-0.1396` n `239`; crypto_major avg `-3.1016` n `8`; equity avg `0.3465` n `158`; fx avg `-0.1395` n `6`; index avg `0.0651` n `27`; metal avg `0.3822` n `20`; unknown avg `0.7535` n `1030`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
