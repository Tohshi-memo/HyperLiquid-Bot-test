# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T20:52:25.168542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `13`; crypto_alt avg `-0.0361` n `239`; crypto_major avg `-0.0595` n `8`; equity avg `-0.1506` n `158`; fx avg `-0.0143` n `6`; index avg `-0.0232` n `27`; metal avg `0.0033` n `20`; unknown avg `28.1783` n `1260`
- 1h: commodity avg `0.0373` n `13`; crypto_alt avg `-0.2859` n `239`; crypto_major avg `-0.2258` n `8`; equity avg `-0.5939` n `158`; fx avg `-0.0049` n `6`; index avg `-0.0775` n `27`; metal avg `-0.0163` n `20`; unknown avg `69.7239` n `1232`
- 4h: commodity avg `-0.1196` n `13`; crypto_alt avg `0.1079` n `239`; crypto_major avg `-0.0551` n `8`; equity avg `-0.1589` n `158`; fx avg `-0.0286` n `6`; index avg `-0.0351` n `27`; metal avg `0.0183` n `20`; unknown avg `1.4049` n `1178`
- 24h: commodity avg `-0.0956` n `13`; crypto_alt avg `-1.0065` n `239`; crypto_major avg `0.0872` n `8`; equity avg `0.0037` n `158`; fx avg `0.0421` n `6`; index avg `-0.0551` n `27`; metal avg `-0.0268` n `20`; unknown avg `-0.0382` n `1024`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
