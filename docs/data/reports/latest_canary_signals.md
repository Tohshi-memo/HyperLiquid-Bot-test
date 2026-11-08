# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T13:22:27.856285+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0797` n `13`; crypto_alt avg `0.1511` n `239`; crypto_major avg `0.2279` n `8`; equity avg `0.0432` n `158`; fx avg `-0.0042` n `6`; index avg `0.0069` n `27`; metal avg `0.0011` n `20`; unknown avg `-0.0466` n `1262`
- 1h: commodity avg `-0.0699` n `13`; crypto_alt avg `0.0639` n `239`; crypto_major avg `0.3335` n `8`; equity avg `0.1021` n `158`; fx avg `0.0125` n `6`; index avg `0.0087` n `27`; metal avg `-0.0032` n `20`; unknown avg `0.0269` n `1256`
- 4h: commodity avg `-0.0197` n `13`; crypto_alt avg `0.3093` n `239`; crypto_major avg `0.7182` n `8`; equity avg `0.2713` n `158`; fx avg `0.0085` n `6`; index avg `0.0129` n `27`; metal avg `-0.0037` n `20`; unknown avg `219.0194` n `1170`
- 24h: commodity avg `0.0509` n `13`; crypto_alt avg `-1.1484` n `239`; crypto_major avg `0.2845` n `8`; equity avg `0.2496` n `158`; fx avg `0.0101` n `6`; index avg `0.0249` n `27`; metal avg `-0.0291` n `20`; unknown avg `5.6776` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
