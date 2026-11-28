# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T04:52:24.703593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `13`; crypto_alt avg `-0.0227` n `239`; crypto_major avg `-0.0019` n `8`; equity avg `-0.0338` n `168`; fx avg `-0.0006` n `6`; index avg `-0.001` n `27`; metal avg `0.0017` n `20`; unknown avg `0.5342` n `1267`
- 1h: commodity avg `-0.0083` n `13`; crypto_alt avg `-0.3582` n `239`; crypto_major avg `-0.0705` n `8`; equity avg `0.0636` n `168`; fx avg `-0.0015` n `6`; index avg `-0.0023` n `27`; metal avg `0.0077` n `20`; unknown avg `72.0735` n `1245`
- 4h: commodity avg `0.0733` n `13`; crypto_alt avg `-0.8446` n `239`; crypto_major avg `-0.0003` n `8`; equity avg `0.2491` n `168`; fx avg `0.0124` n `6`; index avg `0.0165` n `27`; metal avg `0.0231` n `20`; unknown avg `2.8735` n `1245`
- 24h: commodity avg `-0.7941` n `13`; crypto_alt avg `-1.912` n `239`; crypto_major avg `-1.7583` n `8`; equity avg `0.6971` n `168`; fx avg `-0.1177` n `6`; index avg `0.0548` n `27`; metal avg `0.0982` n `20`; unknown avg `214.2915` n `979`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
