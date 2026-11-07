# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T20:52:27.968949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0031` n `13`; crypto_alt avg `-0.6167` n `239`; crypto_major avg `-0.3741` n `8`; equity avg `-0.0994` n `158`; fx avg `0.0105` n `6`; index avg `-0.0056` n `27`; metal avg `-0.0017` n `20`; unknown avg `-0.532` n `1262`
- 1h: commodity avg `0.0311` n `13`; crypto_alt avg `-0.6198` n `239`; crypto_major avg `-0.4844` n `8`; equity avg `-0.1385` n `158`; fx avg `0.0019` n `6`; index avg `-0.0057` n `27`; metal avg `-0.0033` n `20`; unknown avg `-0.6098` n `1240`
- 4h: commodity avg `0.05` n `13`; crypto_alt avg `-0.5921` n `239`; crypto_major avg `-0.3735` n `8`; equity avg `0.026` n `158`; fx avg `-0.0041` n `6`; index avg `0.0165` n `27`; metal avg `0.0001` n `20`; unknown avg `-0.3959` n `1209`
- 24h: commodity avg `0.1138` n `13`; crypto_alt avg `-2.0063` n `239`; crypto_major avg `-0.9486` n `8`; equity avg `0.1022` n `158`; fx avg `-0.0008` n `6`; index avg `0.0662` n `27`; metal avg `0.0143` n `20`; unknown avg `-0.5327` n `1075`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
