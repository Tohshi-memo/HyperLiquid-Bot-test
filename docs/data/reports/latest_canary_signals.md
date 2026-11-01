# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T04:52:24.687531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0345` n `13`; crypto_alt avg `0.1304` n `238`; crypto_major avg `0.118` n `8`; equity avg `0.0645` n `156`; fx avg `0.0074` n `6`; index avg `0.0002` n `27`; metal avg `-0.0009` n `20`; unknown avg `0.3593` n `1262`
- 1h: commodity avg `-0.0238` n `13`; crypto_alt avg `0.0802` n `238`; crypto_major avg `0.164` n `8`; equity avg `0.1231` n `156`; fx avg `-0.003` n `6`; index avg `0.012` n `27`; metal avg `-0.0022` n `20`; unknown avg `0.7398` n `1248`
- 4h: commodity avg `-0.0378` n `13`; crypto_alt avg `0.2861` n `238`; crypto_major avg `0.0539` n `8`; equity avg `0.2425` n `156`; fx avg `-0.0048` n `6`; index avg `0.0311` n `27`; metal avg `0.0066` n `20`; unknown avg `2.239` n `1240`
- 24h: commodity avg `-0.0286` n `13`; crypto_alt avg `0.4519` n `238`; crypto_major avg `0.4269` n `8`; equity avg `0.3144` n `156`; fx avg `0.0035` n `6`; index avg `0.0023` n `27`; metal avg `0.0605` n `20`; unknown avg `2.9045` n `996`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
