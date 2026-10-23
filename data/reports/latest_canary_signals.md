# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T21:22:36.552347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `13`; crypto_alt avg `-0.0944` n `237`; crypto_major avg `-0.0176` n `8`; equity avg `-0.0441` n `152`; fx avg `0.0146` n `6`; index avg `-0.0029` n `26`; metal avg `0.0026` n `20`; unknown avg `-0.1017` n `1230`
- 1h: commodity avg `0.0255` n `13`; crypto_alt avg `0.4802` n `237`; crypto_major avg `0.2987` n `8`; equity avg `0.0123` n `152`; fx avg `0.018` n `6`; index avg `0.0089` n `26`; metal avg `0.0041` n `20`; unknown avg `0.1356` n `1218`
- 4h: commodity avg `0.1486` n `13`; crypto_alt avg `-1.0114` n `237`; crypto_major avg `-0.5703` n `8`; equity avg `-0.3271` n `152`; fx avg `0.0034` n `6`; index avg `0.0207` n `26`; metal avg `-0.0096` n `20`; unknown avg `0.3206` n `1143`
- 24h: commodity avg `0.4656` n `13`; crypto_alt avg `0.1167` n `237`; crypto_major avg `0.1366` n `8`; equity avg `1.1904` n `152`; fx avg `-0.0689` n `6`; index avg `0.1017` n `26`; metal avg `-0.1498` n `20`; unknown avg `0.1231` n `1022`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1991`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
