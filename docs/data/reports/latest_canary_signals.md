# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T23:36:18.835012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.023` n `13`; crypto_alt avg `-0.0148` n `239`; crypto_major avg `0.0921` n `8`; equity avg `-0.0364` n `158`; fx avg `-0.0039` n `6`; index avg `-0.0168` n `27`; metal avg `-0.0148` n `20`; unknown avg `-0.0645` n `1262`
- 1h: commodity avg `0.0354` n `13`; crypto_alt avg `-0.4635` n `239`; crypto_major avg `-0.2168` n `8`; equity avg `-0.3344` n `158`; fx avg `0.012` n `6`; index avg `-0.0639` n `27`; metal avg `-0.0126` n `20`; unknown avg `0.0157` n `1202`
- 4h: commodity avg `-0.0265` n `13`; crypto_alt avg `0.4817` n `239`; crypto_major avg `0.3149` n `8`; equity avg `0.0418` n `158`; fx avg `0.0276` n `6`; index avg `0.0175` n `27`; metal avg `0.0221` n `20`; unknown avg `175.3282` n `1138`
- 24h: commodity avg `-1.7576` n `13`; crypto_alt avg `1.5329` n `239`; crypto_major avg `2.0522` n `8`; equity avg `-1.8323` n `158`; fx avg `0.0556` n `6`; index avg `0.036` n `27`; metal avg `1.2028` n `20`; unknown avg `29.6117` n `1036`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2661`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1655`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
