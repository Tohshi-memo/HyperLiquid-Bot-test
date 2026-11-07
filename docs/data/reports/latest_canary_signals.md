# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T13:22:27.480836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `13`; crypto_alt avg `-0.0273` n `239`; crypto_major avg `0.0465` n `8`; equity avg `-0.0577` n `158`; fx avg `0.003` n `6`; index avg `-0.005` n `27`; metal avg `-0.0034` n `20`; unknown avg `0.035` n `1261`
- 1h: commodity avg `-0.0319` n `13`; crypto_alt avg `-0.1293` n `239`; crypto_major avg `-0.2191` n `8`; equity avg `0.0561` n `158`; fx avg `0.0151` n `6`; index avg `0.0074` n `27`; metal avg `0.0` n `20`; unknown avg `0.8177` n `1255`
- 4h: commodity avg `0.0252` n `13`; crypto_alt avg `-0.5401` n `239`; crypto_major avg `-0.4891` n `8`; equity avg `-0.0986` n `158`; fx avg `0.0571` n `6`; index avg `-0.0158` n `27`; metal avg `-0.0` n `20`; unknown avg `0.1019` n `1249`
- 24h: commodity avg `-0.0929` n `13`; crypto_alt avg `-1.4024` n `239`; crypto_major avg `-0.6596` n `8`; equity avg `-0.419` n `158`; fx avg `0.016` n `6`; index avg `-0.0424` n `27`; metal avg `-0.0258` n `20`; unknown avg `0.2793` n `1115`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
