# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T16:07:28.107517+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0691` n `13`; crypto_alt avg `-0.1184` n `239`; crypto_major avg `-0.1726` n `8`; equity avg `-0.4473` n `158`; fx avg `-0.0075` n `6`; index avg `-0.0545` n `27`; metal avg `0.0353` n `20`; unknown avg `4.1206` n `1245`
- 1h: commodity avg `-0.1582` n `13`; crypto_alt avg `-0.1956` n `239`; crypto_major avg `0.2069` n `8`; equity avg `-0.3952` n `158`; fx avg `-0.0047` n `6`; index avg `-0.0226` n `27`; metal avg `0.1157` n `20`; unknown avg `3.3581` n `1243`
- 4h: commodity avg `-0.414` n `13`; crypto_alt avg `-0.0732` n `239`; crypto_major avg `-0.4956` n `8`; equity avg `-1.5113` n `158`; fx avg `-0.0342` n `6`; index avg `-0.0268` n `27`; metal avg `0.0281` n `20`; unknown avg `50.2366` n `1243`
- 24h: commodity avg `-0.1318` n `13`; crypto_alt avg `2.572` n `239`; crypto_major avg `-0.6546` n `8`; equity avg `2.6338` n `158`; fx avg `-0.0957` n `6`; index avg `0.1461` n `27`; metal avg `-0.018` n `20`; unknown avg `25.8114` n `1076`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
