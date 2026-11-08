# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T15:52:31.214420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.008` n `13`; crypto_alt avg `0.0681` n `239`; crypto_major avg `-0.0063` n `8`; equity avg `0.0414` n `158`; fx avg `0.0029` n `6`; index avg `0.0038` n `27`; metal avg `0.0031` n `20`; unknown avg `0.9197` n `1262`
- 1h: commodity avg `-0.0255` n `13`; crypto_alt avg `0.1005` n `239`; crypto_major avg `-0.102` n `8`; equity avg `-0.1017` n `158`; fx avg `0.0088` n `6`; index avg `-0.0148` n `27`; metal avg `-0.0312` n `20`; unknown avg `4.619` n `1256`
- 4h: commodity avg `0.0129` n `13`; crypto_alt avg `-0.3791` n `239`; crypto_major avg `-0.0507` n `8`; equity avg `-0.1256` n `158`; fx avg `0.0012` n `6`; index avg `-0.0185` n `27`; metal avg `-0.0391` n `20`; unknown avg `1.9949` n `1242`
- 24h: commodity avg `0.0827` n `13`; crypto_alt avg `-0.9981` n `239`; crypto_major avg `0.2269` n `8`; equity avg `0.2264` n `158`; fx avg `0.0402` n `6`; index avg `-0.0072` n `27`; metal avg `-0.0461` n `20`; unknown avg `9.2369` n `1091`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
