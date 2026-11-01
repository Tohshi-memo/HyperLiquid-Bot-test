# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T04:07:27.301147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0104` n `13`; crypto_alt avg `-0.1644` n `238`; crypto_major avg `-0.0886` n `8`; equity avg `-0.0157` n `156`; fx avg `0.0007` n `6`; index avg `0.0022` n `27`; metal avg `-0.0008` n `20`; unknown avg `0.4592` n `1248`
- 1h: commodity avg `0.0603` n `13`; crypto_alt avg `0.1518` n `238`; crypto_major avg `-0.1033` n `8`; equity avg `0.0498` n `156`; fx avg `-0.0085` n `6`; index avg `-0.0018` n `27`; metal avg `0.0065` n `20`; unknown avg `0.4937` n `1244`
- 4h: commodity avg `0.009` n `13`; crypto_alt avg `-0.0255` n `238`; crypto_major avg `-0.0534` n `8`; equity avg `0.1191` n `156`; fx avg `0.0041` n `6`; index avg `-0.0008` n `27`; metal avg `0.0094` n `20`; unknown avg `2.0381` n `1194`
- 24h: commodity avg `-0.0277` n `13`; crypto_alt avg `-0.2239` n `238`; crypto_major avg `-0.1841` n `8`; equity avg `0.0748` n `156`; fx avg `0.002` n `6`; index avg `-0.0248` n `27`; metal avg `0.0597` n `20`; unknown avg `2.7204` n `996`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
