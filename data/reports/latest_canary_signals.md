# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T16:22:30.850001+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1784` n `13`; crypto_alt avg `-0.2164` n `239`; crypto_major avg `-0.1961` n `8`; equity avg `-0.1364` n `158`; fx avg `0.0112` n `6`; index avg `-0.0193` n `27`; metal avg `-0.0106` n `20`; unknown avg `44.668` n `1255`
- 1h: commodity avg `0.0669` n `13`; crypto_alt avg `-0.6472` n `239`; crypto_major avg `-0.3928` n `8`; equity avg `-0.6291` n `158`; fx avg `-0.0024` n `6`; index avg `-0.0699` n `27`; metal avg `-0.0182` n `20`; unknown avg `36.3084` n `1249`
- 4h: commodity avg `-0.19` n `13`; crypto_alt avg `-0.4263` n `239`; crypto_major avg `-0.6805` n `8`; equity avg `-1.3919` n `158`; fx avg `-0.0511` n `6`; index avg `-0.0239` n `27`; metal avg `-0.0194` n `20`; unknown avg `58.3315` n `1243`
- 24h: commodity avg `0.1194` n `13`; crypto_alt avg `1.1316` n `239`; crypto_major avg `-1.8228` n `8`; equity avg `-0.1103` n `158`; fx avg `-0.0843` n `6`; index avg `-0.0503` n `27`; metal avg `-0.292` n `20`; unknown avg `42.2113` n `1076`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
