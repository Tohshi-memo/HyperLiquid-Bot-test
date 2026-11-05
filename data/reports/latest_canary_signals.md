# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T10:22:25.755282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.017` n `13`; crypto_alt avg `-0.0731` n `239`; crypto_major avg `-0.0235` n `8`; equity avg `0.0491` n `158`; fx avg `0.0078` n `6`; index avg `0.0159` n `27`; metal avg `0.0162` n `20`; unknown avg `0.0197` n `1261`
- 1h: commodity avg `0.1725` n `13`; crypto_alt avg `-0.1165` n `239`; crypto_major avg `0.0434` n `8`; equity avg `0.2937` n `158`; fx avg `-0.0137` n `6`; index avg `0.0649` n `27`; metal avg `-0.0038` n `20`; unknown avg `14.1122` n `1231`
- 4h: commodity avg `0.5311` n `13`; crypto_alt avg `0.1242` n `239`; crypto_major avg `0.1679` n `8`; equity avg `0.4362` n `158`; fx avg `-0.0471` n `6`; index avg `0.0703` n `27`; metal avg `-0.0058` n `20`; unknown avg `15.4288` n `1151`
- 24h: commodity avg `-1.245` n `13`; crypto_alt avg `0.6745` n `239`; crypto_major avg `1.5879` n `8`; equity avg `-3.298` n `158`; fx avg `-0.0277` n `6`; index avg `-0.2814` n `27`; metal avg `0.4719` n `20`; unknown avg `0.2392` n `1078`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2478`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
