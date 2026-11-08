# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T05:52:25.591322+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `13`; crypto_alt avg `0.0102` n `239`; crypto_major avg `-0.0115` n `8`; equity avg `0.0194` n `158`; fx avg `0.0079` n `6`; index avg `0.0019` n `27`; metal avg `0.0002` n `20`; unknown avg `62.4811` n `1260`
- 1h: commodity avg `-0.0173` n `13`; crypto_alt avg `0.1942` n `239`; crypto_major avg `0.0937` n `8`; equity avg `0.0939` n `158`; fx avg `0.0153` n `6`; index avg `-0.0008` n `27`; metal avg `0.0064` n `20`; unknown avg `75.5983` n `1252`
- 4h: commodity avg `-0.0247` n `13`; crypto_alt avg `-0.0658` n `239`; crypto_major avg `0.0535` n `8`; equity avg `0.0823` n `158`; fx avg `0.0136` n `6`; index avg `-0.0062` n `27`; metal avg `-0.0068` n `20`; unknown avg `-0.1586` n `1238`
- 24h: commodity avg `0.1275` n `13`; crypto_alt avg `-1.8584` n `239`; crypto_major avg `-0.688` n `8`; equity avg `-0.0465` n `158`; fx avg `0.0483` n `6`; index avg `0.0338` n `27`; metal avg `-0.0552` n `20`; unknown avg `162.4897` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
