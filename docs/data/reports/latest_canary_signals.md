# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T09:52:25.404934+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0802` n `13`; crypto_alt avg `-0.0065` n `239`; crypto_major avg `-0.2209` n `8`; equity avg `0.1412` n `158`; fx avg `-0.0081` n `6`; index avg `0.0302` n `27`; metal avg `-0.0165` n `20`; unknown avg `0.0186` n `1263`
- 1h: commodity avg `0.1655` n `13`; crypto_alt avg `0.423` n `239`; crypto_major avg `-0.3152` n `8`; equity avg `0.2568` n `158`; fx avg `-0.0197` n `6`; index avg `0.0315` n `27`; metal avg `0.0074` n `20`; unknown avg `124.569` n `1257`
- 4h: commodity avg `0.0034` n `13`; crypto_alt avg `0.4176` n `239`; crypto_major avg `-0.3777` n `8`; equity avg `0.0663` n `158`; fx avg `0.0136` n `6`; index avg `0.0094` n `27`; metal avg `-0.2071` n `20`; unknown avg `140.929` n `1111`
- 24h: commodity avg `-0.0538` n `13`; crypto_alt avg `-1.5499` n `239`; crypto_major avg `-3.3006` n `8`; equity avg `-0.459` n `158`; fx avg `-0.0934` n `6`; index avg `-0.032` n `27`; metal avg `0.2534` n `20`; unknown avg `0.3319` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
