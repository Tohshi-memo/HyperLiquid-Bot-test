# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T12:07:30.599309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `13`; crypto_alt avg `-0.0369` n `238`; crypto_major avg `-0.1148` n `8`; equity avg `-0.0149` n `156`; fx avg `0.0086` n `6`; index avg `0.0006` n `27`; metal avg `-0.0004` n `20`; unknown avg `0.7555` n `1250`
- 1h: commodity avg `-0.0192` n `13`; crypto_alt avg `0.2071` n `238`; crypto_major avg `0.1647` n `8`; equity avg `0.0482` n `156`; fx avg `0.0046` n `6`; index avg `0.0033` n `27`; metal avg `0.0039` n `20`; unknown avg `22.4379` n `1238`
- 4h: commodity avg `0.0351` n `13`; crypto_alt avg `0.2625` n `238`; crypto_major avg `0.2507` n `8`; equity avg `0.0359` n `156`; fx avg `0.014` n `6`; index avg `-0.0062` n `27`; metal avg `0.032` n `20`; unknown avg `22.7723` n `1218`
- 24h: commodity avg `-0.2543` n `13`; crypto_alt avg `0.4294` n `238`; crypto_major avg `-0.4998` n `8`; equity avg `-1.2486` n `156`; fx avg `-0.0444` n `6`; index avg `-0.1204` n `27`; metal avg `-0.2673` n `20`; unknown avg `4.5763` n `1041`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
