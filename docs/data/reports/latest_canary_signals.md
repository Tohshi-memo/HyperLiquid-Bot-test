# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T19:37:24.657651+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0502` n `13`; crypto_alt avg `0.0847` n `239`; crypto_major avg `0.1262` n `8`; equity avg `-0.0215` n `168`; fx avg `-0.0028` n `6`; index avg `-0.0013` n `27`; metal avg `-0.0059` n `20`; unknown avg `-0.2492` n `1265`
- 1h: commodity avg `-0.0203` n `13`; crypto_alt avg `0.4434` n `239`; crypto_major avg `0.5995` n `8`; equity avg `0.1812` n `168`; fx avg `0.0008` n `6`; index avg `0.0155` n `27`; metal avg `0.0274` n `20`; unknown avg `159.2816` n `1258`
- 4h: commodity avg `-0.2979` n `13`; crypto_alt avg `0.2039` n `239`; crypto_major avg `-0.0359` n `8`; equity avg `0.7401` n `168`; fx avg `-0.0442` n `6`; index avg `0.0917` n `27`; metal avg `0.0511` n `20`; unknown avg `181.9811` n `1226`
- 24h: commodity avg `-0.584` n `13`; crypto_alt avg `0.0725` n `239`; crypto_major avg `0.323` n `8`; equity avg `3.2237` n `168`; fx avg `-0.1504` n `6`; index avg `0.3183` n `27`; metal avg `0.8285` n `20`; unknown avg `260.7364` n `1039`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
