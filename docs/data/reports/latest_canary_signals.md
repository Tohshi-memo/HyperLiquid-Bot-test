# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T20:37:27.011997+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0396` n `13`; crypto_alt avg `-0.0047` n `239`; crypto_major avg `-0.0258` n `8`; equity avg `0.0288` n `158`; fx avg `0.0002` n `6`; index avg `-0.0096` n `27`; metal avg `0.0068` n `20`; unknown avg `7.0396` n `1264`
- 1h: commodity avg `0.0714` n `13`; crypto_alt avg `0.0291` n `239`; crypto_major avg `-0.0325` n `8`; equity avg `-0.052` n `158`; fx avg `0.0315` n `6`; index avg `-0.0119` n `27`; metal avg `0.08` n `20`; unknown avg `171.2049` n `1236`
- 4h: commodity avg `-0.2363` n `13`; crypto_alt avg `-1.1196` n `239`; crypto_major avg `-0.8419` n `8`; equity avg `0.3394` n `158`; fx avg `0.0128` n `6`; index avg `0.0479` n `27`; metal avg `0.18` n `20`; unknown avg `6.7689` n `1238`
- 24h: commodity avg `-1.7252` n `13`; crypto_alt avg `1.6219` n `239`; crypto_major avg `1.9064` n `8`; equity avg `-0.9723` n `158`; fx avg `0.0684` n `6`; index avg `0.1342` n `27`; metal avg `1.3627` n `20`; unknown avg `5.9412` n `1117`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2662`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
