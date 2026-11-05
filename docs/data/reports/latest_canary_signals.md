# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T04:22:35.331795+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `13`; crypto_alt avg `-0.0907` n `239`; crypto_major avg `-0.0872` n `8`; equity avg `-0.2595` n `158`; fx avg `-0.0091` n `6`; index avg `-0.0491` n `27`; metal avg `-0.0917` n `20`; unknown avg `0.7303` n `1263`
- 1h: commodity avg `-0.0545` n `13`; crypto_alt avg `-0.6153` n `239`; crypto_major avg `-0.6487` n `8`; equity avg `-0.6541` n `158`; fx avg `0.0004` n `6`; index avg `-0.148` n `27`; metal avg `-0.0858` n `20`; unknown avg `-0.4517` n `1243`
- 4h: commodity avg `-0.2877` n `13`; crypto_alt avg `0.1593` n `239`; crypto_major avg `-0.5279` n `8`; equity avg `-0.9389` n `158`; fx avg `0.021` n `6`; index avg `-0.215` n `27`; metal avg `0.3126` n `20`; unknown avg `3.8987` n `1242`
- 24h: commodity avg `-1.7352` n `13`; crypto_alt avg `3.3053` n `239`; crypto_major avg `3.4925` n `8`; equity avg `0.5604` n `158`; fx avg `0.1565` n `6`; index avg `0.3353` n `27`; metal avg `1.8612` n `20`; unknown avg `33.4431` n `1024`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2513`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1957`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1933`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
